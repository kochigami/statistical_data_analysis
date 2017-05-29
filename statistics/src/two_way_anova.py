#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import DataFrame
#from scipy import stats
#import matplotlib.pyplot as plt
import numpy as np
import math
#from texttable import Texttable
from calculate_average import CalculateAverage
from calculate_variance import CalculateVariance
from analysis_of_variance import AnalysisOfVariance

class TwoWayAnova:
    def __init__(self):
        self.calculate_average = CalculateAverage()
        self.calculate_variance = CalculateVariance()
        self.analysis_of_variance = AnalysisOfVariance()
    
    def calc_two_way_anova(self, df_of_each_group, label_of_each_group, df_factor1, label_factor1, df_factor2, label_factor2, df_of_all_samples, label_of_all_samples):
        ### calculate total average ###
        within_average = []
        factor1_average = []
        factor2_average = []
        for i in range(len(label_of_each_group)):
            within_average.append(self.calculate_average.calc_average(df_of_each_group, label_of_each_group[i]))

        for i in range(len(label_factor1)):
            factor1_average.append(self.calculate_average.calc_average(df_factor1, label_factor1[i]))

        for i in range(len(label_factor2)):
            factor2_average.append(self.calculate_average.calc_average(df_factor2, label_factor2[i]))

        average_of_all = self.calculate_average.calc_average(df_of_all_samples, label_of_all_samples)
        
        ### calculate sample nums ###
        sample_num_per_group =[]
        sample_num_per_factor1 = []
        sample_num_per_factor2 = []
        total_sample_num = []
        sample_num_per_group = self.analysis_of_variance.calc_sample_num(df_of_each_group, label_of_each_group, sample_num_per_group)
        sample_num_per_factor1 = self.analysis_of_variance.calc_sample_num(df_factor1, label_factor1, sample_num_per_factor1)
        sample_num_per_factor2 = self.analysis_of_variance.calc_sample_num(df_factor2, label_factor2, sample_num_per_factor2)
        total_sample_num = self.analysis_of_variance.calc_sample_num(df_of_all_samples, label_of_all_samples, total_sample_num)

        ### calculate total variance ###
        within_variance = []
        factor1_variance = []
        factor2_variance = []
        for i in range(len(label_of_each_group)):
            within_variance.append(self.calculate_variance.calc_variance(df_of_each_group, label_of_each_group[i]))
        for i in range(len(label_factor1)):
            factor1_variance.append(self.calculate_variance.calc_variance(df_factor1, label_factor1[i]))
        for i in range(len(label_factor2)):
            factor2_variance.append(self.calculate_variance.calc_variance(df_factor2, label_factor2[i]))
        variance_of_all = self.calculate_variance.calc_variance(df_of_all_samples, label_of_all_samples)
        
        ### calculate sum of squares ###
        sum_of_squares_of_others = 0.0
        for i in range(len(label_of_each_group)):
            sum_of_squares_of_others += within_variance[i] * sample_num_per_group[i]
        
        sum_of_squares_of_each_group = 0.0
        for i in range(len(label_of_each_group)):
            sum_of_squares_of_each_group += math.pow((within_average[i] - average_of_all), 2) * sample_num_per_group[i]

        sum_of_squares_of_factor1 = 0.0
        for i in range(len(label_factor1)):
            sum_of_squares_of_factor1 += math.pow((factor1_average[i] - average_of_all), 2) * sample_num_per_factor1[i]

        sum_of_squares_of_factor2 = 0.0
        for i in range(len(label_factor2)):
            sum_of_squares_of_factor2 += math.pow((factor2_average[i] - average_of_all), 2) * sample_num_per_factor2[i]
    
        sum_of_squares_of_interaction = sum_of_squares_of_each_group - sum_of_squares_of_factor1 - sum_of_squares_of_factor2
        
        ### calculate dof ###
        dof_of_factor1 = len(sample_num_per_factor1) - 1.0
        dof_of_factor2 = len(sample_num_per_factor2) - 1.0
        dof_of_interaction = dof_of_factor1 * dof_of_factor2
        dof_of_all = total_sample_num[0] - 1.0
        dof_of_others = dof_of_all - dof_of_factor1 - dof_of_factor2 - dof_of_interaction

        ### calculate sum of squares ###
        mean_square_of_factor1 = 0.0
        mean_square_of_factor2 = 0.0
        mean_square_of_interaction = 0.0
        mean_square_of_others = 0.0

        mean_square_of_factor1 = sum_of_squares_of_factor1 / dof_of_factor1
        mean_square_of_factor2 = sum_of_squares_of_factor2 / dof_of_factor2
        mean_square_of_interaction = sum_of_squares_of_interaction / dof_of_interaction
        mean_square_of_others = sum_of_squares_of_others / dof_of_others

        ### calculate F ###
        F_of_factor1 = mean_square_of_factor1 / mean_square_of_others
        F_of_factor2 = mean_square_of_factor2 / mean_square_of_others
        F_of_interaction = mean_square_of_interaction / mean_square_of_others

        sum_of_squares = {"Factor1": sum_of_squares_of_factor1,
                          "Factor2": sum_of_squares_of_factor2,
                          "Interaction": sum_of_squares_of_interaction,
                          "Others": sum_of_squares_of_others,
                          "Total": sum_of_squares_of_factor1 + sum_of_squares_of_factor2 + sum_of_squares_of_interaction + sum_of_squares_of_others}
        
        dof = {"Factor1": dof_of_factor1,
               "Factor2": dof_of_factor2,
               "Interaction": dof_of_interaction,
               "Others": dof_of_others,
               "Total": dof_of_all}
        
        mean_squares = {"Factor1": mean_square_of_factor1,
                        "Factor2": mean_square_of_factor2,
                        "Interaction": mean_square_of_interaction,
                        "Others": mean_square_of_others}
        
        F = {"Factor1": F_of_factor1,
             "Factor2": F_of_factor2,
             "Interaction": F_of_interaction}
        
        self.analysis_of_variance.show_table(sum_of_squares, dof, mean_squares, F, analysis_type="two-way")

        show_table_df = DataFrame (index=list("12345"), columns=[])
        show_table_df['Sum of Squares'] = [sum_of_squares_of_factor1, sum_of_squares_of_factor2, sum_of_squares_of_interaction, sum_of_squares_of_others, sum_of_squares_of_factor1 + sum_of_squares_of_factor2 + sum_of_squares_of_interaction + sum_of_squares_of_others]
        show_table_df['DOF'] = [dof_of_factor1, dof_of_factor2, dof_of_interaction, dof_of_others, dof_of_all]
        show_table_df['Mean Square'] = [mean_square_of_factor1, mean_square_of_factor2, mean_square_of_interaction, mean_square_of_others, ""]
        show_table_df['F'] = [F_of_factor1, F_of_factor2, F_of_interaction, "", ""]
        show_table_df.index = ['Factor1', 'Factor2', 'Interaction', 'Others', 'Total']
        
        self.analysis_of_variance.matplotlib_table(show_table_df)

if __name__ == '__main__':
    # data = {'Crispy-hot':  [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
    #         'Crispy-mild': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
    #         'Normal-hot' : [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
    #         'Normal-mild' : [70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]
    #     }

    data = {'Crispy-hot':  [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
            'Crispy-normal': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
            'Crispy-mild': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
            'Normal-hot' : [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
            'Normal-normal' : [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
            'Normal-mild' : [70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]
        }

    df = DataFrame(data, index = [str(i+1)  for i  in np.arange(15)])
    
    data_factor1 = {'Crispy': [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90, 65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75, 65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
                    'Normal': [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75, 70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75, 70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]}

    data_factor2 = {'hot': [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90, 70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
                    'normal': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75, 70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
                    'mild': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75, 70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]}

    df_factor1 = DataFrame(data_factor1, index = [str(i+1)  for i  in np.arange(45)])
    df_factor2 = DataFrame(data_factor2, index = [str(i+1)  for i  in np.arange(30)])

    data_all = {'all': [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90, 65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75, 65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75, 70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75, 70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75, 70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]
            }

    df_all = DataFrame(data_all, index = [str(i+1) for i in np.arange(90)])

    two_way_anova = TwoWayAnova()
    two_way_anova.calc_two_way_anova(df, ['Crispy-hot', 'Crispy-normal', 'Crispy-mild', 'Normal-hot', 'Normal-normal', 'Normal-mild'], df_factor1, ['Crispy', 'Normal'], df_factor2, ['hot', 'normal', 'mild'], df_all, ['all'])
