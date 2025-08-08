import pandas as pd
import numpy as np

# Load the data from data_download.csv
data = pd.read_csv("data_download.csv")

# Missing Values
data = data.dropna()  

# Outliers
def remove_outliers(df, columns):
    z_scores = np.abs((df[columns] - df[columns].mean()) / df[columns].std())
    return df[(z_scores < 3).all(axis=1)]

numerical_columns = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
data = remove_outliers(data, numerical_columns)

# Normalization
for column in ["Open", "High", "Low", "Close", "Adj Close"]:
    if column in data.columns:
        data[column] = data[column] / data[column].iloc[0]  

data.to_csv("cleaned_data.csv", index=False)