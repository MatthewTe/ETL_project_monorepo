# Importing Dash methods:
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash

# Importing plotly methods:
import plotly.express as px
import plotly.graph_objects as go

# Importing sk methods for image processing:
from skimage import io

# Importing methods for extracting Zotero data:
from ..zotero_logic import build_collection_heatmap, extract_zotero_items_for_date

# Data management methods:
import datetime
import os

# Creating the Dash App for the North Korea images:
image_app = DjangoDash("nk_img_dashboard")

image_app.layout = html.Div(
    children=[

        html.H1("The DPRK (from 2005)"),

        dcc.Tabs(id="nk-map-tabs", value='nk-map-admin', children=[
            dcc.Tab(label="Administrative Regions", value="nk-map-admin"),
            dcc.Tab(label="Transportation Infrastructure", value="nk-map-transport"),
            dcc.Tab(label="Elevation", value="nk-map-elevation"),
        ]),

        dcc.Graph(id="nk-map")
    ]
)

@image_app.callback(
    Output("nk-map", "figure"),
    Input("nk-map-tabs", "value")
)
def render_nk_map(tab):
    """The Dash function that renders a North Korean map depending on the tab that is 
    input in the Dash app.
    """
    # Specifying the dimensions of the image (px):
    img_height = 1182
    img_width = 975    
    scale_factor = 1
    
    # Adding the image to the layout based on the tab seelected:
    if tab == "nk-map-admin":
        # Loading the image from the static:
        img = io.imread("application_frontend/static/application_frontend/imgs/north_korea/korea_north_admin_2005.jpg")
        fig = px.imshow(img)
        
    elif tab == "nk-map-transport":
        img = io.imread("application_frontend/static/application_frontend/imgs/north_korea/korea_north_pol_2005.jpg")
        fig = px.imshow(img)
        

    elif tab == "nk-map-elevation":
        img = io.imread("application_frontend/static/application_frontend/imgs/north_korea/korea_north_rel_2005.jpg")
        fig = px.imshow(img)
        

    # Configure other layout
    fig.update_layout(
        width=img_width * 1.5,
        height=img_height * scale_factor,
        margin={"l": 0, "r": 0, "t": 0, "b": 0},
    )

    return fig

# Creating the zotero heatmap for korean readings:
# Loading the heatmap for my zotero sources to be displayed in the dashboard:
heatmap_data = build_collection_heatmap(
    api_key=os.environ["ZOTERO_API_KEY"],
    library_id=os.environ["ZOTERO_LIBRARY_ID"],
    collection_name="Korean-Peninsula"
)

# Dash App for my Zotero North Korea Readings:
nk_zotero_app = DjangoDash("nk_zotero_sources_dashboard")

nk_zotero_app.layout = html.Div(
    children=[
        html.H1("My Saved Readings on the Korean Peninsula"),
        dcc.Graph(id="nk-zotero-heatmap", figure=heatmap_data["heatmap"]),

        html.Div(id="daily_readings")
    ]
)
@nk_zotero_app.callback(
    Output("daily_readings", "children"),
    Input("nk-zotero-heatmap", "clickData"))
def display_daily_information_from_heatmap(heatmap_point):
    """The callback that renders the plotly figure displaying a list of
    sources for a single day given an on click event from the heatmap. 
    """
    # Function that constructs a Dash Html element for a zotero item dict:
    def build_html_element(item):
        """Takes in a zotero item dict and generates a dash html element
        for use in the Dash callback.
        
        Args:
            item (dict): The dict of a single zotero item.
            
        Returns:
            dash_html_components.Div: The Div element containing the formatted html 
                to be rendered
        """
        # Empty list to populate:
        children = [
            html.A(target="_blank", children=[html.H1(source["title"])], href=source["url"], rel="noopener noreferrer"),
        ]
        
        # Adding author information:
        if "creators" in source:
            for author in source["creators"]:
                children.append(html.P(f"{author['firstName']} {author['lastName']}"))
        
        if "dateAdded" in source:
            children.append(html.P(f"Read On: {source['dateAdded']}"))
        
        if "websiteType" in source:
            children.append(html.P(f"Site Type: {source['websiteType']}"))
        
        if "websiteTitle" in source:
            children.append(html.P(f"Source: {source['websiteTitle']}"))
        
        if "itemType" in source:
            children.append(html.P(f"Read as a {source['itemType']}"))

        # Extracting values from item:        
        div = html.Div(children, className='heatmap_day_source')
        
        return div
    
    # If there is not data render the zotero items for today:
    if heatmap_point is None:
        return html.H1("No Date Selected - Click on a day to see its sources in full")
    
    # If there is data extract the date from clickData object and get date:
    heatmap_date = heatmap_point["points"][0]["text"]

    # Converting date into the correct format for the zotero method:
    formatted_date = datetime.datetime.strptime(heatmap_date, '%d %b, %Y').strftime("%Y-%m-%d")

    # Using formatted date to query sources for specific day:
    daily_sources = extract_zotero_items_for_date(
        date=formatted_date,
        collection=heatmap_data["collection"]
    )

    # Iterating through the collection data and building an html response:
    content_lst = []
    for source in daily_sources:
        
        source_html_item = build_html_element(source)
        content_lst.append(source_html_item)
    
    main_div = html.Div(content_lst)

    return main_div


