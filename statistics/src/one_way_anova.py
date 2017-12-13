#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
import math
from scipy.stats import t as calc_p
# referenced as calc_p because of the error below:
# File "/home/kochigami/my_tutorial/statistics/src/t_test/t_test.py", line 80, in unpaired_ttest
# p = t.sf(t_value, dof)
# UnboundLocalError: local variable 't' referenced before assignment
# t test

class OneWayAnova:
    '''
    data = {'Japanese': [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
            'English':  [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
            'French' :  [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75]}
    mode: string. between or within.
    '''
    def one_way_anova(self, data, mode="one-factor-repeated", threshold=0.05, comparison_mode="holm"):
        # if mode is within test, sample num should be same in each category
        if mode == "one-factor-factorical":
            for i in range(len(data.keys()) - 1):
                if len(data[(data.keys())[i]]) != len(data[(data.keys())[i+1]]):
                    print "Be sure that sample num of each category is same."
                    sys.exit()

        if mode == "one-factor-repeated":
            """
                   | sum of squares |     dof     |    mean squares    |          F            |      
            ------------------------------------------------------------------------------------
            gunkan | ss_between     | between_dof | mean_square_between| ms_between/ ms_within |
            gunnai | ss_within      | within_dof  | mean_square_within |                       |
            -------|----------------------------------------------------------------------------
            total  | ss_b+ss_w      | b_dof+w_dof | 
            """
            
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

            # calculate ss_total (sum of squares per total samples)
            ss_total = 0.0
            for i in range(len(data.keys())):
                for j in range(len(data[(data.keys())[i]])):
                    ss_total += pow(((data[(data.keys())[i]])[j] - total_average), 2.0)

            # calculate ss_between (sum of squares per category)
            ss_between = 0.0
            for i in range(len(data.keys())):
                ss_between += pow((average_per_group[i] - total_average), 2.0) * len(data[(data.keys())[i]])

            # calculate ss_within (sum of squares per category)
            ss_within = ss_total - ss_between

            # calculate dof
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
            self.comparison(data, mean_square_between, between_dof, threshold, comparison_mode)
            return answer_list

        elif mode == "one-factor-factorical":
            """
                   | sum of squares |   dof       |     mean squares    |                   F                    |       
            ------------------------------------------------------------------------------------------------------
            youin  | ss_between     | between_dof | mean_square_between | mean_square_between/ mean_square_error |
            subject| ss_subject     | subject_dof | mean_square_subject |                                        |
            error  | ss_error       | error_dof   | mean_square_error   |                                        |
            ------------------------------------------------------------------------------------------------------
            Total  | ss_b+s+e       | b+s+e_dof   | 
            """
            
            # calculate total
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
            x = pow(x, 2.0) / (len(data.keys()) * len(data[(data.keys())[0]]))

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
            self.comparison(data, mean_square_between, between_dof, threshold, comparison_mode)
            return answer_list

        else:
            print "Please choose mode 'one-factor-repeated' or 'one-factor-factorical'."
            return False

    def comparison(self, data, mean_square_between, between_dof, threshold=0.05, mode="holm"):
        """
        if data.keys() = [A, B, C, D]
        order of comparison:
        1. A vs B
        2. A vs C
        3. A vs D
        4. B vs C
        5. B vs D
        6. C vs D
        order of result:
        [1, 2, 3, 4, 5, 6]
        """
        average_per_group = []
        sample_num_per_group = []
        pair_of_keys = [] 
        t_per_group = []
        p_per_group = []
        modified_pair_of_keys = []
        modified_p_per_group = []
        modified_threshold = []
        results = []

        for i in range(len(data.keys())):
            average_per_group.append(np.mean(data[(data.keys())[i]]))
            sample_num_per_group.append(len(data[(data.keys())[i]]))
        
        for i in range(len(data.keys())):
            for j in range(i+1, len(data.keys())):
                pair_of_keys.append((data.keys())[i] + " + " + (data.keys())[j])
                t_per_group.append(abs(average_per_group[i] - average_per_group[j]) / math.sqrt(mean_square_between * ((1.0 / sample_num_per_group[i]) + (1.0 / sample_num_per_group[j]))))
        for i in range(len(t_per_group)):
            p_per_group.append(calc_p.sf(t_per_group[i], between_dof))

        for i in range(len(t_per_group)):
            if mode == "bonferroni":
                modified_threshold.append(threshold / len(t_per_group))
            elif mode == "holm":
                modified_threshold.append(threshold / (len(t_per_group) - i))
            else:
                print "Please choose bonferroni or holm."
                sys.exit()

        if mode == "holm":
            modified_p_per_group = sorted(p_per_group)
            for i in range(len(t_per_group)):
                for j in range(len(t_per_group)):
                    if modified_p_per_group[i] == p_per_group[j]:
                        modified_pair_of_keys.append(pair_of_keys[j])

        for i in range(len(t_per_group)):
            if mode == "bonferroni":
                if modified_threshold[i] > p_per_group[i]:
                    results.append("o ")
                else:
                    results.append("x ")
            if mode == "holm":
                if modified_threshold[i] > modified_p_per_group[i]:
                    results.append("o ")
                else:
                    results.append("x ")
                break

        if mode == "bonferroni":
            print "pair of comparison: " + str(pair_of_keys)
        elif mode == "holm":
            print "pair of comparison: " + str(modified_pair_of_keys)
        
        print "threshold: " + str(modified_threshold)
        
        if mode == "bonferroni":
            print "p list: " + str(p_per_group)
        elif mode == "holm":
            print "modified p list: " + str(modified_p_per_group)
            print "Note: "
        
        print "comparison: " + str(results)

if __name__ == '__main__':
    pass
