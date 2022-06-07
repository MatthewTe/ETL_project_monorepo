# Importing data parsing logic:
from .sipri_logic import build_company_timeseries, build_company_timeseries_subplot_fig

# Importing Dash methods:
from dash import dcc, html, Input, Output
from django_plotly_dash import DjangoDash

# Creating the Dash App:
app = DjangoDash("SIPRI_arms_companies")

app.layout = html.Div(
    children=[

        # The main input for searches:
        html.Div([
            "Select Company:", 
            dcc.Input(id="company-input", value="Lockheed Martin Corp.", type="text"),
            dcc.RangeSlider(
                min=2002,
                max=2020,
                step=None,
                value=[2002, 2020],
                marks={
                    2002: "2002",
                    2003: "2003",
                    2004: "2004",
                    2005: "2005",
                    2006: "2006",
                    2007: "2007",
                    2008: "2008",
                    2009: "2009",
                    2010: "2010",
                    2011: "2011",
                    2012: "2012",
                    2013: "2013",
                    2014: "2014",
                    2015: "2015",
                    2016: "2016",
                    2017: "2017",
                    2018: "2018",
                    2019: "2019",
                    2020: "2020"
                }, 
                id="date-range-slider")
            ]),

        html.H1(id="company-header"),

        html.Div(id="company-info-desc"),

        html.Div(
            id="main-company-graph",
            children=[dcc.Graph(id="company-subplot")]
            )
    ]
)


# Callbacks that formats the text content based on the company:
@app.callback(
    Output(component_id="company-header", component_property="children"),
    Input(component_id="company-input", component_property="value"))
def format_header_descriptions(company):
    return f"Arms Sales Data for {company}"

@app.callback(
    Output("company-info-desc", "children"),
    Input("company-input", "value"))
def format_main_desc(company):
    return f"This is the large description for the company Div Tag for {company}"

# Callbacks the format the main subplot graph:
@app.callback(
    Output("company-subplot", "figure"), 
    Input("company-input", "value"),
    Input("date-range-slider", "value")
    )
def return_subplot_from_company(company, date_range):
    """
    """
    # Building the dataframe from the .xlsx file:
    dataset = build_company_timeseries(
            workbook="application_frontend/static/application_frontend/data/SIPRI-Top-100-2002-2020.xlsx",
            company=company,
            years=date_range
    )
    
    end_date_placeholder_text="YYYY"
    # Using the dataset to create the subplots:
    company_subplots = build_company_timeseries_subplot_fig(dataset)

    return company_subplots