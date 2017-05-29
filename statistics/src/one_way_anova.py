#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import DataFrame
import numpy as np
from calculate_average import CalculateAverage
from calculate_variance import CalculateVariance
from analysis_of_variance import AnalysisOfVariance

# within: gun-nai
# between: gun-kan

class OneWayAnova:
    def __init__(self):
        self.calculate_average = CalculateAverage()
        self.calculate_variance = CalculateVariance()
        self.analysis_of_variance = AnalysisOfVariance()

    def calc_one_way_anova(self, df_of_each_group, label_of_each_group, df_of_all_samples, label_of_all_samples):
        
        ### calculate total average ###
        within_average = []
        for i in range(len(label_of_each_group)):
            within_average.append(self.calculate_average.calc_average(df_of_each_group, label_of_each_group[i]))
        average_of_all = self.calculate_average.calc_average(df_of_all_samples, label_of_all_samples)
        
        ### calculate sample nums ###
        sample_num_per_group =[]
        total_sample_num = []
        sample_num_per_group = self.analysis_of_variance.calc_sample_num(df_of_each_group, label_of_each_group, sample_num_per_group)
        total_sample_num = self.analysis_of_variance.calc_sample_num(df_of_all_samples, label_of_all_samples, total_sample_num)

        ### calculate total variance ###
        within_variance = []
        for i in range(len(label_of_each_group)):
            within_variance.append(self.calculate_variance.calc_variance(df_of_each_group, label_of_each_group[i]))
        variance_of_all = self.calculate_variance.calc_variance(df_of_all_samples, label_of_all_samples)
        
        ### calculate sum of squares ###
        between_sum_of_squares = 0.0
        within_sum_of_squares = 0.0
        for i in range(len(label_of_each_group)):
            within_sum_of_squares += within_variance[i] * sample_num_per_group[i]
        between_sum_of_squares = variance_of_all * total_sample_num[0] - within_sum_of_squares

        ### calculate dof ###
        between_dof = len(label_of_each_group) - 1.0
        within_dof = 0.0
        for i in range(len(label_of_each_group)):
            within_dof += len(df[label_of_each_group[i]]) - 1.0

        ### calculate mean square ###
        between_mean_square = between_sum_of_squares / between_dof
        within_mean_square = within_sum_of_squares / within_dof

        ### calculate F value ###
        F = between_mean_square / within_mean_square

        sum_of_squares = {"Within Groups": within_sum_of_squares,
                          "Between Groups": between_sum_of_squares,
                          "Total": within_sum_of_squares + between_sum_of_squares}

        dof = {"Within Groups": within_dof,
               "Between Groups": between_dof,
               "Total": within_dof + between_dof}
        
        mean_squares = {"Within Groups": within_mean_square,
                        "Between Groups": between_mean_square}

        self.analysis_of_variance.show_table(sum_of_squares, dof, mean_squares, F, analysis_type="one-way")
        #print "one-way anova F value: " + str(F) + "\n degree of freedom between group: " + str(between_dof) + "\n degree of freedom within group: " + str(within_dof) 

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

    data_all = {'all': [2.148006, 2.198387, 2.009008, 2.033217, 2.148546, 1.64081, 1.597316, 1.6, 2.398989, 2.418485, 2.306829, 1.579134, 1.442516, 1.873331, 1.755275, 2.190506, 3.176726, 2.009838]}

    df = DataFrame(data, index = [str(i+1)  for i  in np.arange(6)]) # must change the length of array
    df_all = DataFrame(data_all, index = [str(i+1)  for i  in np.arange(18)])

    one_way_anova = OneWayAnova()
    one_way_anova.calc_one_way_anova(df, ['vision', 'sound', 'vision + sound'], df_all, ['all'])
