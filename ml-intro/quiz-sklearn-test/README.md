## Usar o comando train_test_split
Esta seção usa o conjunto de dados da seção anterior.

A função recebe como entradas X e y, retornando quatro coisas:
- X_train: a entrada de treinamento
- X_test: a entrada de teste
- y_train: os labels de treinamento
- y_test: os labels de teste

A chamada para a função é feita como apresentado a seguir:
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)
```
O último parâmetro, test_size, é a percentagem de pontos quero usar no teste. Na chamada acima, estou usando 25% dos pontos para teste e 75% para treinamento.