# ML pentru prezicerea calitatii vinului

Acest proiect de machine-learning are ca scop prezicerea calitatii unui vin prin intermediul unui Random Forest Regressor.

## Functii importante

- **[Random Forest Regressor](https://en.wikipedia.org/wiki/Random_forest)** -> folosit pentru antrenarea modelului
- **[Joblib](https://joblib.readthedocs.io/en/stable/)** -> folosit pentru salvarea modelului
- **[Gradio](https://www.gradio.app/)** -> folosit pentru crearea interfatei

## Preprocesarea datelor

Pentru a imbunatati acuratetea predictiilor, am aplicat un MinMaxScaler pentru a normaliza valorile caracteristicilor intre 0 si 1. <br>
Tipul vinului este encodat astfel: vinurile albe → 1, vinurile rosii → 0. Aceasta transformare ajuta modelul sa proceseze datele in mod eficient. <br>
In acest fel, prin intermediul Random Forest Regressor -ului se obtine ML cu ***[RMSE](https://en.wikipedia.org/wiki/Root_mean_square_deviation) = 0.56***

## Histograma erorilor

### Erorile prezise sunt in mare parte apropiate de 0, ceea ce sugereaza ca modelul are o performanta buna si poate fi utilizat pentru predictii fiabile.
![Histograma erorilor](./Histograma%20erorilor.png)

## Resurse externe

Pentru realizarea proiectului am folosit database-ul [acesta](https://media.geeksforgeeks.org/wp-content/uploads/20240910131455/winequalityN.csv) oferit de **[Geeks for geeks](https://www.geeksforgeeks.org/)**.

## Rularea proiectului
### 1. Cloneaza repository-ul
```bash
git clone https://github.com/RORO123b/ML-wine-quality.git
cd ML-wine-quality
```

### 2. Creeaza un mediu virtual (Optional, dar recomandat)
```bash
python -m venv venv
source venv/bin/activate      # pe Windows: venv\Scripts\activate
```

### 3. Instaleaza dependintele
```bash
pip install -r requirements.txt
```