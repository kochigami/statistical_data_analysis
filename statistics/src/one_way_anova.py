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
            within_dof += self.analysis_of_variance.calc_dof(len(df[label_of_each_group[i]]))

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
        
        show_table_df = DataFrame (index=list("123"), columns=[])
        show_table_df['Sum of Squares'] = [float(between_sum_of_squares), float(within_sum_of_squares), float(within_sum_of_squares) + float(between_sum_of_squares)]
        show_table_df['DOF'] = [float(between_dof), float(within_dof), float(within_dof) + float(between_dof)]
        show_table_df['Mean Square'] = [float(between_mean_square), float(within_mean_square), ""]
        show_table_df['F'] = [float(F), "", ""]
        show_table_df.index = ['Between', 'Within', 'Total']
        
        self.analysis_of_variance.matplotlib_table(show_table_df)

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
