import pandas as pd
import numpy as np
import holoviews as hv
import hvplot.pandas  
import panel as pn
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from datetime import datetime
import pytz
hv.extension('bokeh')
pn.extension()

# Load the data and define sector maps
data = pd.read_csv("../cleaned_data.csv")
data['Date'] = pd.to_datetime(data['Date'])
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

# Calculate daily returns
data['Return'] = data.groupby('Ticker')['Adj Close'].pct_change()

# Define available event dates
event_dates = {
    "Lehman Brothers Bankruptcy": datetime(2008, 9, 15, tzinfo=pytz.UTC),
    "American Recovery and Reinvestment Act": datetime(2009, 2, 17, tzinfo=pytz.UTC),
    "Stock Market Bottoms": datetime(2009, 3, 9, tzinfo=pytz.UTC),
    "U.S. Credit Downgrade": datetime(2011, 8, 5, tzinfo=pytz.UTC),
    "Brexit Referendum": datetime(2016, 6, 23, tzinfo=pytz.UTC),
    "Tax Cuts and Jobs Act Signed": datetime(2017, 12, 22, tzinfo=pytz.UTC),
    "COVID-19 Declared a Pandemic": datetime(2020, 3, 11, tzinfo=pytz.UTC),
    "CARES Act Passed": datetime(2020, 3, 27, tzinfo=pytz.UTC),
    "Highest Inflation Reported": datetime(2021, 11, 10, tzinfo=pytz.UTC),
    "Silicon Valley Bank Collapse": datetime(2023, 3, 10, tzinfo=pytz.UTC)
}


# Function to plot return KDEs before and after an event for a selected sector using Holoviews
def plot_return_kde(sector, event_dates):
    before_event = data[(data['Date'] < event_dates) & (data['Sector'] == sector)]['Return'].dropna()
    after_event = data[(data['Date'] >= event_dates) & (data['Sector'] == sector)]['Return'].dropna()
    
    before_kde = before_event.hvplot.kde(
        alpha=0.6, color='blue', 
        label=f"Before Event ({event_dates.strftime('%Y-%m-%d')})"
    )
    
    after_kde = after_event.hvplot.kde(
        alpha=0.6, color='orange', 
        label=f"After Event ({event_dates.strftime('%Y-%m-%d')})"
    )
    
    return (before_kde * after_kde).opts(
        title=f"{sector} - Returns Before and After Event",
        xlabel="Return", ylabel="Density", width=500, height=400,
        legend_position='right',  # Move legend to the right of the plot
        legend_opts={'label_text_font_size': '8pt'},  # Make legend text smaller
    )

# Panel widgets for interactivity
sector_dropdown = pn.widgets.Select(name="Select Sector", options=list(data['Sector'].unique()))
event_date_dropdown = pn.widgets.Select(name="Select Event Date", options=list(event_dates.keys()))

# Update function for Panel
@pn.depends(sector=sector_dropdown, event=event_date_dropdown)
def update_kde(sector, event):
    event_date = event_dates[event]
    kde_plot = plot_return_kde(sector, event_date)
    return kde_plot

# K-means Clustering Function
def kmeans_clustering():
    summary = data.groupby('Ticker').agg(
        avg_return=('Return', 'mean'),
        volatility=('Return', 'std')
    ).dropna()
    
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(summary)
    
    kmeans = KMeans(n_clusters=3, random_state=42)
    summary['Cluster'] = kmeans.fit_predict(scaled_features)
    
    cluster_plot = summary.hvplot.scatter(
        x='avg_return', y='volatility', by='Cluster', 
        title="K-means Clustering of Stocks",
        xlabel="Average Return", ylabel="Volatility", 
        size=100, hover_cols=['Cluster'], legend='top_right', width=500, height=400
    )
    
    return cluster_plot

# Correlation Analysis Function
@pn.depends(event=event_date_dropdown)
def correlation_analysis(event):
    event_date = event_dates[event]

    # Average Returns and Matrices
    before_event = data[data['Date'] < event_date].groupby(['Date', 'Sector'])['Return'].mean().unstack()
    after_event = data[data['Date'] >= event_date].groupby(['Date', 'Sector'])['Return'].mean().unstack()
    corr_before = before_event.corr()
    corr_after = after_event.corr()

    # Correlation heatmaps
    before_heatmap = hv.HeatMap((corr_before.index, corr_before.columns, corr_before.values)).opts(
        colorbar=True, cmap='coolwarm', title="Sector Correlation Before Event", width=500, height=400
    )
    after_heatmap = hv.HeatMap((corr_after.index, corr_after.columns, corr_after.values)).opts(
        colorbar=True, cmap='coolwarm', title="Sector Correlation After Event", width=500, height=400
    )
    
    return pn.Row(before_heatmap, after_heatmap)

# Layout
analysis_dashboard = pn.Column(
    pn.pane.Markdown("## In Depth Dive"),
    pn.pane.Markdown("### Interactive KDE of Returns Before and After Events"),
    sector_dropdown,
    event_date_dropdown,
    update_kde,
    pn.pane.Markdown("### Clustering of Stocks Based on Average Return and Volatility"),
    kmeans_clustering(),
    pn.pane.Markdown("### Sector Interdependencies Pre- and Post-Event"),
    correlation_analysis
)

