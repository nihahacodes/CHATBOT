import pandas as pd

df = pd.read_csv("raw_data/cashflow.csv")

print(df.head())
print(df.columns)

print(df.info())

print(df.isnull().sum())

print(df.describe())