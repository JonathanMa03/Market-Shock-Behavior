import yfinance as yf
import pandas as pd
import os

# Define the list of tickers, indented by sector
tickers = [
    "AAPL", "MSFT", "GOOGL",  # Technology
    "AMZN", "MCD",            # Consumer Discretionary
    "JNJ", "PFE",             # Healthcare
    "JPM", "BAC",             # Financials
    "GE", "MMM",              # Industrials
    "NEE", "DUK",             # Utilities
    "XOM", "CVX",             # Energy
    "PG", "KO",               # Consumer Staples
    "META", "CMCSA",          # Communication Services
    "AMT", "PLD"              # Real Estate
]

# Set the date range
start_date = "2007-01-01"
end_date = "2023-12-31"

# Fetch the data
data = yf.download(tickers, start=start_date, end=end_date, interval="1d", group_by="ticker")

# Check if data was retrieved successfully
if data.empty:
    print("No data retrieved. Please check tickers and date range.")
else:
    print("Data retrieved successfully.")
    data = data.stack(level=0).reset_index(level=1)
    data.rename(columns={'level_1': 'Ticker'}, inplace=True)
    data = data.reset_index()
    data.columns.name = None