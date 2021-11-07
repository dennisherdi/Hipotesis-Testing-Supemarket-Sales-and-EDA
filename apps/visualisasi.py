import datetime

from pandas._config.config import options
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc
from app import app

external_stylesheets = [dbc.themes.LUX]
 

df = pd.read_csv('supermarket_sales.csv')
df = df.rename(
       columns = {
            "Product line" : "Product_line",
            "Customer type" : "Customer_type"
        })

layout = html.Div(children=[
     html.Div(
        children=[
            html.H1(children= "Grafik Persebaran Pada Supermarket Sales ", className="header-emoji"),
            html.H1(
                children ="",
                className="header-description",
            ),
        ],
        className="header",
    ),
    html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(children="Product_line", className = "menu-title"),
                    dcc.Dropdown(
                        id="region-filter",
                        options =[
                        {"label" : Product_line, "value" : Product_line}
                        for Product_line in np.sort(df.Product_line.unique())
                        ],
                        value = 'Fashion accessories',
                    ),
                ]
        ),
            html.Div(
                children=[
                    html.Div(children="Type", className = "menu-title"),
                    dcc.Dropdown(
                        id="type-filter",
                        options =[
                            {"label" : Gender, "value" : Gender}
                            for Gender in df.Gender.unique()
                        ],
                        value = 'Female',
                    ),
                ]
            ),

        ],
        className="menu",
    ),
    html.Div(
        children=[
            html.Div(
                children = dcc.Graph(
                    id = "price-chart"
                    ),

                className = "card",
            ),
            html.Div(
                children = dcc.Graph(
                    id = "total-chart"
                    ),

                className = "card",
            ),
            html.Div(
                children = dcc.Graph(
                    id = "tax-chart"
                    ),

                className = "card",
            ),
            html.Div(
                children = dcc.Graph(
                    id = "grass-chart"
                    
                    ),

                className = "card",
            ),     
        ],
        className= "wrapper"
    ),
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Grafik Lingkaran Pada Supermarket Sales"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='Memvisualisasikan grafik Pie Chart'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='Gender',
                    options=[
                       {"label" : Gender, "value" : Gender} for Gender in df.Gender.unique()
                       
                    ],
                    value='Female',
            
                ),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='the_graph'
                )
            )
        ])
    ])
])

           

@app.callback(
    [
     Output("price-chart", "figure"),
     Output("total-chart", "figure"), 
     Output("tax-chart", "figure"), 
     Output("grass-chart", "figure")  
    ],
    [
     Input("region-filter", "value"),
     Input("type-filter", "value")
    ],
)    
def update_charts(Product_line, Gender):
    filtered_df = df[(df.Product_line.isin([Product_line])) &
                     (df.Gender.isin([Gender]))]

    fig = px.scatter(filtered_df, x = "Total", y = "Unit price",
           size="Quantity", color="Payment", hover_name="City",
           log_x=True, size_max=55, title='Unit Price')

    fig2 = px.scatter(filtered_df, x = "Total", y = "Tax 5%",
           size="Quantity", color="Payment", hover_name="City",
           log_x=True, size_max=55, title='Tax 5%')


    fig3 = px.scatter(filtered_df, x = "Total", y = "gross income",
                     size="Quantity", color="Payment", hover_name="City",
                     log_x=True, size_max=55, title='Gross Income')


    fig4 = px.scatter(filtered_df, x = "Total", y = "Rating",
                     size="Quantity", color="Payment", hover_name="City",
                     log_x=True, size_max=55, title='Rating')
    
 
    return fig, fig2, fig3, fig4

@app.callback(
    Output('the_graph', 'figure'),
    Input('Gender', 'value')
)
def update_graph(Gender):
   d3 = df.groupby(['Product_line', 'Gender'])[['Total']].sum().reset_index()
   d4 = d3[d3['Gender'] == Gender]
   piechart = px.pie(d4, names = 'Product_line', values = 'Total', height=600, title=f'Total dari Product Line Dan Gender')

   return piechart    