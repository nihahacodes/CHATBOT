import pandas as pd 

#load the cleaned data 
df=pd.read_csv("cleaned_data/financial_cleaned.csv")

df_long=pd.melt(
    df,
    id_vars=["Metric"],
    var_name="Year",
    value_name="Value"

)
print(df_long.head())

df_long.to_csv(
    "cleaned_data/financial_long.csv"
    ,index=False
)
balance_df=pd.read_csv("cleaned_data/balancesheet_cleaned.csv")
balance_long = pd.melt(
    balance_df,
    id_vars=["Metric"],
    var_name="Year",
    value_name="Value"
)
balance_long.to_csv(
    "cleaned_data/balance_long.csv"
    ,index=False
)

cashflow_df=pd.read_csv("cleaned_data/cashflow_cleaned.csv")
cashflow_long = pd.melt(
    balance_df,
    id_vars=["Metric"],
    var_name="Year",
    value_name="Value"
)

cashflow_long.to_csv(
    "cleaned_data/cashflow_long.csv"
    ,index=False
)