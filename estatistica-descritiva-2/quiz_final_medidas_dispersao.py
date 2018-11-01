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

def calc_median(dataset):
    n = len(dataset)
    sorted_dataset = sorted(dataset)
    if (n % 2 == 0):
        return sum(sorted_dataset[n//2-1:n//2+1])/2.0
    else:
        return sorted_dataset[n//2]

def print_spread(dataset):
    print('Data set: '.upper() + str(dataset))
    dataset_len = len(dataset)
    mean = sum(dataset)/dataset_len
    median = calc_median(dataset)
    variance = calc_variance(dataset)
    std = calc_std(variance)
    sorted_dataset = sorted(dataset)
    dataset_minimum = sorted_dataset[0]
    dataset_maximum = sorted_dataset[-1]
    dataset_range = dataset_maximum - dataset_minimum

    print('* Number of elements: {}\n* Mean: {}\n* Median: {}\n* Variance: {}\n* Standard deviation: {}\n* Minimum: {}\n* Maximum: {}\n* Range: {}\n* Sorted data set: {}'.format(dataset_len, mean, median, variance, std, dataset_minimum, dataset_maximum, dataset_range, sorted_dataset))
    return

dataset = input('Please, inform the elements of the data set: ').split(',')
dataset = [int(value) for value in dataset]
print_spread(dataset)