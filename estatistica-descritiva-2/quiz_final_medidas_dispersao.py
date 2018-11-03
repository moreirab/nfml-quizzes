def calc_mean(dataset):
    # TODO DOC
    return sum(dataset)/len(dataset)

def calc_variance(dataset, is_bessels_correction=False):
    # TODO DOC
    mean = calc_mean(dataset)
    variances = []
    for value in dataset:
        variances.append((value - mean)**2)
    variance = sum(variances)/(len(dataset) - 1) if is_bessels_correction else sum(variances)/len(dataset)
    return variance

def calc_std(variance):
    # TODO DOC
    return variance**.5 # square root

def calc_median(dataset):
    # TODO DOC
    n = len(dataset)
    sorted_dataset = sorted(dataset)
    if (n % 2 == 0):
        return sum(sorted_dataset[n//2-1:n//2+1])/2.0
    else:
        return sorted_dataset[n//2]

def deviations_from_mean(dataset):
    # TODO DOC
    mean = calc_mean(dataset)
    deviations = []
    for value in dataset:
        deviation = value - mean
        deviations.append(deviation)

    return deviations

def absolute_deviations_from_mean(dataset):
    # TODO DOC
    deviations = deviations_from_mean(dataset)
    absolute_deviations = []
    for deviation in deviations:
        absolute_deviation = deviation * -1 if deviation < 0 else deviation
        absolute_deviations.append(absolute_deviation)

    return absolute_deviations

def squared_deviations_from_mean(dataset):
    # TODO DOC
    deviations = deviations_from_mean(dataset)
    squared_deviations = []
    for deviation in deviations:
        squared_deviation = deviation**2
        squared_deviations.append(squared_deviation)

    return squared_deviations

def print_spread(dataset):
    # TODO DOC
    print("*********************************************************")
    print("***********************Data set**************************".upper())
    print("*********************************************************")
    print(str(dataset))
    dataset_len = len(dataset)
    mean = sum(dataset)/dataset_len
    median = calc_median(dataset)
    variance = calc_variance(dataset)
    variance_bessels_correction = calc_variance(dataset, True)
    std = calc_std(variance) # sample std (σ)
    std_bessels_correction = calc_std(variance_bessels_correction) # std of population (s)
    sorted_dataset = sorted(dataset)
    dataset_minimum = sorted_dataset[0]
    dataset_maximum = sorted_dataset[-1]
    dataset_range = dataset_maximum - dataset_minimum
    deviations = deviations_from_mean(dataset)
    average_deviation = calc_mean(deviations)
    absolute_deviations = absolute_deviations_from_mean(dataset)
    average_absolute_deviation = calc_mean(absolute_deviations)
    squared_deviations = squared_deviations_from_mean(dataset)
    average_squared_deviation = calc_mean(squared_deviations)

    print('* Number of elements: {}\n* Mean: {}\n* Median: {}\n* Variance: {}\n* Variance (Bessel\'s correction): {}\n* Standard deviation: {}\n* Standard deviation (Bessel\'s correction): {}\n* Minimum: {}\n* Maximum: {}\n* Range: {}\n* Sorted data set: {}\n* Deviations from mean: {}\n* Average deviation: {}\n* Absolute deviations from mean: {}\n* Average absolute deviation: {}\n* Squared deviations from mean: {}\n* Average squared deviation: {}'.format(dataset_len, mean, median, variance, variance_bessels_correction, std, std_bessels_correction, dataset_minimum, dataset_maximum, dataset_range, sorted_dataset, deviations, average_deviation, absolute_deviations, average_absolute_deviation, squared_deviations, average_squared_deviation))

dataset = input('Please, inform the elements of the data set: ').split(',')
dataset = [float(value.replace('[', '').replace(']', '')) for value in dataset]
print_spread(dataset)