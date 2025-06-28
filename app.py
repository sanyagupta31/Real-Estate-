# app.py
import dash
from dash import html, dcc, Input, Output, State
import pandas as pd
import joblib

# Load model
model = joblib.load('real_estate_model.pkl')

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Real Estate Price Prediction", style={'text-align': 'center','font-famiy':'cursive'}),
    html.Div([
        dcc.Input(id='distance_to_mrt', type='number', placeholder='Distance to MRT Station (meters)',
                  style={'margin': '10px', 'padding': '10px'}),
        dcc.Input(id='num_convenience_stores', type='number', placeholder='Number of Convenience Stores',
                  style={'margin': '10px', 'padding': '10px'}),
        dcc.Input(id='latitude', type='number', placeholder='Latitude',
                  style={'margin': '10px', 'padding': '10px'}),
        dcc.Input(id='longitude', type='number', placeholder='Longitude',
                  style={'margin': '10px', 'padding': '10px'}),
        html.Button('Predict Price', id='predict_button', n_clicks=0,
                    style={'margin': '10px', 'padding': '10px', 'background-color': '#007BFF', 'color': 'white'}),
    ], style={'text-align': 'center','backgroundColor': "#84b2e0"}),

    html.Div(
    id='prediction_output',
    style={
        'textAlign': 'center',
        'fontSize': '24px',
        'fontWeight': 'bold',
        'marginTop': '30px',
        'color': 'white',
        'backgroundColor': '#007BFF',
        'padding': '20px',
        'borderRadius': '10px',
        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)'
    }
)

])

@app.callback(
    Output('prediction_output', 'children'),
    Input('predict_button', 'n_clicks'),
    State('distance_to_mrt', 'value'),
    State('num_convenience_stores', 'value'),
    State('latitude', 'value'),
    State('longitude', 'value')
)
def update_output(n_clicks, distance_to_mrt, num_convenience_stores, latitude, longitude):
    if n_clicks > 0 and None not in [distance_to_mrt, num_convenience_stores, latitude, longitude]:
        features = pd.DataFrame([[distance_to_mrt, num_convenience_stores, latitude, longitude]],
                                columns=['Distance to the nearest MRT station', 'Number of convenience stores', 'Latitude', 'Longitude'])
        prediction = model.predict(features)[0]
        return f'Predicted House Price of Unit Area: {prediction:.2f}'
    elif n_clicks > 0:
        return 'Please enter all values to get a prediction'
    return ''

if __name__ == '__main__':
    app.run(debug=True)
