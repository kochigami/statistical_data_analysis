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
    group_average = df[label].mean()
    # print group_average['Japanese']

    # TODO calculate total average

    group_variance = df[label].var(ddof=False)
    # print group_variance['Japanese']

    # TODO calculate total variance

    # TODO calculate heihouwa
    
    # TODO calculate dof

    # TODO calculate heikin heihou

    # TODO calculate F value

if __name__ == '__main__':
    data = {'Japanese':  [68, 75, 80, 71, 73, 79, 69, 65],
            'Mathematics': [86, 83, 76, 81, 75, 82, 87, 75],
            'Science' : [85, 69, 77, 77, 75, 74, 87, 69],
            'English': [80, 76, 84, 93, 76, 80, 79, 84]}
    df = DataFrame(data, index = ["Student" + str(i+1)  for i  in np.arange(8)])
    main(df, ['Japanese', 'Mathematics', 'Science'])
