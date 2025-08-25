# Robert Cristian Barbulescu 315CD - ML for Wine Quality Prediction

This machine learning project aims to predict wine quality using a **Random Forest Regressor**.

---

## Key Components

- **[Random Forest Regressor](https://en.wikipedia.org/wiki/Random_forest)** → used to train the model  
- **[Joblib](https://joblib.readthedocs.io/en/stable/)** → used to save the trained model  
- **[Gradio](https://www.gradio.app/)** → used to create an interactive interface  

---

## Data Preprocessing

To improve prediction accuracy, a **MinMaxScaler** was applied to normalize feature values between 0 and 1.  
Wine type is encoded as: white wines → 1, red wines → 0. This transformation allows the model to process the data efficiently.  

Using the Random Forest Regressor, the model achieves **[RMSE](https://en.wikipedia.org/wiki/Root_mean_square_deviation) = 0.56**, which corresponds to an accuracy of **91%** (average wine quality is 5.81; calculated as `100% - (0.56 / 5.81) * 100 ≈ 91%`).  

---

## Error Histogram

Predicted errors are mostly close to 0, indicating that the model performs well and can be used for reliable predictions.  

![Error Histogram](./Histograma%20erorilor.png)

---

## External Resources

The dataset used for this project is available [here](https://media.geeksforgeeks.org/wp-content/uploads/20240910131455/winequalityN.csv) from **[Geeks for Geeks](https://www.geeksforgeeks.org/)**.

---

## Running the Project

### 1. Clone the repository
```bash
git clone https://github.com/RORO123b/ML-wine-quality.git
cd ML-wine-quality
```

```bash
git clone https://github.com/RORO123b/ML-wine-quality.git
cd ML-wine-quality
```

### 2. Create a virtual environment (Optional but recommended)
```bash
python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```
