#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import DataFrame
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import math

# within: gun-nai
# between: gun-kan

def main(data, label):
    ### calculate total average ###
    within_average = np.mean(df[label].values.flatten())
    between_average = df[label].mean()
    # print within_average
    # print between_average

    ### calculate total variance ###
    within_variance = np.var(df[label].values.flatten())
    between_variance = df[label].var(ddof=False)
    # print within_variance
    # print between_variance
    
    ### calculate heihouwa ###
    between_heihouwa = 0.0
    within_heihouwa = 0.0
    for i in range(len(label)):
        between_heihouwa += (within_average - between_average[label[i]]) *  (within_average - between_average[label[i]]) * len(df[label[i]])
    for i in range(len(label)):
        within_heihouwa += between_variance[label[i]] * len(df[label[i]])
    # print between_heihouwa
    # print within_heihouwa

    ### calculate dof ###
    between_dof = len(label) - 1
    within_dof = 0
    for i in range(len(label)):
        within_dof += len(df[label[i]]) - 1
    # print between_dof
    # print within_dof

    ### calculate heikin heihou ###
    between_heikin_heihou = between_heihouwa / between_dof
    within_heikin_heihou = within_heihouwa / within_dof
    # print between_heikin_heihou
    # print within_heikin_heihou

    ### calculate F value ###
    F = between_heikin_heihou / within_heikin_heihou
    # print F

    print "one-way anova F value: " + str(F) + "\n degree of freedom between group: " + str(between_dof) + "\n degree of freedom within group: " + str(within_dof)     


if __name__ == '__main__':
    # data = {'Japanese':  [68, 75, 80, 71, 73, 79, 69, 65],
    #         'Mathematics': [86, 83, 76, 81, 75, 82, 87, 75],
    #         'Science' : [85, 69, 77, 77, 75, 74, 87, 69],
    #         'English': [80, 76, 84, 93, 76, 80, 79, 84]}
    data = {'Japanese':  [80, 75, 80, 90, 95, 80, 80, 85, 85, 80, 90, 80, 75, 90, 85, 85, 90, 90, 85, 80],
            'Mathematics': [75, 70, 80, 85, 90, 75, 85, 80, 80, 75, 80, 75, 70, 85, 80, 75, 80, 80, 90, 80],
            'Science' : [80, 80, 80, 90, 95, 85, 95, 90, 85, 90, 95, 85, 98, 95, 85, 85, 90, 90, 85, 85]}

    df = DataFrame(data, index = [str(i+1)  for i  in np.arange(20)]) # must change the length of array

    main(df, ['Japanese', 'Mathematics', 'Science'])
