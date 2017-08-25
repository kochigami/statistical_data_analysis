#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import math

class OneWayAnova:
    '''
    data = {'Japanese': [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
            'English':  [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
            'French' :  [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75]}
    mode: string. between or within.
    '''
    def one_way_anova(self, data, mode="between"):
        # sample num should be same in each category
        if mode == "within":
            for i in range(len(data.keys()) - 1):
                if len(data[(data.keys())[i]]) != len(data[(data.keys())[i+1]]):
                    print "Be sure that sample num of each category is same."
                    return False

        if mode == "between":
            # calculate total average
            total_average = 0.0
            total_sample_num = 0.0
            for i in range(len(data.keys())):
                total_sample_num += len(data[(data.keys())[i]])
                for j in range(len(data[(data.keys())[i]])):
                    total_average += (data[(data.keys())[i]])[j]
            total_average = total_average / total_sample_num

            # calculate average per category
            average_per_group = []
            for i in range(len(data.keys())):
                average_per_group.append(np.mean(data[(data.keys())[i]]))

            # calculate sum of squares
            ss_total = 0.0
            for i in range(len(data.keys())):
                for j in range(len(data[(data.keys())[i]])):
                    ss_total += pow(((data[(data.keys())[i]])[j] - total_average), 2.0)

            ss_between = 0.0
            for i in range(len(data.keys())):
                ss_between += pow((average_per_group[i] - total_average), 2.0) * len(data[(data.keys())[i]])

            ss_within = ss_total - ss_between

            # calculate dof (group type & sample number of each type)
            between_dof = len(data.keys()) - 1
            total_dof = total_sample_num - 1
            within_dof = total_dof - between_dof

            # calculate mean square
            mean_square_between = ss_between / float(between_dof)
            mean_square_within = ss_within / float(within_dof)

            # calculate F
            F = mean_square_between / mean_square_within

            answer_list = [[math.ceil(ss_between * 100.0) * 0.01, int(between_dof), math.ceil(mean_square_between * 100.0) * 0.01, math.ceil(F * 100.0) * 0.01],
                           [math.ceil(ss_within * 100.0) * 0.01, int(within_dof), math.ceil(mean_square_within * 100.0) * 0.01, '--'], 
                           [math.ceil((ss_between + ss_within) * 100.0) * 0.01, int(between_dof + within_dof),'--', '--']]
            return answer_list

        elif mode == "within":
            # total
            total_S = 0.0
            total_sample_num = 0.0
            for i in range(len(data.keys())):
                total_sample_num += len(data[(data.keys())[i]])
                for j in range(len(data[(data.keys())[i]])):
                    total_S += pow((data[(data.keys())[i]])[j], 2.0)

            # each category
            category_S = 0.0
            for i in range(len(data.keys())):
                category_S += pow(sum(data[(data.keys())[i]]), 2.0) / len(data[(data.keys())[i]])
            
            # each subject
            # sample num should be same in each category
            # that's why checking array length at first code
            subject_S = 0.0
            subject_S_tmp = 0.0
            target_num = 0
            count = 0
            for i in range(len(data[(data.keys())[0]])):
                for j in range(len(data.keys())):
                    if i == target_num:
                        subject_S_tmp += (data[(data.keys())[j]])[i]
                        count += 1
                    if count == len(data.keys()):
                        subject_S += pow(subject_S_tmp, 2.0) / len(data.keys())
                        count = 0
                        target_num += 1
                        subject_S_tmp = 0.0

            # calculate x (correction term)
            x = 0.0
            for i in range(len(data.keys())):
                x += sum(data[(data.keys())[i]])
            x = pow(x, 2.0) / (len(data.keys()) * len(data[(data.keys())[i]]))

            # calculate sum of squares
            ss_total = total_S - x
            ss_between = category_S - x
            ss_subject = subject_S - x
            ss_error = ss_total - ss_between - ss_subject

            # calculate dof (group type & sample number of each type)
            between_dof = len(data.keys()) - 1.0
            subject_dof = len(data[(data.keys())[0]]) - 1.0
            error_dof =  total_sample_num - 1 - between_dof - subject_dof

            # calculate mean square
            mean_square_between = ss_between / between_dof
            mean_square_subject = ss_subject / subject_dof            
            mean_square_error = ss_error / error_dof

            # calculate F
            F = mean_square_between / mean_square_error

            answer_list = [[math.ceil(ss_between * 100.0) * 0.01, int(between_dof), math.ceil(mean_square_between * 100.0) * 0.01, math.ceil(F * 100.0) * 0.01],
                           [math.ceil(ss_subject * 100.0) * 0.01, int(subject_dof), math.ceil(mean_square_subject * 100.0) * 0.01, '--'],
                           [math.ceil(ss_error * 100.0) * 0.01, int(error_dof), math.ceil(mean_square_error * 100.0) * 0.01, '--'],
                           [math.ceil(ss_total * 100.0) * 0.01, int(between_dof + subject_dof + error_dof),'--', '--']]
            return answer_list

        else:
            print "Please choose mode 'between' or 'within'."
            return False

if __name__ == '__main__':
    pass
