# Data Analysis

#### Histograms for each feature allow us to understand the distribution of values in the dataset. They help identify possible asymmetries, extreme values (outliers), or uneven distributions, which can affect the performance of machine learning models.  
#### For example, the alcohol feature has a relatively symmetric distribution, similar to a normal distribution. This suggests that the values are balanced and do not require additional transformations. In contrast, volatile acidity has a left-skewed distribution, indicating that most values are high, but there are a few examples with significantly lower values.

![Wine Feature Histograms](./Histograma%20caracteristicilor%20vinului.png)

#### An imbalance is observed in the label distribution: most wines have quality 5, 6, or 7, while extreme values (3, 4, 8, 9) are rare. This imbalance could negatively influence model performance, as the model may tend to favor the dominant classes.

![Wine Count by Quality](./Numarul%20de%20vinuri%20in%20functie%20de%20calitate.png)

#### The boxplot shows a positive correlation between wine quality and alcohol content: higher-quality wines tend to have higher alcohol levels. The distribution is more varied for mid-range qualities (5 and 6), while higher-quality wines show more concentrated values. This pattern suggests that alcohol is a relevant factor for predicting quality.

![Alcohol by Quality](./Alcool%20in%20functie%20de%20calitate.png)

#### This image shows how the various wine features are related to each other and, especially, their influence on quality. Red colors indicate a positive correlation (e.g., alcohol ↑ → quality ↑), while blue colors indicate a negative correlation (e.g., volatile acidity ↑ → quality ↓). The numbers show the strength of these relationships. In short, it helps us quickly see what is important for a good wine.

![Correlation Heatmap](./Matricea%20de%20corelatie.png)

#### This graph (violin plot) shows how volatile acidity (a wine feature) is distributed for each quality level (from 3 to 9). The “violin” shapes indicate data density: wider areas show where most wines are concentrated. A clear trend is observed: as wine quality increases, the level and variability of volatile acidity decrease significantly, suggesting that lower volatile acidity is associated with higher-quality wines.

![Violin Plot](./Volatile%20acidity%20in%20functie%20de%20calitate.png)
