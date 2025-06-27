import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Load the LEGO dataset
lego_data = pd.read_csv("path_to_your/lego_sets.csv")

# Prepare the data for the dashboard
yearly_sets = lego_data.groupby('year').size().reset_index(name='num_sets')
average_price = lego_data.groupby('year')['US_retailPrice'].mean().reset_index()
theme_counts = lego_data['theme'].value_counts().reset_index()
theme_counts.columns = ['theme', 'num_sets']

# Initialize the dashboard
app = Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("LEGO Dataset Dashboard", style={'text-align': 'center'}),

    # Number of sets released per year
    dcc.Graph(
        figure=px.line(yearly_sets, x='year', y='num_sets', title='Number of LEGO Sets Released Per Year',
                       labels={'year': 'Year', 'num_sets': 'Number of Sets'})
    ),

    # Average price over time
    dcc.Graph(
        figure=px.line(average_price, x='year', y='US_retailPrice', title='Average Price of LEGO Sets Over Time',
                       labels={'year': 'Year', 'US_retailPrice': 'Average Price (USD)'})
    ),

    # Top 10 themes by the number of sets
    dcc.Graph(
        figure=px.bar(theme_counts.head(10), x='theme', y='num_sets', title='Top 10 LEGO Themes by Number of Sets',
                      labels={'theme': 'Theme', 'num_sets': 'Number of Sets'})
    ),

    # Distribution of pieces
    dcc.Graph(
        figure=px.histogram(lego_data, x='pieces', nbins=50, title='Distribution of Piece Counts',
                            labels={'pieces': 'Number of Pieces'})
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
