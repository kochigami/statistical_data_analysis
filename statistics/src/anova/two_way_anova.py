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
    mode: string. between or within.
    '''
    def two_way_anova(self, data, label_A, label_B, mode="between"):
        # sample num should be same in each category
        if mode == "within":
            for i in range(len(data.keys()) - 1):
                if len(data[(data.keys())[i]]) != len(data[(data.keys())[i+1]]):
                    print "Be sure that sample num of each category is same."
                    return False
        if mode == "between":            
            total_ss = 0.0
            total_sum = 0.0
            total_num = 0
            # total ss
            # total sum
            for i in range(len(data.keys())):
                for j in range(len(data[(data.keys()[i])])):
                    total_ss += pow((data[(data.keys()[i])])[j], 2.0)
                    total_sum += (data[(data.keys()[i])])[j]
                    total_num += 1

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
            for i in range(len(data.keys())):
                x += sum(data[(data.keys())[i]])
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

        elif mode == "within":
            # calculate total average
            total_average = 0.0
            total_sample_num = 0.0
            for i in range(len(data.keys())):
                total_sample_num += len(data[(data.keys())[i]])
                for j in range(len(data[(data.keys())[i]])):
                    total_average += (data[(data.keys())[i]])[j]
            total_average = total_average / total_sample_num

            # calculate average per category
            average_per_category = []
            std_per_category = []
            for i in range(len(data.keys())):
                average_per_category.append(np.mean(data[(data.keys())[i]]))
                std_per_category.append(np.std(data[(data.keys())[i]]))

            total_ss_tmp = 0.0
            total_ss = 0.0
            total_sum = 0.0
            total_num = 0
            # total ss
            # total sum
            for i in range(len(data[(data.keys()[0])])):
                for j in range(len(data.keys())):
                    total_ss_tmp += (data[(data.keys())[j]])[i]
                    total_sum += (data[(data.keys())[j]])[i]
                    total_num += 1
                total_ss += pow(total_ss_tmp, 2.0)
                total_ss_tmp = 0.0

            correction_term = pow(total_sum, 2.0) / float(total_num)
            preparation_term = total_ss / float(len(data.keys()))
            ss_subject = preparation_term - correction_term
             
            # ss_1
            ss_1 = 0.0
            ss_1_tmp = 0.0
            ss_1_num_tmp = 0.0
            for i in range(len(label_A)):
                for j in range(len(data.keys())):
                    if label_A[i] in (data.keys())[j]:
                        ss_1_tmp += average_per_category[j] * len(data[(data.keys())[j]])
                        ss_1_num_tmp += len(data[(data.keys())[j]])
                ss_1 += pow(((ss_1_tmp / ss_1_num_tmp) - total_average), 2.0) * ss_1_num_tmp
                ss_1_tmp = 0.0
                ss_1_num_tmp = 0.0

            # ss_2
            ss_2 = 0.0
            ss_2_tmp = 0.0
            ss_2_num_tmp = 0.0
            for i in range(len(label_B)):
                for j in range(len(data.keys())):
                    if label_B[i] in (data.keys())[j]:
                        ss_2_tmp += average_per_category[j] * len(data[(data.keys())[j]])
                        ss_2_num_tmp += len(data[(data.keys())[j]])
                ss_2 += pow(((ss_2_tmp / ss_2_num_tmp) - total_average), 2.0) * ss_2_num_tmp
                ss_2_tmp = 0.0
                ss_2_num_tmp = 0.0

            # ss_1_e
            # sample num should be same in each category
            # that's why checking array length at first code
            category1_sum = 0.0
            category1_sum_tmp = 0.0
            for i in range(len(label_A)):
                for j in range(len(data[(data.keys())[0]])):
                    for k in range(len(data.keys())):
                        if label_A[i] in (data.keys())[k]:
                            category1_sum_tmp += (data[(data.keys())[k]])[j]

                    category1_sum += pow(category1_sum_tmp, 2.0)
                    category1_sum_tmp = 0.0
            ss_1_e = category1_sum / float(len(label_A)) - ss_subject - correction_term - ss_1

            # ss_2_e
            # sample num should be same in each category
            # that's why checking array length at first code
            category2_sum = 0.0
            category2_sum_tmp = 0.0
            for i in range(len(label_B)):
                for j in range(len(data[(data.keys())[0]])):
                    for k in range(len(data.keys())):
                        if label_B[i] in (data.keys())[k]:
                            category2_sum_tmp += (data[(data.keys())[k]])[j]

                    category2_sum += pow(category2_sum_tmp, 2.0)
                    category2_sum_tmp = 0.0
            ss_2_e = category2_sum / float(len(label_B)) - ss_subject - correction_term - ss_2

            # ss_1x2
            total_error = 0.0
            for i in range(len(data.keys())):
                total_error += pow((average_per_category[i] - total_average), 2.0)
            total_error = total_error * len(data[(data.keys())[0]])
            ss_1x2 = total_error - ss_1 - ss_2
            
            # ss_e
            ss_e = 0.0
            for i in range(len(data.keys())):
                ss_e += pow(std_per_category[i], 2.0) * len(data[(data.keys())[i]])
            
            # ss_1x2_e
            ss_1x2_e = ss_e - ss_subject - ss_1_e - ss_2_e

            # calculate dof
            subject_dof = len(data[(data.keys())[0]]) - 1
            category1_dof = len(label_A) - 1
            s_1_dof = subject_dof * category1_dof
            category2_dof = len(label_B) - 1
            s_2_dof = subject_dof * category2_dof
            category1x2_dof = (len(label_A) - 1) * (len(label_B) - 1) 
            s_1x2_dof = subject_dof * category1x2_dof

            # calculate mean square
            ms_s = ss_subject / float(subject_dof)
            ms_1 = ss_1 / float(category1_dof)
            ms_1_e = ss_1_e / float(s_1_dof)
            ms_2 = ss_2 / float(category2_dof)
            ms_2_e = ss_2_e / float(s_2_dof)
            ms_1x2 = ss_1x2 / float(category1x2_dof)
            ms_1x2_e = ss_1x2_e / float(s_1x2_dof)

            # calculate F value
            f_1 = ms_1 / ms_1_e
            f_2 = ms_2 / ms_2_e
            f_1x2 = ms_1x2 / ms_1x2_e
            
            answer_list = [[math.ceil(ss_subject * 100.0) * 0.01, int(subject_dof), math.ceil(ms_s * 100.0) * 0.01, '--'],
                           [math.ceil(ss_1 * 100.0) * 0.01, int(category1_dof), math.ceil(ms_1 * 100.0) * 0.01, math.ceil(f_1 * 100.0) * 0.01],
                           [math.ceil(ss_1_e * 100.0) * 0.01, int(s_1_dof), math.ceil(ms_1_e * 100.0) * 0.01, '--'],
                           [math.ceil(ss_2 * 100.0) * 0.01, int(category2_dof), math.ceil(ms_2 * 100.0) * 0.01, math.ceil(f_2 * 100.0) * 0.01],
                           [math.ceil(ss_2_e * 100.0) * 0.01, int(s_2_dof), math.ceil(ms_2_e * 100.0) * 0.01, '--'],
                           [math.ceil(ss_1x2 * 100.0) * 0.01, int(category1x2_dof), math.ceil(ms_1x2 * 100.0) * 0.01, math.ceil(f_1x2 * 100.0) * 0.01],
                           [math.ceil(ss_1x2_e * 100.0) * 0.01, int(s_1x2_dof), math.ceil(ms_1x2_e * 100.0) * 0.01, '--'],
                           [math.ceil((ss_subject + ss_1 + ss_1_e + ss_2 + ss_2_e + ss_1x2 + ss_1x2_e) * 100.0) * 0.01, int(subject_dof + category1_dof + s_1_dof + category2_dof + s_2_dof + category1x2_dof + s_1x2_dof), '--', '--' ]]
            return answer_list

if __name__ == '__main__':
    pass
