import pandas as pd

df = pd.read_csv('winequalityN.csv')

print("============== VALORI LIPSA ================")
print(df.isnull().sum())
print("============== Statistici descriptive ================")
print(df.describe())