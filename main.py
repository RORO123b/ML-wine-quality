import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.calibration import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import joblib

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

def antrenarea_modelului(df, quality_original):
    # Prelucrarea datelor
    X = df.drop('quality', axis=1)
    y = df['quality']

    # Impartirea setului de date in seturi de antrenare si testare
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

    # Antrenarea modelului --> DONE
    ### model = RandomForestRegressor(n_estimators=250, random_state=42)
    ### model.fit(X_train, y_train)

    model = joblib.load("model_forest.pkl")

    # Predictia
    y_pred = model.predict(X_test)

    # Evaluarea modelului
    print("============== Evaluarea modelului de regresie ================")
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"RMSE: {rmse}")

    # Exportarea seturilor de date de antrenare si testare
    train_set = pd.concat([X_train, y_train], axis=1)
    test_set = pd.concat([X_test, y_test], axis=1)
    train_set.to_csv('train_set.csv', index=False)
    test_set.to_csv('test_set.csv', index=False)

    # Salvarea modelului --> DONE
    ### joblib.dump(model, "model_forest.pkl")

    y_test_original = quality_original.loc[y_test.index]
    y_pred_original = y_pred * (quality_original.max() - quality_original.min()) + quality_original.min()
    errors = y_test_original - y_pred_original

    # Histograma erorilor
    plt.figure(figsize=(12, 10))
    df_errors = pd.DataFrame({
        'error': errors,
        'quality': y_test_original
    })
    sns.histplot(data=df_errors, x='error', bins=30, hue='quality', palette='coolwarm')
    plt.title('Histograma erorilor (calitate reala - prezisa)')
    plt.xlabel('Eroare')
    plt.ylabel('Frecventa')
    plt.show()

df = pd.read_csv('winequalityN.csv')

quality_original = df['quality'].copy()

analiza_datelor(df)

for col in ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'pH', 'sulphates']:
    df[col] = df[col].fillna(df[col].mean())

encoder = LabelEncoder()
df['type'] = encoder.fit_transform(df['type'])
scaler = MinMaxScaler()
df[df.columns] = scaler.fit_transform(df[df.columns])

antrenarea_modelului(df, quality_original)
