import joblib
import gradio as gr
import pandas as pd
import numpy as np

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
    
    input_dict = dict(zip(feature_names, inputs))
    
    for key in input_dict:
        if input_dict[key] is None:
            if key == 'type':
                input_dict[key] = 'red'
            else:
                input_dict[key] = df[key].mean()

    input_dict['type'] = 1 if input_dict['type'] == 'red' else 0
    input_data = pd.DataFrame([input_dict])

    prediction_result = model.predict(input_data)[0]
    prediction_result = np.clip(prediction_result, 3, 9)
    return f"Predicted wine quality: {round(prediction_result, 2)}"

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
