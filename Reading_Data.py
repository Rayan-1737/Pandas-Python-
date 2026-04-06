import pandas as pd 

a = pd.read_csv("CryptocurrencyData.csv")

print(a.columns)

print(a["Coin Name"])
