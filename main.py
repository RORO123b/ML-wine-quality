import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.calibration import LabelEncoder
from sklearn.discriminant_analysis import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score

def analiza_datelor(df):
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

def antrenarea_modelului(df):
    # Prelucrarea datelor
    X = df.drop('quality', axis=1)
    y = df['quality']

    # Impartirea setului de date in seturi de antrenare si testare
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Antrenarea modelului
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predictia
    y_pred = model.predict(X_test)

    # Evaluarea modelului
    print("============== Raport de clasificare ================")
    print(classification_report(y_test, y_pred))

    print("============== Acuratetea modelului ================")
    print("Acuratetea: ", accuracy_score(y_test, y_pred))

df = pd.read_csv('winequalityN.csv')
df['fixed acidity'] = df['fixed acidity'].fillna(df['fixed acidity'].mean())
df['volatile acidity'] = df['volatile acidity'].fillna(df['volatile acidity'].mean())
df['citric acid'] = df['citric acid'].fillna(df['citric acid'].mean())
df['residual sugar'] = df['residual sugar'].fillna(df['residual sugar'].mean())
df['chlorides'] = df['chlorides'].fillna(df['chlorides'].mean())
df['pH'] = df['pH'].fillna(df['pH'].mean())
df['sulphates'] = df['sulphates'].fillna(df['sulphates'].mean())

encoder = LabelEncoder()
df['type'] = encoder.fit_transform(df['type'])
scaler = MinMaxScaler()
df[df.columns] = scaler.fit_transform(df[df.columns])
scaler = StandardScaler()
df[df.columns] = scaler.fit_transform(df[df.columns])
print(df.head())

# antrenarea_modelului(df)