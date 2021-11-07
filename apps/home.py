import dash_html_components as html
import dash_bootstrap_components as dbc
 
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Welcome to the Supermarket Sales dashboard",
                className="text-center"),
                className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(
                html.H5(children=['Hallo, Nama Saya Dennis Herdiawan!', html.Br(),
                'saya adalah murid di Hacktiv8 Data Science Bootcamp - Batch 004.', html.Br(), 
                'Dan ini adalah Project Milestone saya !']),
                className="mb-4")
        ]),
 
        dbc.Row([
            dbc.Col(
                html.H5(children=['Terdiri dari tiga halaman utama: ', html.Br(),
                '1. Visualisasi, yang memberikan visualisasi data penjualan supermarket, ', html.Br(),
                '2. Pengujian Hipotesis, yang memberi Anda pengujian hipotesis antar variabel', html.Br(),
                '3. Beranda, Anda mendapatkan dataset asli dan mengunjungi halaman Github saya dari sini,']),
                className="mb-5")
        ]),
 
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='kumpulan data asli di sini',
                        className="text-center"),
                        dbc.Button("Supermarket Sales",
                        href="https://www.kaggle.com/aungpyaeap/supermarket-sales",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),
 
            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Kunjungi Halaman Github saya',
                        className="text-center"),
                        dbc.Button("GitHub",
                        href="https://github.com/dennisherdi",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),
        ], className="mb-5"),
    ])
 
])