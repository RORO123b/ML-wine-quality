import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

df = pd.read_csv('winequalityN.csv')

print("============== VALORI LIPSA ================")
print(df.isnull().sum(), "\n")
print((df.isnull().mean() * 100).round(2).astype(str) + '%', "\n")

print("============== Statistici descriptive ================")
print(df.describe(), "\n")

# Histograma
df.hist(bins=10, figsize=(12, 10))
plt.suptitle('Histograma caracteristicilor vinului')
plt.tight_layout()
plt.show()

# Countplot
plt.figure(figsize=(12, 10))
sns.countplot(x='quality', data=df, palette='coolwarm', hue='quality')
plt.title('Numarul de vinuri in functie de calitate')
plt.xlabel('Calitate')
plt.ylabel('Numar de vinuri')
plt.legend(title='Calitate')
plt.show()

# Boxplot
plt.figure(figsize=(12, 10))
sns.scatterplot(x='quality', y='alcohol', data=df, palette='coolwarm', hue='quality')
plt.title('Boxplot al continutului de alcool in functie de calitate')
plt.xlabel('Calitate')
plt.ylabel('Alcool')
plt.show()
