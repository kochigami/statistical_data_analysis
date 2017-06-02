#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import DataFrame
import numpy as np
import math
from calculate_average import CalculateAverage
from calculate_variance import CalculateVariance
from analysis_of_variance import AnalysisOfVariance

class TwoWayAnova:
    def __init__(self):
        self.calculate_average = CalculateAverage()
        self.calculate_variance = CalculateVariance()
        self.analysis_of_variance = AnalysisOfVariance()
    
    def calc_two_way_anova(self, df_of_each_group, label_of_each_group, df_factor1, label_factor1, df_factor2, label_factor2, df_of_all_samples, label_of_all_samples):
        ### calculate average ###
        '''
        Calculate within_average: average (float) list of each category 
        Args:
           df_of_each_group: DataFrame of each category
           label_of_each_group: string list. label of each category
        Example:
           within_average: [79.66666666666667, 71.0, 71.0, 72.66666666666667, 72.66666666666667, 74.33333333333333]
        '''
        within_average = []
        for i in range(len(label_of_each_group)):
            within_average.append(self.calculate_average.calc_average(df_of_each_group, label_of_each_group[i]))
        '''
        Calculate factor1_average: average (float) list of category of factor1 
        Args:
           df_factor1: DataFrame of factor1
           label_factor1: string list. label of factor1
        Example:
           factor1_average: [73.88888888888889, 73.22222222222223]
        '''
        factor1_average = []
        for i in range(len(label_factor1)):
            factor1_average.append(self.calculate_average.calc_average(df_factor1, label_factor1[i]))
        '''
        Calculate factor2_average: average (float) list of category of factor2 
        Args:
           df_factor2: DataFrame of factor2
           label_factor2: string list. label of factor2
        Example:
           factor2_average: [76.16666666666667, 71.83333333333333, 72.66666666666667]
        '''
        factor2_average = []
        for i in range(len(label_factor2)):
            factor2_average.append(self.calculate_average.calc_average(df_factor2, label_factor2[i]))
        '''
        Calculate average_of_all: average (float) of all samples 
        Args:
           df_of_all_samples: DataFrame of all samples
           label_of_all_samples: string list. Normally, ["all"].
        Example:
           average_of_all: 73.5555555556
        '''
        average_of_all = self.calculate_average.calc_average(df_of_all_samples, label_of_all_samples)

        ### calculate sample nums ###
        '''
        Calculate sample_num_per_group: float list. sample num of each category
        Args:
           df_of_each_group: DataFrame of each category
           label_of_each_group: string list. label of each category
        Example:
           sample_num_per_group: [15.0, 15.0, 15.0, 15.0, 15.0, 15.0]
        '''
        sample_num_per_group =[]
        sample_num_per_group = self.analysis_of_variance.calc_sample_num(df_of_each_group, label_of_each_group, sample_num_per_group)
        '''
        Calculate sample_num_per_factor1: float list. sample num per factor1
        Args:
           df_factor1: DataFrame of factor1
           label_factor1: string list. label of factor1
        Example:
           sample_num_per_factor1: [45.0, 45.0]
        '''
        sample_num_per_factor1 = []
        sample_num_per_factor1 = self.analysis_of_variance.calc_sample_num(df_factor1, label_factor1, sample_num_per_factor1)
        '''
        Calculate sample_num_per_factor2: float list. sample num per factor2
        Args:
           df_factor2: DataFrame of factor2
           label_factor2: string list. label of factor2
        Example:
           sample_num_per_factor2: [30.0, 30.0, 30.0]
        '''
        sample_num_per_factor2 = []
        sample_num_per_factor2 = self.analysis_of_variance.calc_sample_num(df_factor2, label_factor2, sample_num_per_factor2)
        '''
        Calculate total_sample_num: float list. sample num of all categories
        Args:
           df_of_all_samples: DataFrame of all samples
           label_of_all_samples: string list. Normally, ["all"].
        Example:
           total_sample_num: [90.0]
        '''
        total_sample_num = []
        total_sample_num = self.analysis_of_variance.calc_sample_num(df_of_all_samples, label_of_all_samples, total_sample_num)

        ### calculate total variance ###
        '''
        Calculate within_variance: variance (float) list of each category 
        Args:
           df_of_each_group: DataFrame of each category
           label_of_each_group: string list. label of each category
        Example:
           within_variance: [58.222222222222214, 50.666666666666664, 50.666666666666664, 56.222222222222214, 56.222222222222214, 59.55555555555555]
        '''
        within_variance = []
        for i in range(len(label_of_each_group)):
            within_variance.append(self.calculate_variance.calc_variance(df_of_each_group, label_of_each_group[i]))
        '''
        Calculate factor1_variance: variance (float) list of factor1 
        Args:
           df_factor1: DataFrame of factor1
           label_of_factor1: string list. label of factor1
        Example:
           factor1_variance: [69.87654320987652, 57.95061728395062]
        '''
        factor1_variance = []
        for i in range(len(label_factor1)):
            factor1_variance.append(self.calculate_variance.calc_variance(df_factor1, label_factor1[i]))
        '''
        Calculate factor2_variance: variance (float) list of factor2 
        Args:
           df_factor2: DataFrame of factor2
           label_of_factor2: string list. label of factor2
        Example:
           factor2_variance: [69.47222222222221, 54.138888888888886, 57.88888888888888]
        '''
        factor2_variance = []
        for i in range(len(label_factor2)):
            factor2_variance.append(self.calculate_variance.calc_variance(df_factor2, label_factor2[i]))
        '''
        Calculate variance_of_all: variance (float) of all samples
        Args:
           df_of_all_samples: DataFrame of all samples
           label_of_all_samples: string list. Normally, ["all"].
        Example:
           variance_of_all: 64.024691358
        '''
        variance_of_all = self.calculate_variance.calc_variance(df_of_all_samples, label_of_all_samples)

        ### calculate sum of squares ###
        '''
        Calculate sum_of_squares_of_others: total sum of squares (float) of others 
        Args:
           sample_num_per_group: calculated from "calculate sample nums" (float list)
           within_variance: calculated from "calculate variance" (float list) 
        Example:
           sum_of_squares_of_others: 4973.33333333 
        '''
        sum_of_squares_of_others = 0.0
        for i in range(len(label_of_each_group)):
            sum_of_squares_of_others += self.analysis_of_variance.calc_sum_of_squares(within_variance[i], sample_num_per_group[i])
        '''
        Calculate sum_of_squares_of_each_group: total sum of squares (float) of each group 
        Args:
           sample_num_per_group: calculated from "calculate sample nums" (float list)
           average_of_all: float.
           within_variance: calculated from "calculate variance" (float list) 
        Example:
           sum_of_squares_of_each_group: 788.888888889
        '''
        sum_of_squares_of_each_group = 0.0
        for i in range(len(label_of_each_group)):
            sum_of_squares_of_each_group += math.pow((within_average[i] - average_of_all), 2) * sample_num_per_group[i]
        '''
        Calculate sum_of_squares_of_factor1: total sum of squares (float) of factor1
        Args:
           sample_num_per_factor1: calculated from "calculate sample nums" (float list)
           average_of_all: float.
           factor1_variance: calculated from "calculate variance" (float list) 
        Example:
           sum_of_squares_of_factor1: 10.0
        '''
        sum_of_squares_of_factor1 = 0.0
        for i in range(len(label_factor1)): 
            sum_of_squares_of_factor1 += math.pow((factor1_average[i] - average_of_all), 2) * sample_num_per_factor1[i]
        '''
        Calculate sum_of_squares_of_factor2: total sum of squares (float) of factor2
        Args:
           sample_num_per_factor2: calculated from "calculate sample nums" (float list)
           average_of_all: float.
           factor2_variance: calculated from "calculate variance" (float list) 
        Example:
           sum_of_squares_of_factor2: 317.222222222 
        '''
        sum_of_squares_of_factor2 = 0.0
        for i in range(len(label_factor2)):
            sum_of_squares_of_factor2 += math.pow((factor2_average[i] - average_of_all), 2) * sample_num_per_factor2[i]
        '''
        Calculate sum_of_squares_of_interaction: total sum of squares (float) of interaction of factor1 and factor2
        Args:
           sum_of_squares_of_each_group: float
           sum_of_squares_of_factor1: float
           sum_of_squares_of_factor2: float
        Example:
           sum_of_squares_of_interaction: 461.666666667
        '''
        sum_of_squares_of_interaction = sum_of_squares_of_each_group - sum_of_squares_of_factor1 - sum_of_squares_of_factor2
        
        ### calculate dof ###
        '''
        Calculate dof_of_factor1: dof (float) of factor1 
        Args:
           sample_num_per_factor1: calculated from "calculate sample nums"
        Example:
           dof_of_factor1: 1.0
        '''
        dof_of_factor1 = len(sample_num_per_factor1) - 1.0
        '''
        Calculate dof_of_factor2: dof (float) of factor2 
        Args:
           sample_num_per_factor2: calculated from "calculate sample nums"
        Example:
           dof_of_factor2: 2.0
        '''
        dof_of_factor2 = len(sample_num_per_factor2) - 1.0
        '''
        Calculate dof_of_interaction: dof (float) of interaction 
        Args:
           dof_of_factor1
           dof_of_factor2
        Example:
           dof_of_interaction: 2.0
        '''
        dof_of_interaction = dof_of_factor1 * dof_of_factor2
        '''
        Calculate dof_of_all: total dof (float) of each category num 
        Args:           
           total_sample_num: args (float list)
        Example:
           dof_of_all: 89.0
        '''
        dof_of_all = total_sample_num[0] - 1.0
        '''
        Calculate dof_of_others: dof (float) of others 
        Args:
           dof_of_all:
           dof_of_factor1:
           dof_of_factor2:
           dof_of_interaction:
        Example:
           dof_of_others: 84.0
        '''
        dof_of_others = dof_of_all - dof_of_factor1 - dof_of_factor2 - dof_of_interaction

        ### calculate sum of squares ###
        '''
        Calculate mean_square_of_factor1: mean_square (float) of factor1
        Args:           
           sum_of_squares_of_factor1: calculated from "calculate sum of squares" (float)
           dof_of_factor1: calculated from "calculate dof" (float)
        Example:
           mean_square_of_factor1: 10.0
        '''
        mean_square_of_factor1 = 0.0
        mean_square_of_factor1 = self.analysis_of_variance.calc_mean_square(sum_of_squares_of_factor1, dof_of_factor1)
        '''
        Calculate mean_square_of_factor2: mean_square (float) of factor2
        Args:           
           sum_of_squares_of_factor2: calculated from "calculate sum of squares" (float)
           dof_of_factor1: calculated from "calculate dof" (float)
        Example:
           mean_square_of_factor2: 158.611111111
        '''
        mean_square_of_factor2 = 0.0        
        mean_square_of_factor2 = self.analysis_of_variance.calc_mean_square(sum_of_squares_of_factor2, dof_of_factor2)
        '''
        Calculate mean_square_of_interaction: mean_square (float) of interaction
        Args:           
           sum_of_squares_of_interaction: calculated from "calculate sum of squares" (float)
           dof_of_interaction: calculated from "calculate dof" (float)
        Example:
           mean_square_of_interaction: 230.833333333
        '''        
        mean_square_of_interaction = 0.0
        mean_square_of_interaction = self.analysis_of_variance.calc_mean_square(sum_of_squares_of_interaction, dof_of_interaction)
        '''
        Calculate mean_square_of_others: mean_square (float) of others
        Args:           
           sum_of_squares_of_others: calculated from "calculate sum of squares" (float)
           dof_of_others: calculated from "calculate dof" (float)
        Example:
           mean_square_of_others: 59.2063492063
        '''
        mean_square_of_others = 0.0
        mean_square_of_others = self.analysis_of_variance.calc_mean_square(sum_of_squares_of_others, dof_of_others)

        ### calculate F ###
        '''
        Calculate F_of_factor1 value. (float)
        Args:
           mean_square_of_factor1: calculated from "calculate mean square" (float)
           mean_square_of_others: calculated from "calculate mean square" (float)
        Example: 
           F_of_factor1: 0.16890080429
        '''
        F_of_factor1 = self.analysis_of_variance.calc_F(mean_square_of_factor1, mean_square_of_others)
        '''
        Calculate F_of_factor2 value. (float)
        Args:
           mean_square_of_factor2: calculated from "calculate mean square" (float)
           mean_square_of_others: calculated from "calculate mean square" (float)
        Example: 
           F_of_factor2: 2.67895442359
        '''
        F_of_factor2 = self.analysis_of_variance.calc_F(mean_square_of_factor2, mean_square_of_others)
        '''
        Calculate F_of_interaction value. (float)
        Args:
           mean_square_of_interaction: calculated from "calculate mean square" (float)
           mean_square_of_others: calculated from "calculate mean square" (float)
        Example: 
           F_of_interaction: 3.89879356568
        '''
        F_of_interaction = self.analysis_of_variance.calc_F(mean_square_of_interaction, mean_square_of_others)

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
