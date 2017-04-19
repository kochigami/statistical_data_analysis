#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import DataFrame
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import math
from texttable import Texttable

def main(data, label, factor1, factor2,  condition):
    sample_sum_of_each_category_sum = []
    #[0.0 for i in range(9)] # 9
    sample_sum_of_each_category_average = []
    sample_sum_of_each_category_variance = []
    sample_num_of_each_category = []
    
    for i in range(len(label)):
        sample_sum_of_each_category_sum.append(df[label[i]].mean())
        sample_num_of_each_category.append(len(df[label[i]]))

    sample_sum_of_each_category_sum.append((df[label[0]].sum() + df[label[1]].sum()) / (float (len(df[label[0]]) + len(df[label[1]]))))
    sample_sum_of_each_category_sum.append((df[label[2]].sum() + df[label[3]].sum()) / (float (len(df[label[2]]) + len(df[label[3]]))))
    sample_sum_of_each_category_sum.append((df[label[0]].sum() + df[label[2]].sum()) / (float (len(df[label[0]]) + len(df[label[2]]))))
    sample_sum_of_each_category_sum.append((df[label[1]].sum() + df[label[3]].sum()) / (float (len(df[label[1]]) + len(df[label[3]]))))
    sample_sum_of_each_category_sum.append((df[label[0]].sum() + df[label[1]].sum() + df[label[2]].sum() + df[label[3]].sum()) / 
                                           (float (len(df[label[0]]) + len(df[label[1]]) + len(df[label[2]]) + len(df[label[3]]))))

    sample_num_of_each_category.append(len(df[label[0]]) + len(df[label[1]]))
    sample_num_of_each_category.append(len(df[label[2]]) + len(df[label[3]]))
    sample_num_of_each_category.append(len(df[label[0]]) + len(df[label[2]]))
    sample_num_of_each_category.append(len(df[label[1]]) + len(df[label[3]]))
    sample_num_of_each_category.append(len(df[label[0]]) + len(df[label[1]]) + len(df[label[2]]) + len(df[label[3]]))

    ### calculate total variance ###
    condition1 = []
    condition2 = []
    condition3 = []
    condition4 = []
    
    for i in range(len(label)):
        sample_sum_of_each_category_variance.append(df[label[i]].var(ddof=False))

    for i in range(len(df[label[0]])):
        condition1.append(df[label[0]][i])
    for i in range(len(df[label[1]])):
        condition1.append(df[label[1]][i])

    for i in range(len(df[label[2]])):
        condition2.append(df[label[2]][i])
    for i in range(len(df[label[3]])):
        condition2.append(df[label[3]][i])

    for i in range(2): # condition
        for j in range(len(df[label[2 * i]])):
            condition3.append(df[label[2 * i]][j])
        for k in range(len(df[label[2 * i + 1]])):
            condition4.append(df[label[2 * i + 1]][k])

    sample_sum_of_each_category_variance.append(np.var(condition1))
    sample_sum_of_each_category_variance.append(np.var(condition2))
    sample_sum_of_each_category_variance.append(np.var(condition3))
    sample_sum_of_each_category_variance.append(np.var(condition4))
    sample_sum_of_each_category_variance.append(np.var(df[label].values.flatten()))
    
    # print sample_sum_of_each_category_variance
    
    ### calculate sum of squares ###
    between_sum_of_squares = []
    for i in range(len(label)):
        between_sum_of_squares.append(sample_sum_of_each_category_variance[i] * len(df[label[i]]))
 
    between_sum_of_squares.append(sample_sum_of_each_category_variance[condition * len(label)] * len(df[label]) * len(label))
    # print between_sum_of_squares
        

    ### calculate difference of factor1 ###
    difference_of_factor1 = 0.0
    difference_of_factor1 = math.pow((sample_sum_of_each_category_sum[4] - sample_sum_of_each_category_sum[8]), 2) * sample_num_of_each_category[4] + math.pow((sample_sum_of_each_category_sum[5] - sample_sum_of_each_category_sum[8]), 2) * sample_num_of_each_category[5]
    # print difference_of_factor1

    ### calculate difference of factor2 ###
    difference_of_factor2 = 0.0
    difference_of_factor2 = math.pow((sample_sum_of_each_category_sum[6] - sample_sum_of_each_category_sum[8]), 2) * sample_num_of_each_category[6] + math.pow((sample_sum_of_each_category_sum[7] - sample_sum_of_each_category_sum[8]), 2) * sample_num_of_each_category[7]
    # print difference_of_factor2

    ### calculate difference of interaction ###
    difference_of_each_group = 0.0
    for i in range(len(label)):
        difference_of_each_group += math.pow((sample_sum_of_each_category_sum[i] - sample_sum_of_each_category_sum[8]), 2) * len(df[label[i]]) 

    # print difference_of_each_group
    
    difference_of_interaction = 0.0
    difference_of_interaction = difference_of_each_group - difference_of_factor1 - difference_of_factor2
    # print difference_of_interaction

    ### calculate difference_of_others
    difference_of_others = 0.0
    for i in range(4):
        difference_of_others += between_sum_of_squares[i]
    # print difference_of_others
    
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
                    ["Factor1 (" + str(factor1_name) + ")", str(difference_of_factor1), str(1), str(difference_of_factor1 / 1.0), str((difference_of_factor1 / 1.0) / ((difference_of_others / (total_num -1 -1 -1 -1))))],
                    ["Factor2 ("+ str(factor2_name) + ")", str(difference_of_factor2), str(1), str(difference_of_factor2 / 1.0), str((difference_of_factor2 / 1.0) / (difference_of_others / (total_num -1 -1 -1 -1)))],
                    ["Interaction", str(difference_of_interaction), str(1), str(difference_of_interaction / 1.0), str((difference_of_interaction / 1.0) / (difference_of_others / (total_num -1 -1 -1 -1)))],
                    ["Others", str(difference_of_others), str(total_num -1 -1 -1 -1), str(difference_of_others / (total_num -1 -1 -1 -1)), ""],
                    ["Total", str(between_sum_of_squares[4]), str(total_num -1), "", ""]])
    
    print table.draw()

    # print "one-way anova F value: " + str(F) + "\n degree of freedom between group: " + str(between_dof) + "\n degree of freedom within group: " + str(within_dof)     


if __name__ == '__main__':
    data = {'Crispy-hot':  [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
            'Crispy-mild': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
            'Normal-hot' : [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
            'Normal-mild' : [70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]
    }

    df = DataFrame(data, index = [str(i+1)  for i  in np.arange(15)]) # must change the length of array

    main(df, ['Crispy-hot', 'Crispy-mild', 'Normal-hot', 'Normal-mild'], "Texture", "Flavor", 2)

