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
from CRFpq import CRF_pq
from SPFpq import SPF_pq
from RBFpq import RBF_pq

class TwoWayAnova:
    '''
    data = {'NAO-Adult':       [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
            'NAO-Children':    [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
            'Pepper-Adult':    [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
            'Pepper-Children': [60, 85, 85, 80, 85, 90, 95, 90, 95, 85, 85, 80, 85, 80, 85]}
    label_A: string list. ex: ["NAO", "Pepper"]
    label_B: string list. ex: ["Adult", "Children"]
    mode: string. CRFpq, SPFpq, RBFpq.
    '''
    def two_way_anova(self, data, label_A, label_B, mode="CRFpq"):
        if mode == "CRFpq":

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
            crf_pq = CRF_pq()
            is_data_size_equal = True
            for i in range(len(data.keys())):
                if len(data[(data.keys())[0]]) != len(data[(data.keys())[i]]):
                    is_data_size_equal = False

            if is_data_size_equal:
                SSa, SSb, SSaxb, SSwc, SSt, A_dof, B_dof, AxB_dof, WC_dof, MSa, MSb, MSaxb, MSwc, Fa, Fb, Faxb, p_1, p_2, p_1x2 = \
                crf_pq.test(data, label_A, label_B, mode="equal")
                
            else:
                SSa, SSb, SSaxb, SSwc, SSt, A_dof, B_dof, AxB_dof, WC_dof, MSa, MSb, MSaxb, MSwc, Fa, Fb, Faxb, p_1, p_2, p_1x2 = \
                crf_pq.test(data, label_A, label_B, mode="notequal")

            # multiple comparison
            if p_1x2 < 0.05:
                # simple major effect
                # 1. label_A
                self.evaluate_simple_main_effect(data, label_A, label_B)
                # 2. label_B
                self.evaluate_simple_main_effect(data, label_B, label_A)

            elif p_1 < 0.05:
                self.evaluate_main_effect(data, label_A, MSa, A_dof)
                
            elif p_2 < 0.05:
                self.evaluate_main_effect(data, label_B, MSb, B_dof)

            answer_list = [[math.ceil(SSa * 100.0) * 0.01, int(A_dof), math.ceil(MSa * 100.0) * 0.01, math.ceil(Fa * 100.0) * 0.01, math.ceil(p_1 * 1000.0) * 0.001],
                           [math.ceil(SSb * 100.0) * 0.01, int(B_dof), math.ceil(MSb * 100.0) * 0.01, math.ceil(Fb * 100.0) * 0.01, math.ceil(p_2 * 1000.0) * 0.001],
                           [math.ceil(SSaxb * 100.0) * 0.01, int(AxB_dof), math.ceil(MSaxb * 100.0) * 0.01, math.ceil(Faxb * 100.0) * 0.01, math.ceil(p_1x2 * 1000.0) * 0.001],
                           [math.ceil(SSwc * 100.0) * 0.01, int(WC_dof), math.ceil(MSwc * 100.0) * 0.01, '--', '--'],
                           [math.ceil(SSt * 100.0) * 0.01, int(A_dof + B_dof + AxB_dof + WC_dof),'--', '--', '--']]
            return answer_list

        elif mode == "SPFpq":
            spf_pq = SPF_pq()
            # same as CRFpq & size is equal #
            is_data_size_equal = True
            for i in range(len(data.keys())):
                if len(data[(data.keys())[0]]) != len(data[(data.keys())[i]]):
                    is_data_size_equal = False

            if is_data_size_equal:
                SSa, SSsa, SSb, SSaxb, SSbxsa, A_dof, SA_dof, B_dof, AxB_dof, BxSA_dof, MSa, MSsa, MSb, MSaxb, MSbxsa, Fa, Fb, Faxb, p_1, p_2, p_1x2 = \
                spf_pq.test(data, label_A, label_B, mode="equal")
            else:
                SSa, SSsa, SSb, SSaxb, SSbxsa, A_dof, SA_dof, B_dof, AxB_dof, BxSA_dof, MSa, MSsa, MSb, MSaxb, MSbxsa, Fa, Fb, Faxb, p_1, p_2, p_1x2 = \
                spf_pq.test(data, label_A, label_B, mode="notequal")

            answer_list = [[math.ceil(SSa *100.0) *0.01, int(A_dof), math.ceil(MSa *100.0) *0.01, math.ceil(Fa *100.0) *0.01, math.ceil(p_1 *1000.0) *0.001],
                           [math.ceil(SSsa *100.0) *0.01, int(SA_dof), math.ceil(MSsa *100.0) *0.01, '--', '--'],
                           [math.ceil(SSb *100.0) *0.01, int(B_dof), math.ceil(MSb *100.0) *0.01, math.ceil(Fb *100.0) *0.01, math.ceil(p_2 *1000.0) *0.001],
                           [math.ceil(SSaxb *100.0) *0.01, int(AxB_dof), math.ceil(MSaxb *100.0) *0.01, math.ceil(Faxb *100.0) *0.01, math.ceil(p_1x2 *1000.0) *0.001],
                           [math.ceil(SSbxsa *100.0) *0.01, int(BxSA_dof), math.ceil(MSbxsa *100.0) *0.01, '--', '--'],
                           [math.ceil((SSa + SSsa + SSb + SSaxb + SSbxsa) *100.0) * 0.01, int(A_dof + SA_dof + B_dof + AxB_dof + BxSA_dof),'--', '--', '--']]
            return answer_list

        elif mode == "RBFpq":
            rbf_pq = RBF_pq()
            SSs, SSa, SSaxs, SSb, SSbxs, SSaxb, SSaxbxs, SSt, S_dof, A_dof, AxS_dof, B_dof, BxS_dof, AxB_dof, AxBxS_dof, T_dof, MSs, MSa, MSaxs, MSb, MSbxs, MSaxb, MSaxbxs, Fa, Fb, Faxb, p_1, p_2, p_1x2 = rbf_pq.test(data, label_A, label_B)
            answer_list = [[math.ceil(SSs *100.0) *0.01, int(S_dof), math.ceil(MSs *100.0) *0.01, '--', '--'],
                           [math.ceil(SSa *100.0) *0.01, int(A_dof), math.ceil(MSa *100.0) *0.01, math.ceil(Fa *100.0) *0.01, math.ceil(p_1 *1000.0) *0.001],
                           [math.ceil(SSaxs *100.0) *0.01, int(AxS_dof), math.ceil(MSaxs *100.0) *0.01, '--', '--'],
                           [math.ceil(SSb *100.0) *0.01, int(B_dof), math.ceil(MSb *100.0) *0.01, math.ceil(Fb *100.0) *0.01, math.ceil(p_2 *1000.0) *0.001],
                           [math.ceil(SSbxs *100.0) *0.01, int(BxS_dof), math.ceil(MSbxs *100.0) *0.01, '--', '--'],
                           [math.ceil(SSaxb *100.0) *0.01, int(AxB_dof), math.ceil(MSaxb *100.0) *0.01, math.ceil(Faxb *100.0) *0.01, math.ceil(p_1x2 *1000.0) *0.001],
                           [math.ceil(SSaxbxs *100.0) *0.01, int(AxBxS_dof), math.ceil(MSaxbxs *100.0) *0.01, '--', '--'],
                           [math.ceil(SSt *100.0) * 0.01, int(T_dof),'--', '--', '--']]
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
