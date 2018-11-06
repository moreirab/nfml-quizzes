def calc_harmonic_mean(precision, recall):
    return (2*(precision*recall))/(precision+recall)

precision = float(input('Please, inform the precision: '))
recall = float(input('Please, inform the recall: '))

print('The F1 score is: ' + str(calc_harmonic_mean(precision, recall)))
print('The mean is: ' + str((precision+recall)/2))