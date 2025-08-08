# Market Behavior Analysis through EDA and Clustering

## Overview
This project provides a **foundational understanding of stock market behavior** using core market data such as daily prices, trading volume, and returns.  
We source historical stock data from **Yahoo Finance**, perform **exploratory data analysis (EDA)**, and apply **clustering techniques** to group stocks based on performance metrics like average returns and volatility.

The aim is to uncover:
- How different stocks and sectors respond to market events
- Relationships and dependencies not visible in single-stock analysis
- Sector-based trends and correlations
- Patterns associated with volatility or sector-specific risks

The project emphasizes **simplicity and interpretability**—making it a practical analytical tool without relying on complex derivatives or advanced metrics like implied volatility or Greeks.

---

## Introduction
The focus of this project is to analyze stock market behavior using **basic historical stock data**, including daily prices, trading volume, and returns, sourced from Yahoo Finance.  
This data allows us to explore fundamental patterns in stock performance across various sectors, such as technology, finance, and healthcare.  

We apply:
- **EDA** to understand data distributions and detect outliers.
- **Clustering** to identify groups of stocks with similar behaviors.
- **Correlation Analysis** to explore interdependencies between sectors, especially during major market events.

---

## Motivation
In an interconnected global economy, sectors are influenced by common economic forces, investor sentiment, and market events. Understanding these relationships:
- Helps investors diversify portfolios and manage risk.
- Supports analysts in identifying sector sensitivities.
- Assists policymakers in anticipating systemic risks.

By directly analyzing raw stock data, this project offers a **transparent, replicable** methodology for understanding market sentiment and sector relationships.

---

## Methods

### 1. Exploratory Data Analysis (EDA) — *Line Charts*
Visualize sector performance over time to identify:
- Trends
- Seasonal patterns
- Volatility spikes
- Reactions to events

### 2. Before & After Density Plots
Compare return distributions **pre- and post-event** to assess:
- Volatility changes
- Shifts in average returns
- Sector stability

### 3. Clustering
Use **unsupervised ML** (K-Means) to group stocks by:
- Average returns
- Volatility  
This reveals natural co-movement patterns and diversification opportunities.

### 4. Correlation Heatmaps
Display relationships between sector returns with:
- Positive correlations (move together)
- Negative/low correlations (independent)  
We also compare relationships **before vs. after** key market events.

---

## 📂 Project Structure
```
├── data/               # Raw & processed datasets
├── notebooks/          # Jupyter notebooks for EDA & modeling
├── src/                # Python scripts for data processing & analysis
├── results/            # Visualizations, cluster summaries, outputs
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 📦 Dependencies
- **Core Libraries**: `numpy`, `pandas`, `datetime`, `os`, `pytz`
- **Data Acquisition**: `yfinance`
- **Visualization**: `matplotlib`, `seaborn`, `holoviews`, `hvplot.pandas`, `panel`
- **Machine Learning**: `scikit-learn` (`sklearn.cluster`, `sklearn.preprocessing`)

## ✅ Conclusions
This project has provided a comprehensive analysis of stock market behavior using basic historical stock data, focusing on **sector relationships, stock volatility, and patterns of market sentiment**.

Key takeaways:
- **Time Series Analysis** revealed sector-specific trends and volatility patterns not always captured in general market commentary.  
- **Before/After Return Distributions** demonstrated how sentiment and stability shift following specific events.  
- **Clustering Analysis** grouped stocks with similar return-volatility profiles, highlighting co-movement patterns within and across sectors.  
- **Correlation Heatmaps** visualized inter-sector relationships, enabling the identification of diversification opportunities and risk clusters.

Through EDA, clustering, and correlation analysis, this project delivers **data-driven insights** that can guide investment decisions, risk management strategies, and deeper market research.

---

## 📜 License
This project is licensed under the MIT License. See `LICENSE` for details.
