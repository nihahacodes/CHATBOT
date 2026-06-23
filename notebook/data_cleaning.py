import pandas as pd

#load the dataset 

financial=pd.read_csv("raw_data/financial.csv")

#rename the first coloumn 

financial.rename(columns={"Unnamed: 0":"Metric"},inplace=True)

#drop 2019 column since too many missing values 

financial.drop(columns=["2019-12-31"],inplace=True)

#save the cleaned file 

financial.to_csv("cleaned_data/financial_cleaned.csv",index=False)




balance=pd.read_csv("raw_data/balancesheet.csv")

balance.rename(columns={"Unnamed: 0":"Metric"},inplace=True)

balance.drop(columns=["2019-12-31"],inplace=True)

balance.to_csv("cleaned_data/balancesheet_cleaned.csv",index=False)

cashflow = pd.read_csv("raw_data/cashflow.csv")

cashflow.rename(columns={"Unnamed: 0": "Metric"}, inplace=True)

cashflow.drop(columns=["2019-12-31"], inplace=True)

cashflow.to_csv("cleaned_data/cashflow_cleaned.csv", index=False)
