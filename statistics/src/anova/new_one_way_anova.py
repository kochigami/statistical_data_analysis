#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import DataFrame
import numpy as np
from analysis_of_variance import AnalysisOfVariance

import sys
import os
sys.path.append( os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/basic')
from calculate_average import CalculateAverage
from calculate_variance import CalculateVariance

# within: gun-nai
# between: gun-kan

class OneWayAnova:
    def __init__(self):
        self.calculate_average = CalculateAverage()
        self.calculate_variance = CalculateVariance()
        self.analysis_of_variance = AnalysisOfVariance()

    def calc_one_way_anova(self, df_of_each_group, label_of_each_group, df_of_all_samples, label_of_all_samples, test_mode="between"):
        # if within test #
        if test_mode == "within":
            # yobi keisan
            ss_total_data = 0.0
            for i in range(len(label_of_each_group)):
                for j in range(len(df_of_each_group[label_of_each_group[0]])):
                    ss_total_data += pow((df_of_each_group[label_of_each_group[i]])[j], 2.0)
                
            ss_between_data = 0.0
            for i in range(len(label_of_each_group)):
                ss_between_data += pow(df_of_each_group[label_of_each_group[i]].sum(), 2.0) / len(df_of_each_group[label_of_each_group[i]])
            
            ss_subject_data = 0.0
            for i in range(len(df_of_each_group[label_of_each_group[0]])):
                tmp = 0.0
                for j in range(len(label_of_each_group)):
                    tmp += df_of_each_group[label_of_each_group[j]][i]
                ss_subject_data += pow(tmp, 2.0) / len(label_of_each_group)

            # syuseikou
            x = pow(df_of_all_samples[label_of_all_samples].sum(), 2.0) / (len(label_of_each_group) * len(df_of_each_group[label_of_each_group[0]]))

            # sum_of_squares
            ss_total = ss_total_data - x 
            ss_between = ss_between_data - x
            ss_subject = ss_subject_data - x
            ss_error = ss_total - ss_between - ss_subject
            
            # calculate dof
            between_dof = self.analysis_of_variance.calc_dof(len(label_of_each_group))
            subject_dof = self.analysis_of_variance.calc_dof(len(df_of_each_group[label_of_each_group[0]]))
            error_dof = len(df_of_all_samples[label_of_all_samples]) - 1 - between_dof - subject_dof

            # calculate mean square #
            #between_mean_square = self.analysis_of_variance.calc_mean_square(between_sum_of_squares, between_dof)
            between_mean_square = self.analysis_of_variance.calc_mean_square(ss_between, between_dof)
            subject_mean_square = self.analysis_of_variance.calc_mean_square(ss_subject, subject_dof)
            error_mean_square = self.analysis_of_variance.calc_mean_square(ss_error, error_dof)
        
            # calculate f #
            f = between_mean_square / error_mean_square

        # if between test #
        if test_mode == "between":
            ### calculate average ###
            '''
            Calculate within_average: average (float) list of each category 
            Args:
            df_of_each_group: DataFrame of each category
            label_of_each_group: string list. label of each category
            Example:
            within_average: [2.0296623333333335, 1.9834588333333334, 2.074698666666667]
            '''
            within_average = []
            for i in range(len(label_of_each_group)):
                within_average.append(self.calculate_average.calc_average(df_of_each_group, label_of_each_group[i]))
                '''
            Calculate average_of_all: average (float) of all samples
            Args:
            df_of_all_samples: DataFrame of all samples
            label_of_all_samples: string list. Normally, ["all"].
            Example:
            average_of_all: 2.029273
            '''
            average_of_all = self.calculate_average.calc_average(df_of_all_samples, label_of_all_samples)

            ### calculate sample nums ###
            '''
            Calculate sample_num_per_group: float list. sample num of each category
            Args:
            df_of_each_group: DataFrame of each category
            label_of_each_group: string list. label of each category
            Example:
            sample_num_per_group: [6.0, 6.0, 6.0]
            '''
            sample_num_per_group =[]
            sample_num_per_group = self.analysis_of_variance.calc_sample_num(df_of_each_group, label_of_each_group, sample_num_per_group)
            '''
            Calculate total_sample_num: float list. sample num of all categories
            Args:
            df_of_all_samples: DataFrame of all samples
            label_of_all_samples: string list. Normally, ["all"].
            Example:
            total_sample_num: [18.0]
            '''
            total_sample_num = []
            total_sample_num = self.analysis_of_variance.calc_sample_num(df_of_all_samples, label_of_all_samples, total_sample_num)
            
            ### calculate variance ###
            '''
            Calculate within_variance: variance (float) list of each category 
            Args:
            df_of_each_group: DataFrame of each category
            label_of_each_group: string list. label of each category
            Example:
            within_variance: [0.03470865617688887, 0.1543511475384722, 0.2957196379978889]
            '''
            within_variance = []
            for i in range(len(label_of_each_group)):
                within_variance.append(self.calculate_variance.calc_variance(df_of_each_group, label_of_each_group[i]))
            
            '''
            Calculate variance_of_all: variance (float) of all samples
            Args:
            df_of_all_samples: DataFrame of all samples
            label_of_all_samples: string list. Normally, ["all"].
            Example:
            variance_of_all: 0.162980674118
            '''
            variance_of_all = self.calculate_variance.calc_variance(df_of_all_samples, label_of_all_samples)

            ### calculate sum of squares ###
            '''
            Calculate within_sum_of_squares: total sum of squares (float) of each category 
            Args:
            sample_num_per_group: calculated from "calculate sample nums" (float list)
            within_variance: calculated from "calculate variance" (float list) 
            Example:
            within_sum_of_squares: 2.90867665028 
            '''
            within_sum_of_squares = 0.0
            for i in range(len(sample_num_per_group)):
                within_sum_of_squares += self.analysis_of_variance.calc_sum_of_squares(within_variance[i], sample_num_per_group[i])
            '''
            Calculate between_sum_of_squares: total sum of squares (float) of each category 
            Args:           
            variance_of_all: calculated from "calculate variance" (float)
            total_sample_num: calculated from "calculate sample nums" (float list)
            within_sum_of_squares: calculated from "calculate sum of squares" (float)
            Example:
            between_sum_of_squares: 0.0249754838381
            '''
            between_sum_of_squares = 0.0
            between_sum_of_squares = self.analysis_of_variance.calc_sum_of_squares(variance_of_all, total_sample_num[0]) - within_sum_of_squares
            
            ### calculate dof ###
            '''
            Calculate between_dof: total dof (float) of each category num 
            Args:           
            label_of_each_group: args (string list)
            Example:
            between_dof: 2.0
            '''
            between_dof = self.analysis_of_variance.calc_dof(len(label_of_each_group))
            '''
            Calculate within_dof: total dof (float) of each category sample num
            Args:           
            label_of_each_group: args (string list)
            Example:
            within_dof: 15.0
            '''
            within_dof = 0.0
            for i in range(len(label_of_each_group)):
                within_dof += self.analysis_of_variance.calc_dof(len(df_of_each_group[label_of_each_group[i]]))

            ### calculate mean square ###
            '''
            Calculate between_mean_square: mean_square (float) of between categories
            Args:           
            between_sum_of_squares: calculated from "calculate sum of squares" (float)
            between_dof: calculated from "calculate dof" (float)
            Example:
            between_mean_square: 0.012
            '''
            between_mean_square = self.analysis_of_variance.calc_mean_square(between_sum_of_squares, between_dof)
            '''
            Calculate within_mean_square: mean_square (float) of within each category
            Args:           
            within_sum_of_squares: calculated from "calculate sum of squares" (float)
            within_dof: calculated from "calculate dof" (float)
            Example:
            within_mean_square: 0.194
            '''
            within_mean_square = self.analysis_of_variance.calc_mean_square(within_sum_of_squares, within_dof)

            ### calculate F value ###
            '''
            Calculate F value. (float)
            Args:
            between_mean_square: calculated from "calculate mean square" (float)
            within_mean_square: calculated from "calculate mean square" (float)
            Example: 
            F: 0.064
            '''
            F = self.analysis_of_variance.calc_F(between_mean_square, within_mean_square)
            
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

            '''
            Draw matplotlib table.
            Args: between_sum_of_squares
            within_sum_of_squares
            between_dof
            within_dof
            between_mean_square
            within_mean_square
            F
            '''
            show_table_df = self.analysis_of_variance.make_df_of_one_way_anova_for_matplotlib_table(between_sum_of_squares, within_sum_of_squares, between_dof, within_dof, between_mean_square, within_mean_square, F)
            self.analysis_of_variance.matplotlib_table(show_table_df)

if __name__ == '__main__':
    pass
