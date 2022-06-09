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

# Creating the Dash App:
app = DjangoDash("nk_img_dashboard")

app.layout = html.Div(
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

@app.callback(
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