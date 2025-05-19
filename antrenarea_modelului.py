import numpy as np
import pandas as pd
from sklearn.calibration import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

df = pd.read_csv('winequalityN.csv')

for col in ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'pH', 'sulphates']:
    df[col] = df[col].fillna(df[col].mean())

encoder = LabelEncoder()
df['type'] = encoder.fit_transform(df['type'])
scaler = MinMaxScaler()
df[df.columns] = scaler.fit_transform(df[df.columns])

# Prelucrarea datelor
X = df.drop('quality', axis=1)
y = df['quality']

# Impartirea setului de date in seturi de antrenare si testare
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

# Antrenarea modelului
model = RandomForestRegressor(n_estimators=250, random_state=42)
model.fit(X_train, y_train)


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
