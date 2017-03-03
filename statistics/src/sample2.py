#!/usr/bin/env python
import numpy as np
import math

def main():
    a =[70, 75, 70, 85, 90, 70, 80, 75]
    b =[85, 80, 95, 70, 80, 75, 80, 90]
    #a = [0, 1, 3, 1, 3, 3, 4, 2, 4, 1, 3, 3, 0, 2, 1]
    #b = [1, 3, 2, 4, 3, 4, 2, 1, 5, 2, 3, 4, 5, 1, 1]
    # unpaired t-value: -1.31631047528, degree of freedom: 28
    #b = [1, 3, 2, 4, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    # unpaired t-value: -4.29303354125, degree of freedom: 28 
    t = t_value(a, b)
    print "unpaired t-value: " + str(t) + ", degree of freedom: " + str((len(a) - 1) + (len(b) - 1))

def raw_data_average (l):
    ave = 0.0
    for i in range(len(l)):
        ave = ave + l[i]
    ave = ave / (len(l))
    return ave

def sample_variance (l):
    sample_variance = 0.0
    ave = raw_data_average(l)
    for i in range(len(l)):
        sample_variance += (l[i] - ave) * (l[i] - ave)
    sample_variance = sample_variance / (len(l))
    return sample_variance

def difference_average (l1, l2):
    difference_average = 0.0
    for i in range(len(l1)):
        difference_average += l1[i] - l2[i]
    difference_average = difference_average / (len(l1))
    return difference_average

def difference_variance (l1, l2):
    difference_variance = 0.0
    sample_variance1 = sample_variance(l1)
    sample_variance2 = sample_variance(l2)
    difference_variance = (sample_variance1 * (len(l1)) + sample_variance2 * (len(l2))) / ((len(l1) + len(l2) -2))
    return difference_variance

def difference_error (l1, l2):
    difference_error = 0.0
    diff_variance = difference_variance(l1, l2)
    difference_error = math.sqrt (diff_variance * ((1.0 / (len(l1))) + (1.0 / (len(l2)))))
    return difference_error

def t_value (l1, l2):
    t = 0.0
    diff_average = difference_average(l1, l2)
    diff_error = difference_error(l1, l2)
    t = diff_average / diff_error
    return t

if __name__ == '__main__':
    main()
