# Importing data ingestion/manipulation methods:
import pandas as pd
from openpyxl import load_workbook
from datetime import date

# Importing PLotly and Dash visuzalization methods: 
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

# Function that creates a formatted dataframe from the .xlsx file:
def build_company_timeseries(workbook:str, company:str, years:list=[2002, 2020]):

    # Function that is used to extract information from the worksheet:
    def extract_company_data_from_sheet(sheet, company:str):
        # Extracting all companies in the list and determining the position of the company in the sheet:
        companies =  [cell[0].value for cell in sheet["C5:C120"]]

        if company in companies:
            company_location = companies.index(company) + 5 # Adding 4 to auto-navigate to table position

        else:
            return [None, None, None, None, None, None, None]

        # Extracting relevant company data from the row as a list:
        company_data = [row.value for row in sheet[f"A{company_location}:I{company_location}"][0]]

        # Removing irrelevant rows:
        irrelevant_rows = [1, 5]
        for i in sorted(irrelevant_rows, reverse=True):
            company_data.pop(i)

        return company_data

    # Main dict to be populated:
    timeseries_dict = {}

    # Loading workbook:
    workbook = load_workbook(workbook, read_only=True)
    #print(years)
    # Extracting the list of years:
    years = list(range(years[0],years[1]+1))
    years = [str(year) for year in years][::-1]
    #print(years)
    # Iterating through each sheet extracting company row data:
    for year in years:
        timeseries_dict[year] = extract_company_data_from_sheet(workbook[year], company)

    # Building the dataframe from dict:
    headers = ["Rank", "Company", "Country", "Arms Sales", "Total Sales", "Arms sales as % of total sales", "Arms sales adjusted price"]
    df = pd.DataFrame.from_dict(timeseries_dict, orient="index", columns=headers)
    df.dropna(inplace=True)
    df = df.iloc[::-1]
    return df

# Function that creates the subplot for Arms Sales Company Dashboards:
def build_company_timeseries_subplot_fig(dataframe):
    """"""
    titles_units = {
    "Rank": "Position",
    "Arms Sales": "Millions $USD",
    "Total Sales": "Millions $USD",
    "Arms sales as % of total sales": "%",
    "Arms sales adjusted price": "Millions $USD"
    }

    # Plotting the timeseries from the dataframe:
    fig = make_subplots(
        rows=3,
        cols=2,
        specs=[[{}, {}],[{}, {}], [{"colspan" : 2}, None]],
        subplot_titles=("Rank", "Arms Sales", "Total Sales", "Arms sales as % of total sales", "Arms sales adjusted price")
    )
    row=1


    # Creating all scatterplots:
    fig.add_trace(
        go.Scatter(
        x=dataframe.index,
        y=dataframe["Rank"],
        name="Position",
        hovertemplate="%{y}"
        ),
        col=1, row=1)

    fig.add_trace(
        go.Scatter(
        x=dataframe.index,
        y=dataframe["Arms Sales"],
        name="Millions $USD",
        hovertemplate="%{y}",
        fill="tozeroy"

        ),
        col=2, row=1)

    fig.add_trace(
        go.Scatter(
        x=dataframe.index,
        y=dataframe["Total Sales"],
        name="Millions $USD",
        hovertemplate="%{y}",
        fill="tozeroy"

        ),
        col=1, row=2)

    fig.add_trace(
        go.Scatter(
        x=dataframe.index,
        y=dataframe["Arms sales as % of total sales"],
        name="%",
        hovertemplate="%{y}",
        fill="tozeroy"

        ),
        col=2, row=2)

    fig.add_trace(
        go.Scatter(
        x=dataframe.index,
        y=dataframe["Arms sales adjusted price"],
        name="Millions $USD",
        hovertemplate="%{y}",
        fill="tozeroy"
        ),
        col=1, row=3)



    # Styling the figure correctly:
    fig.update_layout(height=900)


    return fig
