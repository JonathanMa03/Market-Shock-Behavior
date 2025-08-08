import pandas as pd
import holoviews as hv
import hvplot.pandas  
import panel as pn
hv.extension('bokeh')

# Load the data
data = pd.read_csv("../cleaned_data.csv")

# making datetime consistent
data['Date'] = pd.to_datetime(data['Date'])

# Sector dictionary
sector_mapping = {
    "AAPL": "Technology", "MSFT": "Technology", "GOOGL": "Technology",
    "AMZN": "Consumer Discretionary", "MCD": "Consumer Discretionary",
    "JNJ": "Healthcare", "PFE": "Healthcare",
    "JPM": "Financials", "BAC": "Financials",
    "GE": "Industrials", "MMM": "Industrials",
    "NEE": "Utilities", "DUK": "Utilities",
    "XOM": "Energy", "CVX": "Energy",
    "PG": "Consumer Staples", "KO": "Consumer Staples",
    "META": "Communication Services", "CMCSA": "Communication Services",
    "AMT": "Real Estate", "PLD": "Real Estate"
}
data['Sector'] = data['Ticker'].map(sector_mapping)

# Individual Performance
def plot_individual_stock_performance(sector):
    sector_data = data[data['Sector'] == sector]
    if sector_data.empty:
        return hv.Text(0.5, 0.5, "No data available for this sector", halign="center", valign="center")
    
    plot = sector_data.hvplot.line(
        x='Date', y='Adj Close', by='Ticker',
        title=f"Individual Stock Performance in {sector}",
        xlabel="Date", ylabel="Adjusted Close Price",
        width=600, height=400
    )
    return plot

# Aggregate Performance
def plot_sector_aggregate_performance(selected_sectors):
    sector_agg = data.groupby(['Date', 'Sector'])['Adj Close'].mean().reset_index()
    sector_agg = sector_agg[sector_agg['Sector'].isin(selected_sectors)]
    if sector_agg.empty:
        return hv.Text(0.5, 0.5, "No data available for selected sectors", halign="center", valign="center")
    
    plot = sector_agg.hvplot.line(
        x='Date', y='Adj Close', by='Sector',
        title="Aggregate Sector Performance (Average Adjusted Close Price)",
        xlabel="Date", ylabel="Average Adjusted Close Price",
        width=600, height=400
    )
    return plot

# Panel layout
sector_dropdown = pn.widgets.Select(name="Select Sector", options=data['Sector'].unique().tolist())
sector_multi_select = pn.widgets.MultiSelect(name="Select Sectors for Aggregate Plot", options=data['Sector'].unique().tolist(), size=6)

individual_stock_plot = pn.bind(lambda sector: hv.DynamicMap(lambda: plot_individual_stock_performance(sector)), sector=sector_dropdown)
aggregate_sector_plot = pn.bind(lambda selected_sectors: hv.DynamicMap(lambda: plot_sector_aggregate_performance(selected_sectors)), selected_sectors=sector_multi_select)

# Arrange the layout
eda_dashboard = pn.Row(
    pn.Column(
        pn.pane.Markdown("## Exploring the Data"),
        pn.pane.Markdown("### Select a sector to view individual stock performance"),
        sector_dropdown,
        individual_stock_plot
    ),
    pn.Column(
        pn.pane.Markdown("### Select sectors to view aggregate performance"),
        sector_multi_select,
        aggregate_sector_plot
    )
)
