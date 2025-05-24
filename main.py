import joblib
import gradio as gr
import pandas as pd
import numpy as np
from sklearn.calibration import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

model = joblib.load("model_forest.pkl")
df = pd.read_csv('winequalityN.csv')

feature_names = ['type', 'fixed acidity', 'volatile acidity', 'citric acid',
                 'residual sugar', 'chlorides', 'free sulfur dioxide',
                 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']

for col in ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
            'chlorides', 'pH', 'sulphates']:
    df[col] = df[col].fillna(df[col].mean())

def prediction(type, fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
               chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,
               pH, sulphates, alcohol):
    
    inputs = [type, fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
              chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,
              pH, sulphates, alcohol]
    inputs = np.array(inputs).reshape(1, -1)
    inputs = pd.DataFrame(inputs, columns=feature_names)
    encoder = LabelEncoder()
    df['type'] = encoder.fit_transform(df['type'])
    inputs['type'] = encoder.fit_transform(inputs['type'])
    scaler = MinMaxScaler()
    scaler.fit(df[feature_names])
    inputs[inputs.columns] = scaler.transform(inputs[feature_names])
    prediction = model.predict(inputs)
    # Rescalez predictia la intervalul original al calitatii
    return f"Predicted quality: {round(prediction[0])}"

interfata = gr.Interface(
    fn=prediction,
    inputs = [
        gr.Dropdown(['red', 'white'], label="Type"),
        gr.Number(label="Fixed acidity"),
        gr.Number(label="Volatile acidity"),
        gr.Number(label="Citric acid"),
        gr.Number(label="Residual sugar"),
        gr.Number(label="Chlorides"),
        gr.Number(label="Free sulfur dioxide"),
        gr.Number(label="Total sulfur dioxide"),
        gr.Number(label="Density"),
        gr.Number(label="pH"),
        gr.Number(label="Sulphates"),
        gr.Number(label="Alcohol")
    ],
    outputs="text"
)

interfata.launch()
