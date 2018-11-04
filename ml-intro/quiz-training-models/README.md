## Treinando modelos no scikit learn
Esta seção utiliza o mesmo conjunto de dados das seções anteriores.

Parte dos algoritmos de classificação mais importantes em Machine Learning:

- Regressão logística
- Redes neurais
- Árvores de decisão
- Máquinas de vetores de suporte (SVM)

### Regressão logística
```python
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
```

### Redes neurais _(note: Apenas disponível na versão 0.18 ou superior do scikit-learn)_
```python
from sklearn.neural_network import MLPClassifier
classifier = MLPClassifier()
```

### Árvores de decisão
```python
from sklearn.ensemble import GradientBoostingClassifier
classifier = GradientBoostingClassifier()
```

### SVM
```python
from sklearn.svm import SVC
classifier = SVC()
```

O objetivo foi utilizar um dos classificadores acima - regressão logística, árvores de decisão ou SVM (não contempla redes neurais por enquanto), para ver qual se encaixa melhor nos dados.