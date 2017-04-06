#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import DataFrame
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import math

def main(df, label):
    #print "one-way anova F value: " + TODO + "\n degree of freedom between group: " + TODO + "\n degree of freedom within group: " + TODO     
    
    # calculate sample_data_average [ave_x, ave_y]
    within_average = df[label].mean()
    # print group_average['Japanese']

    # TODO calculate total average
    between_average = np.mean(df[label].values.flatten())
    # print between_average

    within_variance = df[label].var(ddof=False)
    # print group_variance['Japanese']

    # TODO calculate total variance
    between_variance = np.var(df[label].values.flatten())
    # print between_variance
    
    # TODO calculate heihouwa
    within_heihouwa = 0.0
    for i in range(len(label)):
        within_heihouwa += (between_average - within_average[label[i]]) * (between_average - within_average[label[i]]) * len(df[label[i]])
    # print within_heihouwa

    between_heihouwa = between_variance * len(df[label].values.flatten())
    # print between_heihouwa

    # TODO calculate dof
    between_dof = len(label) - 1
    #print between_dof
    within_dof = 0
    for i in range(len(label)):
        #print len(label[i])
        within_dof += len(df[label[i]]) - 1
    # print within_dof

    # TODO calculate heikin heihou
    between_heikin_heihou = between_heihouwa / between_dof
    within_heikin_heihou = within_heihouwa / within_dof
    print between_heikin_heihou
    print within_heikin_heihou

    # TODO calculate F value
    F = between_heikin_heihou / within_heikin_heihou
    print F

if __name__ == '__main__':
    data = {'Japanese':  [68, 75, 80, 71, 73, 79, 69, 65],
            'Mathematics': [86, 83, 76, 81, 75, 82, 87, 75],
            'Science' : [85, 69, 77, 77, 75, 74, 87, 69],
            'English': [80, 76, 84, 93, 76, 80, 79, 84]}
    df = DataFrame(data, index = ["Student" + str(i+1)  for i  in np.arange(8)])
    main(df, ['Japanese', 'Mathematics', 'Science'])
