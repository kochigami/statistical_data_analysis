#!/usr/bin/env python
import numpy as np
import math

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

def main():
    #a = [225.48972,
    #     236.54971]
    #b = [169.1854,
    #     163.793112679]
    a = [255.56605,
         267.48198]
    b = [135.141159,
         84.659183899]
    #a = [90, 75, 75, 75, 80, 65, 75, 80]
    #b = [95, 80, 80, 80, 75, 75, 80, 85]
    #a = [0, 1, 3, 1, 3, 3, 4, 2, 4, 1, 3, 3, 0, 2, 1]
    #b = [1, 3, 2, 4, 3, 4, 2, 1, 5, 2, 3, 4, 5, 1, 1]
    # paired t-value: -1.46759877141, degree of freedom: 14
    #b = [1, 3, 2, 4, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    # paired t-value: -4.92800147686, degree of freedom: 14
    t = t_value(a, b)
    print "paired t-value: " + str(t) + ", degree of freedom: " + str((len(a) - 1))

def difference_average (l1, l2):
    difference_average = 0.0
    for i in range(len(l1)):
        difference_average += l1[i] - l2[i]
    difference_average = difference_average / (len(l1))
    return difference_average

def difference_variance (l1, l2):
    difference_variance = 0.0
    diff_average = difference_average(l1, l2)
    for i in range(len(l1)):
        difference_variance += (l1[i] - l2[i] - diff_average) * (l1[i] - l2[i] - diff_average)
    difference_variance = difference_variance / (len(l1))
    return difference_variance

def difference_error (l1, l2):
    difference_error = 0.0
    diff_variance = difference_variance(l1, l2)
    difference_error = math.sqrt (diff_variance / (len(l1) - 1))
    return difference_error

def t_value (l1, l2):
    t = 0.0
    diff_average = difference_average(l1, l2)
    diff_error = difference_error(l1, l2)
    t = diff_average / diff_error
    return t

if __name__ == '__main__':
    main()