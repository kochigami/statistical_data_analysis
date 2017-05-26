#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import DataFrame
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import math
from texttable import Texttable
from calculate_average import CalculateAverage
from calculate_variance import CalculateVariance

# within: gun-nai
# between: gun-kan

def main(df, label):

    calculate_average = CalculateAverage()
    calculate_variance = CalculateVariance()

    ### calculate total average ###
    within_average, within_num = calculate_average.calc_average_of_total(df, label)
    between_average, between_num = calculate_average.calc_average_of_each_sample(df, label)
    #print within_average
    #print between_average

    ### calculate total variance ###
    within_variance = []
    between_variance = calculate_variance.calculate_variance_of_each(df, label)
    within_variance.append(calculate_variance.calc_variance_of_total(df, label))
    #print within_variance
    #print between_variance
    
    ### calculate sum of squares ###
    between_sum_of_squares = 0.0
    within_sum_of_squares = 0.0
    for i in range(len(label)):
        between_sum_of_squares += (within_average[0] - between_average[i]) *  (within_average[0] - between_average[i]) * len(df[label[i]])
    for i in range(len(label)):
        within_sum_of_squares += between_variance[i] * len(df[label[i]])
    
    #print between_sum_of_squares
    #print within_sum_of_squares

    ### calculate dof ###
    between_dof = len(label) - 1
    within_dof = 0
    for i in range(len(label)):
        within_dof += len(df[label[i]]) - 1
    # print between_dof
    # print within_dof

    ### calculate mean square ###
    between_mean_square = between_sum_of_squares / between_dof
    within_mean_square = within_sum_of_squares / within_dof
    # print between_mean_square
    # print within_mean_square

    ### calculate F value ###
    F = between_mean_square / within_mean_square
    # print F

    table = Texttable()
    table.set_cols_align(["c", "c", "c", "c", "c"])
    table.set_cols_valign(["m", "m", "m", "m", "m"])
    table.add_rows([ ["Factor", "Sum of Squares", "Dof", "Mean Square", "F"], 
                     ["Between Groups", str(between_sum_of_squares), str(between_dof), str(between_mean_square), str(F)],
                     ["Within Groups", str(within_sum_of_squares), str(within_dof), str(within_mean_square), ""] ])
    print table.draw()

    print "one-way anova F value: " + str(F) + "\n degree of freedom between group: " + str(between_dof) + "\n degree of freedom within group: " + str(within_dof)     


if __name__ == '__main__':
    # data = {'Japanese':  [68, 75, 80, 71, 73, 79, 69, 65],
    #         'Mathematics': [86, 83, 76, 81, 75, 82, 87, 75],
    #         'Science' : [85, 69, 77, 77, 75, 74, 87, 69],
    #         'English': [80, 76, 84, 93, 76, 80, 79, 84]}
    # data = {'Japanese':  [80, 75, 80, 90, 95, 80, 80, 85, 85, 80, 90, 80, 75, 90, 85, 85, 90, 90, 85, 80],
    #         'Mathematics': [75, 70, 80, 85, 90, 75, 85, 80, 80, 75, 80, 75, 70, 85, 80, 75, 80, 80, 90, 80],
    #         'Science' : [80, 80, 80, 90, 95, 85, 95, 90, 85, 90, 95, 85, 98, 95, 85, 85, 90, 90, 85, 85]}

    data = {'vision':  [2.148006, 2.198387, 2.009008, 2.033217, 2.148546, 1.64081],
            'sound': [1.597316, 1.6, 2.398989, 2.418485, 2.306829, 1.579134],
            'vision + sound' : [1.442516, 1.873331, 1.755275, 2.190506, 3.176726, 2.009838]}

    df = DataFrame(data, index = [str(i+1)  for i  in np.arange(6)]) # must change the length of array

    main(df, ['vision', 'sound', 'vision + sound'])
