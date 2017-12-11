#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import math

class TwoWayAnova:
    '''
    data = {'NAO-Adult':       [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
            'NAO-Children':    [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
            'Pepper-Adult':    [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
            'Pepper-Children': [60, 85, 85, 80, 85, 90, 95, 90, 95, 85, 85, 80, 85, 80, 85]}
    label_A: string list. ex: ["NAO", "Pepper"]
    label_B: string list. ex: ["Adult", "Children"]
    mode: string. two-factor-repeated.
    '''
    def two_way_anova(self, data, label_A, label_B, mode="two-factor-repeated"):
        if mode == "two-factor-repeated":            

            """
                         | ss         |   dof           |   ms     |         F        |       
            -------------------------------------------------------------------------
            youin1       | ss_1       | category1_dof   | ms_1     | ms_1/ ms_error   |
            youin2       | ss_2       | category2_dof   | ms_2     | ms_2/ ms_error   |
            youin1xyouin2| ss_1x2     | category1x2_dof | ms_1x2   | ms_1x2/ ms_error |
            error        | ss_error   |     error_dof   | ms_error |                  |
            -------------------------------------------------------------------------
            Total        |ss_1+2+1x2+e| 1+2+1x2+e_dof   | 
            """

            """
                           | youin2-A | youin2-B | youin2-C |   Total  |       
            ------------------------------------------------------------
            youin1-A       |  130     |    340   |  340     |    810   |
            youin1-B       |  140     |     56   |  125     |    321   |
            ------------------------------------------------------------
            Total          |  270     |    396   |  465     |   1131   |
            """

            total_ss = 0.0
            total_sum = 0.0

            # total ss
            # total sum
            for i in range(len(data.keys())):
                for j in range(len(data[(data.keys()[i])])):
                    total_ss += pow((data[(data.keys()[i])])[j], 2.0)
                    total_sum += (data[(data.keys()[i])])[j] ##

            category1_sum = []
            category1_num = []
            category1_sum_tmp = 0.0
            category1_num_tmp = 0.0
            # category1 sum
            for i in range(len(label_A)):
                for j in range(len(data.keys())):
                    if label_A[i] in (data.keys())[j]:
                        category1_sum_tmp += sum(data[(data.keys())[j]])
                        category1_num_tmp += len(data[(data.keys())[j]])
                category1_sum.append(category1_sum_tmp)
                category1_sum_tmp = 0.0
                category1_num.append(category1_num_tmp)
                category1_num_tmp = 0
                    
            # category2 sum
            category2_sum = []
            category2_num = []
            category2_sum_tmp = 0.0
            category2_num_tmp = 0.0
            for i in range(len(label_B)):
                for j in range(len(data.keys())):
                    if label_B[i] in (data.keys())[j]:
                        category2_sum_tmp += sum(data[(data.keys())[j]])
                        category2_num_tmp += len(data[(data.keys())[j]])
                category2_sum.append(category2_sum_tmp)
                category2_sum_tmp = 0.0
                category2_num.append(category2_num_tmp)
                category2_num_tmp = 0

            # preparation
            # category1 preparation
            category1_preparation = 0.0
            for i in range(len(category1_sum)):
                category1_preparation += pow(category1_sum[i], 2.0) / category1_num[i]

            # category2 preparation
            category2_preparation = 0.0
            for i in range(len(category2_sum)):
                category2_preparation += pow(category2_sum[i], 2.0) / category2_num[i]

            # category1x2 preparation
            category1x2_preparation = 0.0
            for i in range(len(data.keys())):
                category1x2_preparation += pow(sum(data[(data.keys())[i]]), 2.0) / float(len(data[(data.keys())[i]]))
            
            # calculate x (correction term)
            x = 0.0                
            total_num = 0
            for i in range(len(data.keys())):
                x += sum(data[(data.keys())[i]])
                total_num += len(data[(data.keys())[i]])

            x = pow(x, 2.0) / float(total_num)

            ss_1 = category1_preparation - x
            ss_2 = category2_preparation - x
            ss_1x2 = category1x2_preparation - x - ss_1 - ss_2
            ss_e = total_ss - category1x2_preparation
            ss_t = total_ss - x
        
            # calculate sample nums
            category1_dof = len(label_A) - 1
            category2_dof = len(label_B) - 1
            category1x2_dof = (len(label_A) - 1) * (len(label_B) - 1) 
            error_dof = (total_num - 1) - category1_dof - category2_dof - category1x2_dof

            # calculate mean square
            ms_1 = ss_1 / float(category1_dof)
            ms_2 = ss_2 / float(category2_dof)
            ms_1x2 = ss_1x2 / float(category1x2_dof)
            ms_e = ss_e / float(error_dof)

            # calculate F value
            f_1 = ms_1 / ms_e
            f_2 = ms_2 / ms_e
            f_1x2 = ms_1x2 / ms_e
            
            answer_list = [[math.ceil(ss_1 * 100.0) * 0.01, int(category1_dof), math.ceil(ms_1 * 100.0) * 0.01, math.ceil(f_1 * 100.0) * 0.01],
                           [math.ceil(ss_2 * 100.0) * 0.01, int(category2_dof), math.ceil(ms_2 * 100.0) * 0.01, math.ceil(f_2 * 100.0) * 0.01],
                           [math.ceil(ss_1x2 * 100.0) * 0.01, int(category1x2_dof), math.ceil(ms_1x2 * 100.0) * 0.01, math.ceil(f_1x2 * 100.0) * 0.01],
                           [math.ceil(ss_e * 100.0) * 0.01, int(error_dof), math.ceil(ms_e * 100.0) * 0.01, '--'], 
                           [math.ceil(ss_t * 100.0) * 0.01, int(category1_dof + category2_dof + category1x2_dof + error_dof),'--', '--']]
            return answer_list

if __name__ == '__main__':
    pass
