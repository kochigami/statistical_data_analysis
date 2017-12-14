#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
import math
from scipy.stats import t as calc_p
from scipy.stats import f as calc_f
# referenced as calc_p because of the error below:
# File "/home/kochigami/my_tutorial/statistics/src/t_test/t_test.py", line 80, in unpaired_ttest
# p = t.sf(t_value, dof)
# UnboundLocalError: local variable 't' referenced before assignment
# t test
from collections import OrderedDict

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

            # calculate F
            f_1 = ms_1 / ms_e
            f_2 = ms_2 / ms_e
            f_1x2 = ms_1x2 / ms_e

            # calculate p
            p_1 = calc_f.sf(f_1, category1_dof, error_dof)
            p_2 = calc_f.sf(f_2, category2_dof, error_dof)
            p_1x2 = calc_f.sf(f_1x2, category1x2_dof, error_dof)

            # multiple comparison
            if p_1x2 < 0.05:
                # simple major effect
                # 1. label_A
                self.evaluate_simple_main_effect(data, label_A, label_B)
                # 2. label_B
                self.evaluate_simple_main_effect(data, label_B, label_A)

            elif p_1 < 0.05:
               self.evaluate_main_effect(data, label_A, ms_1, category1_dof)

            elif p_2 < 0.05:
                self.evaluate_main_effect(data, label_B, ms_2, category2_dof)

            answer_list = [[math.ceil(ss_1 * 100.0) * 0.01, int(category1_dof), math.ceil(ms_1 * 100.0) * 0.01, math.ceil(f_1 * 100.0) * 0.01, math.ceil(p_1 * 1000.0) * 0.001],
                           [math.ceil(ss_2 * 100.0) * 0.01, int(category2_dof), math.ceil(ms_2 * 100.0) * 0.01, math.ceil(f_2 * 100.0) * 0.01, math.ceil(p_2 * 1000.0) * 0.001],
                           [math.ceil(ss_1x2 * 100.0) * 0.01, int(category1x2_dof), math.ceil(ms_1x2 * 100.0) * 0.01, math.ceil(f_1x2 * 100.0) * 0.01, math.ceil(p_1x2 * 1000.0) * 0.001],
                           [math.ceil(ss_e * 100.0) * 0.01, int(error_dof), math.ceil(ms_e * 100.0) * 0.01, '--', '--'], 
                           [math.ceil(ss_t * 100.0) * 0.01, int(category1_dof + category2_dof + category1x2_dof + error_dof),'--', '--', '--']]
            return answer_list

    def evaluate_main_effect(self, data, label, ms, dof):
        if len(label) > 2:
            data_tmp = OrderedDict()
            for i in range(len(label)):
                data_tmp_tmp = []
                for j in range(len(data.keys())):
                    if label[i] in (data.keys())[j]:
                        data_tmp_tmp += data[(data.keys())[j]]
                data_tmp[label[i]] = data_tmp_tmp
            self.comparison(data_tmp, ms, dof)

    def evaluate_simple_main_effect(self, data, focused_label, dependent_label):
        ## focused_label (label_A)
        ## dependent_label (labelB)
        if len(dependent_label) > 2:
            for i in range(len(focused_label)):
                data_tmp = OrderedDict()
                data_focused_label = OrderedDict()
                data_tmp_tmp = []
                for j in range(len(dependent_label)):
                    for k in range(j+1, len(dependent_label)):
                        average = []
                        # choose pair
                        for l in range(len(data.keys())):
                            if focused_label[i] in (data.keys())[l] and dependent_label[j] in (data.keys())[l]:
                                data_tmp[focused_label[i] + "+" + dependent_label[j]] = data[(data.keys())[l]]
                            if focused_label[i] in (data.keys())[l] and dependent_label[k] in (data.keys())[l]:
                                data_tmp[focused_label[i] + "+" + dependent_label[k]] = data[(data.keys())[l]]
                            if focused_label[i] in (data.keys())[l]:
                                data_tmp_tmp += data[(data.keys())[l]]
                        data_focused_label[focused_label[i]] = data_tmp_tmp
                        print data_focused_label

                        for l in range(len(data_focused_label)):
                            average.append(sum(data_focused_label[(data_focused_label.keys())[l]]) / len(data_focused_label[(data_focused_label.keys())[l]]))
                        
                        whole_sum = 0.0
                        whole_num = 0.0
                        whole_average = 0.0
                        for l in range(len(data_tmp)):
                            whole_sum += sum(data_tmp[(data_tmp.keys())[l]])
                            whole_num += len(data_tmp[(data_tmp.keys())[l]])
                        whole_average = whole_sum / whole_num

                        ms = 0.0
                        for l in range(len(average)):
                            ms += pow((average[l] - whole_average), 2.0) * len(data_focused_label[(data_focused_label.keys())[l]])
                        dof = len(dependent_label) - 1.0
                        ms /= dof
                        self.comparison(data_tmp, ms, dof)
    
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
        
        print "comparison: " + str(results)
        average_per_group = []
        sample_num_per_group = []
        pair_of_keys = [] 
        t_per_group = []
        p_per_group = []
        modified_pair_of_keys = []
        modified_p_per_group = []
        modified_threshold = []
        results = []


if __name__ == '__main__':
    pass
