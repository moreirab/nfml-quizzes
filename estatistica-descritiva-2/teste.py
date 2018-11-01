# Primeiro, será necessário encontrar a média. 
# Depois, a diferença entre cada anotação e a média. 
# Então elevar estes valores ao quadrado, somar e dividir pelo número de amostras.

import math

arr = [1, 5, 10, 3, 8, 12, 4]
mean = sum(arr)/len(arr)
variances = []

for value in arr:
    variances.append((value - mean)**2)

variance = sum(variances)/len(arr)
std = math.sqrt(variance)

print('Variance: {}; Standard Deviation: {}'.format(variance, std))

