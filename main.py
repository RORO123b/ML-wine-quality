import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('winequalityN.csv')

print("============== VALORI LIPSA ================")
print(df.isnull().sum(), "\n")
print((df.isnull().mean() * 100).round(2).astype(str) + '%', "\n")

print("============== Statistici descriptive ================")
print(df.describe(), "\n")

# Histograma
df.hist(bins=10, figsize=(10, 10))
plt.show()

# Countplot
plt.figure(figsize=(10, 6))
sns.countplot(x='quality', data=df, palette='coolwarm', hue='quality')

plt.show()