import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

 
from app import app #change this line
 



layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1(children="CHI SQUARE TESTING"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='Uji Chi Square atau dikenal juga di Indonesia sebagai uji Kai Kuadrat, adalah salah satu cara yang digunakan untuk menyampaikan atau menunjukkan keberadaan hubungan (ada atau tidaknya) antara variabel yang diteliti. Misalkan kita sebagai peneliti hendak melakukan uji terhadap perilaku mahasiswa. Karakter yang akan diuji adalah perilaku mahasiswa yang dikategorikan menjadi dua kategori. Kategori tersebut adalah mahasiswa yang mendukung program kampus dan acuh terhadap program kampus. Kondisi tersebut memungkinkan kita untuk melakukan uji hipotesis mengenai perbedaan perilaku mahasiswa tersebut dilihat dari frekuensinya.'),
                className="mb-4"
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.H6(children='H0 = Di suatu populasi yang sama, dua kategorikal variabel tidak berhubungan'),
                    html.H6(children='H1 = Di suatu populasi yang sama, dua kategorikal variabel berhubungan')
                ],    
                    className="mb-4"
            ))
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Hubungan antara Product Line Dengan City'),
                ])
            )
        ]), 

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Observed chi2: 11.56'), 
                    html.P(children='P-value: 0.3156'),
                    html.P(children='dapat disimpulkan bahwa menerima h0, yaitu hubungan Product Line dengan city tidak berhubungan erat antar values'),
                ],
                className="mb-4"
                )
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Hubungan antara Product Line Dengan Customer Type'),
                ],
                className="mt-4")
            )
        ]),  

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Observed chi2: 3.33'), 
                    html.P(children='P-value: 0.6500'),
                    html.P(children='dapat disimpulkan bahwa menerima h0, yaitu hubungan Product Line dengan Customer Type tidak berhubungan erat antar values'),
                ],
                className="mb-4"
                )
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Hubungan antara Product Line Dengan Gender'),
                ],
                className="mt-4")
            )
        ]),  

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Observed chi2: 5.74'), 
                    html.P(children='P-value: 0.3319' ),
                    html.P(children='dapat disimpulkan bahwa menerima h0, yaitu hubungan Product Line dengan Gender tidak berhubungan erat antar values'),
                ],
                className="mb-4"
                )
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Hubungan antara Product Line Dengan Payment'),
                ],
                className="mt-4")
            )
        ]),  

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Observed chi2: 8.72' ), 
                    html.P(children='P-value: 0.5587'),
                    html.P(children='dapat disimpulkan bahwa menerima h0, yaitu hubungan Product Line dengan Payment tidak berhubungan erat antar values'),
                ],
                className="mb-4"
                )
            )
        ]),
        
        
        ])
    ])
 