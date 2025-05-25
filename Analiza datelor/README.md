# Analiza datelor

#### Histogramele fiecarei caracteristici ne permit sa intelegem distributia valorilor din setul de date. Prin ele putem identifica eventuale asimetrii, valori extreme (outliers), sau distributii neuniforme, care pot afecta performanta modelelor de machine learning.
#### De exemplu caracteristica alcool are o distributie relativ simetrica, asemanatoare cu o distributie normala. Acest lucru sugereaza ca valorile sunt echilibrate si nu necesita transformari suplimentare. Insa, aciditate volatila are o distributie asimetrica spre stanga, ceea ce indica faptul ca majoritatea valorilor sunt ridicate, dar exista si cateva exemple cu valori semnificativ mai mici.

![Histograma vinului](./Histograma%20caracteristicilor%20vinului.png)

#### Se observa un dezechilibru in distributia etichetelor: cele mai multe vinuri au calitatea 5, 6 sau 7, in timp ce valorile extreme (3, 4, 8, 9) sunt rare. Acest dezechilibru ar putea influenta negativ performanta modelului, deoarece modelul va fi tentat sa favorizeze clasele dominante.

![Numar vinuri in functie de calitate](./Numarul%20de%20vinuri%20in%20functie%20de%20calitate.png)

#### Boxplot-ul arata o corelatie pozitiva intre calitatea vinului si continutul de alcool: vinurile de calitate mai mare tind sa aiba un nivel mai ridicat de alcool. Distributia este mai variata pentru calitatile medii (5 si 6), in timp ce vinurile de calitate superioara prezinta valori mai concentrate. Acest tipar sugereaza ca alcoolul este un factor relevant in estimarea calitatii.
![Alcool pe calitate](./Alcool%20in%20functie%20de%20calitate.png)