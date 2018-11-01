import math

def calc_variance(dataset):
    mean = sum(dataset)/len(dataset)
    variances = []
    for value in dataset:
        variances.append((value - mean)**2)
    variance = sum(variances)/len(dataset)
    return variance

def calc_std(variance):
    return math.sqrt(variance)

def print_spread(dataset):
    variance = calc_variance(dataset)
    std = calc_std(variance)

    print('Variance: {}; Standard Deviation: {}'.format(variance, std))
    return

i1 = [5, 5, 5, 5, 5, 5]
i2 = [12, -2, 10, 0, 7, 3]

print('Investimentos 1')
print_spread(i1)
print('')
print('Investimentos 2')
print_spread(i2)