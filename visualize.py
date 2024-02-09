import zero_true as zt
import pandas as pd
import plotly.graph_objects as go
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("Ammok/apple_stock_price_from_1980-2021", split='train')
# Convert the dataset to a pandas dataframe
df = pd.DataFrame(dataset)

# Ensure 'Date' is a datetime type
df['Date'] = pd.to_datetime(df['Date'])

def create_stock_price_plot(df):
    # Filter or process the dataframe as needed. Here, we directly use it for plotting.
    fig = go.Figure(go.Scatter(x=df['Date'], y=df['Close'], mode='lines', name='Close'))
    fig.update_layout(title="Apple Stock Price from 1980 to 2021", xaxis_title="Year", yaxis_title="Stock Price (USD)", template="plotly_dark")
    return fig

# Assuming you want to plot all the data:
fig = create_stock_price_plot(df)

# Save the figure as a PNG file
fig.write_image("apple_stock_price.png")
