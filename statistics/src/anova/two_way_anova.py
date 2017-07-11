#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import DataFrame
import numpy as np
import math
from analysis_of_variance import AnalysisOfVariance

import sys
import os
sys.path.append( os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/basic')
from calculate_average import CalculateAverage
from calculate_variance import CalculateVariance

class TwoWayAnova:
    def __init__(self):
        self.calculate_average = CalculateAverage()
        self.calculate_variance = CalculateVariance()
        self.analysis_of_variance = AnalysisOfVariance()
    
    def calc_two_way_anova(self, df_of_each_group, label_of_each_group, df_factor1, label_factor1, df_factor2, label_factor2, df_of_all_samples, label_of_all_samples, test_mode="between"):

        ### calculate average ###
        within_average = []
        for i in range(len(label_of_each_group)):
            within_average.append(self.calculate_average.calc_average(df_of_each_group, label_of_each_group[i]))
        factor1_average = []
        for i in range(len(label_factor1)):
            factor1_average.append(self.calculate_average.calc_average(df_factor1, label_factor1[i]))
        factor2_average = []
        for i in range(len(label_factor2)):
            factor2_average.append(self.calculate_average.calc_average(df_factor2, label_factor2[i]))
        average_of_all = self.calculate_average.calc_average(df_of_all_samples, label_of_all_samples)

        ### calculate sample nums ###
        sample_num_per_group =[]
        sample_num_per_group = self.analysis_of_variance.calc_sample_num(df_of_each_group, label_of_each_group, sample_num_per_group)
        sample_num_per_factor1 = []
        sample_num_per_factor1 = self.analysis_of_variance.calc_sample_num(df_factor1, label_factor1, sample_num_per_factor1)
        sample_num_per_factor2 = []
        sample_num_per_factor2 = self.analysis_of_variance.calc_sample_num(df_factor2, label_factor2, sample_num_per_factor2)
        total_sample_num = []
        total_sample_num = self.analysis_of_variance.calc_sample_num(df_of_all_samples, label_of_all_samples, total_sample_num)        

        ### calculate total variance ###
        within_variance = []
        for i in range(len(label_of_each_group)):
            within_variance.append(self.calculate_variance.calc_variance(df_of_each_group, label_of_each_group[i]))
        factor1_variance = []
        for i in range(len(label_factor1)):
            factor1_variance.append(self.calculate_variance.calc_variance(df_factor1, label_factor1[i]))
        factor2_variance = []
        for i in range(len(label_factor2)):
            factor2_variance.append(self.calculate_variance.calc_variance(df_factor2, label_factor2[i]))
        variance_of_all = self.calculate_variance.calc_variance(df_of_all_samples, label_of_all_samples)

        ### calculate sum of squares ###
        sum_of_squares_of_others = 0.0
        for i in range(len(label_of_each_group)):
            sum_of_squares_of_others += self.analysis_of_variance.calc_sum_of_squares(within_variance[i], sample_num_per_group[i])
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
            
        if test_mode == "within":
            tmp = 0.0
            tmp_sum = 0.0
            correction_term = 0.0
            preparation_term = 0.0
            for i in range(len(df_of_each_group[label_of_each_group[0]])):
                tmp = 0.0
                for j in range(len(label_of_each_group)):
                    tmp += (df_of_each_group[label_of_each_group[j]])[i]
                tmp_sum += tmp
                preparation_term += pow(tmp, 2.0) / (len(label_factor1) * len(label_factor2))

            correction_term = pow(tmp_sum, 2.0) / total_sample_num[0]

            sum_of_squares_of_subject = preparation_term - correction_term

            tmp = 0.0
            tmp_sum = 0.0
            for i in range(len(label_factor1)):
                for k in range(len(df_of_each_group[label_of_each_group[0]])):
                    for j in range(len(label_of_each_group)):
                        if label_factor1[i] in label_of_each_group[j]:
                            tmp += (df_of_each_group[label_of_each_group[j]])[k]
                    tmp_sum += pow(tmp, 2.0)
                    tmp = 0.0
            sum_of_squares_of_factor1_error = (tmp_sum / len(label_factor2)) - sum_of_squares_of_subject - correction_term - sum_of_squares_of_factor1

            tmp = 0.0
            tmp_sum = 0.0
            for i in range(len(label_factor2)):
                for k in range(len(df_of_each_group[label_of_each_group[0]])):
                    for j in range(len(label_of_each_group)):
                        if label_factor2[i] in label_of_each_group[j]:
                            tmp += (df_of_each_group[label_of_each_group[j]])[k]
                    tmp_sum += pow(tmp, 2.0)
                    tmp = 0.0
            sum_of_squares_of_factor2_error = (tmp_sum / len(label_factor1)) - sum_of_squares_of_subject - correction_term - sum_of_squares_of_factor2

            sum_of_squares_of_interaction_error = sum_of_squares_of_others - sum_of_squares_of_subject - sum_of_squares_of_factor1_error - sum_of_squares_of_factor2_error
        
        ### calculate dof ###
        dof_of_factor1 = len(sample_num_per_factor1) - 1.0
        dof_of_factor2 = len(sample_num_per_factor2) - 1.0
        dof_of_interaction = dof_of_factor1 * dof_of_factor2
        dof_of_all = total_sample_num[0] - 1.0
        dof_of_others = dof_of_all - dof_of_factor1 - dof_of_factor2 - dof_of_interaction
                
        if test_mode == "within":
            dof_of_subject = len(df_of_each_group[label_of_each_group[0]]) -1.0
            dof_factor1_x_subject = dof_of_factor1 * dof_of_subject
            dof_factor2_x_subject = dof_of_factor2 * dof_of_subject
            dof_factor1_x_factor2_x_subject = dof_of_factor1 * dof_of_factor2 * dof_of_subject

        ### calculate sum of squares ###
        mean_square_of_factor1 = 0.0
        mean_square_of_factor1 = self.analysis_of_variance.calc_mean_square(sum_of_squares_of_factor1, dof_of_factor1)
        mean_square_of_factor2 = 0.0        
        mean_square_of_factor2 = self.analysis_of_variance.calc_mean_square(sum_of_squares_of_factor2, dof_of_factor2)
        mean_square_of_interaction = 0.0
        mean_square_of_interaction = self.analysis_of_variance.calc_mean_square(sum_of_squares_of_interaction, dof_of_interaction)

        mean_square_of_others = 0.0
        mean_square_of_others = self.analysis_of_variance.calc_mean_square(sum_of_squares_of_others, dof_of_others)

        if test_mode == "within":
            mean_square_of_subject = self.analysis_of_variance.calc_mean_square(sum_of_squares_of_subject, dof_of_subject)
            mean_square_of_factor1_error = self.analysis_of_variance.calc_mean_square(sum_of_squares_of_factor1_error, dof_factor1_x_subject)
            mean_square_of_factor2_error = self.analysis_of_variance.calc_mean_square(sum_of_squares_of_factor2_error, dof_factor2_x_subject)
            mean_square_of_interaction_error = self.analysis_of_variance.calc_mean_square(sum_of_squares_of_interaction_error, dof_factor1_x_factor2_x_subject)

        ### calculate F ###
        if test_mode == "between":
            F_of_factor1 = self.analysis_of_variance.calc_F(mean_square_of_factor1, mean_square_of_others)
            F_of_factor2 = self.analysis_of_variance.calc_F(mean_square_of_factor2, mean_square_of_others)
            F_of_interaction = self.analysis_of_variance.calc_F(mean_square_of_interaction, mean_square_of_others)

        elif test_mode == "within":
            F_of_factor1 = self.analysis_of_variance.calc_F(mean_square_of_factor1, mean_square_of_factor1_error)
            F_of_factor2 = self.analysis_of_variance.calc_F(mean_square_of_factor2, mean_square_of_factor2_error)
            F_of_interaction = self.analysis_of_variance.calc_F(mean_square_of_interaction, mean_square_of_interaction_error)

        if test_mode == "between":
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
        
            self.analysis_of_variance.show_table(sum_of_squares, dof, mean_squares, F, analysis_type="two-way-between")

        elif test_mode == "within":
            sum_of_squares = {"Subject": sum_of_squares_of_subject,
                              "Factor1": sum_of_squares_of_factor1,
                              "Subject x Factor1": sum_of_squares_of_factor1_error,
                              "Factor2": sum_of_squares_of_factor2,
                              "Subject x Factor2": sum_of_squares_of_factor2_error,
                              "Interaction": sum_of_squares_of_interaction,
                              "Subject x Interaction": sum_of_squares_of_interaction_error,
                              "Total": sum_of_squares_of_subject + sum_of_squares_of_factor1 + sum_of_squares_of_factor1_error + sum_of_squares_of_factor2 + sum_of_squares_of_factor2_error + sum_of_squares_of_interaction + sum_of_squares_of_interaction_error}

            dof = {"Subject": dof_of_subject,
                   "Factor1": dof_of_factor1,
                   "Subject x Factor1": dof_factor1_x_subject,
                   "Factor2": dof_of_factor2,
                   "Subject x Factor2": dof_factor2_x_subject,
                   "Interaction": dof_of_interaction,
                   "Subject x Interaction": dof_factor1_x_factor2_x_subject,
                   "Total": dof_of_all}

            mean_squares = {"Subject": mean_square_of_subject,
                            "Factor1": mean_square_of_factor1,
                            "Subject x Factor1": mean_square_of_factor1_error,
                            "Factor2": mean_square_of_factor2,
                            "Subject x Factor2": mean_square_of_factor2_error,
                            "Interaction": mean_square_of_interaction,
                            "Subject x Interaction": mean_square_of_interaction_error}
        
            F = {"Factor1": F_of_factor1,
                 "Factor2": F_of_factor2,
                 "Interaction": F_of_interaction}

            self.analysis_of_variance.show_table(sum_of_squares, dof, mean_squares, F, analysis_type="two-way-within")

        if test_mode == "between":
            '''
            Draw matplotlib table.
            Args: sum_of_squares_of_factor1
                  sum_of_squares_of_factor2
                  sum_of_squares_of_interaction
                  sum_of_squares_of_others
                  dof_of_factor1
                  dof_of_factor2
                  dof_of_interaction
                  dof_of_others
                  dof_of_all
                  mean_square_of_factor1
                  mean_square_of_factor2
                  mean_square_of_interaction
                  mean_square_of_others
                  F_of_factor1
                  F_of_factor2
                  F_of_interaction
            '''
            show_table_df = self.analysis_of_variance.make_df_of_two_way_anova_for_matplotlib_table(sum_of_squares_of_factor1, sum_of_squares_of_factor2, sum_of_squares_of_interaction, sum_of_squares_of_others, dof_of_factor1, dof_of_factor2, dof_of_interaction, dof_of_others, dof_of_all, mean_square_of_factor1, mean_square_of_factor2, mean_square_of_interaction, mean_square_of_others, F_of_factor1, F_of_factor2, F_of_interaction)
            self.analysis_of_variance.matplotlib_table(show_table_df)

if __name__ == '__main__':
    pass
