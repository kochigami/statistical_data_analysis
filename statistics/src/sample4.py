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

def calc_sum_of_squares(df, label, sample_sum_of_each_category_average, sample_sum_of_each_category_variance):
    ### calculate sum of squares ###
    between_sum_of_squares = []
    for i in range(len(label)):
        between_sum_of_squares.append(sample_sum_of_each_category_variance[i] * len(df[label[i]]))
 
    between_sum_of_squares.append(sample_sum_of_each_category_variance[len(sample_sum_of_each_category_average) - 1] * len(df[label]) * len(label)) # total
    #print between_sum_of_squares
    return between_sum_of_squares

def calc_difference_of_factor1(condition_number_of_factor1, sample_sum_of_each_category_average, sample_num_of_each_category, label):
    ### calculate difference of factor1 ###
    difference_of_factor1 = 0.0
    for i in range(condition_number_of_factor1):
        difference_of_factor1 += math.pow((sample_sum_of_each_category_average[len(label) + i] - sample_sum_of_each_category_average[len(sample_sum_of_each_category_average) - 1]), 2) * sample_num_of_each_category[len(label) + i] 
    return difference_of_factor1

def calc_difference_of_factor2(condition_number_of_factor1, sample_sum_of_each_category_average, sample_num_of_each_category, label):
    ### calculate difference of factor2 ###
    difference_of_factor2 = 0.0
    for i in range(len(label) / condition_number_of_factor1):
        difference_of_factor2 += math.pow((sample_sum_of_each_category_average[len(label) + condition_number_of_factor1 + i] - sample_sum_of_each_category_average[len(sample_sum_of_each_category_average) - 1]), 2) * sample_num_of_each_category[len(label) + condition_number_of_factor1 + i]
    return difference_of_factor2

def calc_difference_of_each_group(df, sample_sum_of_each_category_average, label):
    ### calculate difference of interaction ###
    difference_of_each_group = 0.0
    for i in range(len(label)):
        difference_of_each_group += math.pow((sample_sum_of_each_category_average[i] - sample_sum_of_each_category_average[len(sample_sum_of_each_category_average) - 1]), 2) * len(df[label[i]]) 
    return difference_of_each_group
    
def calc_difference_of_interaction(difference_of_each_group, difference_of_factor1, difference_of_factor2):
    difference_of_interaction = 0.0
    difference_of_interaction = difference_of_each_group - difference_of_factor1 - difference_of_factor2
    return difference_of_interaction

def calc_difference_of_others(sample, between_sum_of_squares):
    ### calculate difference_of_others
    difference_of_others = 0.0
    for i in range(sample * 2):
        difference_of_others += between_sum_of_squares[i]
    return difference_of_others

def show_table(df, label, factor1, factor2, condition_number_of_factor1, difference_of_factor1, difference_of_factor2, difference_of_interaction, difference_of_others, between_sum_of_squares):
    ### show a table ###
    total_num = 0
    for i in range(len(label)):
        total_num += len(df[label[i]])
    # print total_num

    table = Texttable()

    factor1_name = factor1
    factor2_name = factor2


    table.set_cols_align(["c", "c", "c", "c", "c"])
    table.set_cols_valign(["m", "m", "m", "m", "m"])
    table.add_rows([["Factor", "Sum of Squares", "Dof", "Mean Square", "F"], 
                    ["Factor1 (" + str(factor1_name) + ")", str(difference_of_factor1), str(condition_number_of_factor1 - 1), str(difference_of_factor1 / (condition_number_of_factor1 - 1.0)), str((difference_of_factor1 / (condition_number_of_factor1 - 1.0)) / ((difference_of_others / (total_num - (condition_number_of_factor1 - 1) - (len(label) / condition_number_of_factor1 -1) -1))))],
                    ["Factor2 ("+ str(factor2_name) + ")", str(difference_of_factor2), str((len(label) / condition_number_of_factor1) - 1), str(difference_of_factor2 / (len(label) / condition_number_of_factor1) - 1), str((difference_of_factor2 / 1.0) / (difference_of_others / (total_num - (condition_number_of_factor1 - 1) - (len(label) / condition_number_of_factor1 -1) -1)))],
                    ["Interaction", str(difference_of_interaction), str((condition_number_of_factor1 - 1.0) * ((len(label) / condition_number_of_factor1) - 1)), str(difference_of_interaction / ((condition_number_of_factor1 - 1.0) * ((len(label) / condition_number_of_factor1) - 1))), str((difference_of_interaction / ((condition_number_of_factor1 - 1.0) * ((len(label) / condition_number_of_factor1) - 1))) / (difference_of_others / (total_num - (condition_number_of_factor1 - 1) - (len(label) / condition_number_of_factor1 -1) -1)))],
                    ["Others", str(difference_of_others), str(total_num - (condition_number_of_factor1 - 1) - ((len(label) / condition_number_of_factor1) - 1) - ((condition_number_of_factor1 - 1.0) * ((len(label) / condition_number_of_factor1) - 1))  -1), str(difference_of_others / (total_num - (condition_number_of_factor1 - 1) - (len(label) / condition_number_of_factor1 -1) -1)), ""],
                    ["Total", str(between_sum_of_squares[len(between_sum_of_squares) - 1]), str(total_num -1), "", ""]])
    
    print table.draw()

def obtain_df (data):
    return DataFrame(data, index = [str(i+1) for i in np.arange(len(data[(data.keys())[0]])) ])

def obtain_condition_number_of_factor2(label, condition_number_of_factor1):
    return len(label) / condition_number_of_factor1

def main(data, label, factor1, factor2, condition_number_of_factor1):
    df = obtain_df(data)
    
    ## sample: condition_number_of_factor2 ##
    sample = obtain_condition_number_of_factor2(label, condition_number_of_factor1)

    sample_sum_of_each_category_average = []
    sample_sum_of_each_category_variance = []
    sample_num_of_each_category = []
    
    calculate_average = CalculateAverage()
    sample_sum_of_each_category_average, sample_num_of_each_category = calculate_average.calc_average(df, label, condition_number_of_factor1)
    
    calculate_variance = CalculateVariance()
    sample_sum_of_each_category_variance = calculate_variance.calc_variance(df, label, condition_number_of_factor1)
        
    between_sum_of_squares = calc_sum_of_squares(df, label, sample_sum_of_each_category_average, sample_sum_of_each_category_variance)

    difference_of_factor1 = calc_difference_of_factor1(condition_number_of_factor1, sample_sum_of_each_category_average, sample_num_of_each_category, label)

    difference_of_factor2 = calc_difference_of_factor2(condition_number_of_factor1, sample_sum_of_each_category_average, sample_num_of_each_category, label)

    difference_of_each_group = calc_difference_of_each_group(df, sample_sum_of_each_category_average, label)

    difference_of_interaction = calc_difference_of_interaction(difference_of_each_group, difference_of_factor1, difference_of_factor2)

    difference_of_others = calc_difference_of_others(sample, between_sum_of_squares)
    
    show_table(df, label, factor1, factor2, condition_number_of_factor1, difference_of_factor1, difference_of_factor2, difference_of_interaction, difference_of_others, between_sum_of_squares)

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

    main(data, ['Crispy-hot', 'Crispy-normal', 'Crispy-mild', 'Normal-hot', 'Normal-normal', 'Normal-mild'], "Texture", "Flavor", 2)
    #main(data, ['Crispy-hot', 'Crispy-mild', 'Normal-hot', 'Normal-mild'], "Texture", "Flavor", 2, 2)
