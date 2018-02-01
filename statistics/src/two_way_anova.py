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

            # sub effect tests
            if p_1x2 < 0.05:
                # simple major effect
                self.evaluate_simple_main_effect(data, label_A, label_B, MSwc, WC_dof, is_data_size_equal)

            elif p_1 < 0.05:
                self.evaluate_main_effect(data, label_A, label_B, MSwc, WC_dof, is_data_size_equal)
                
            elif p_2 < 0.05:
                self.evaluate_main_effect(data, label_B, label_A, MSwc, WC_dof, is_data_size_equal)

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

    def evaluate_main_effect(self, data, label_A, label_B, MSwc, WC_dof, is_data_size_equal):
        if len(label_A) > 2:
            p = len(label_A)
            q = len(label_B)
            if is_data_size_equal:
                n = len(data[(data.keys())[0]])
            else:
                tmp = 0.0
                for i in range(len(data.keys())):
                    tmp += 1.0 / len(data[(data.keys())[i]])
                n = p * q / tmp  # = n_tilde #
            for i in range(len(label_A)):
                sum_list = [0 for i in range(len(label_A))]
                num_list = [0 for i in range(len(label_A))]
                average_list = [0 for i in range(len(label_A))]
            for i in range(len(label_A)):
                for j in range(len(data.keys())):
                    if label_A[i] in (data.keys())[j]:
                        sum_list[i] += sum(data[(data.keys())[j]])
                        num_list[i] += len(data[(data.keys())[j]])

                average_list[i] = sum_list[i] / float(num_list[i])
            for i in range(len(average_list)):
                for j in range(i+1, len(average_list)):
                    print "a" + str(i) + " - " + "a" + str(j) + "= " + str(abs(average_list[i] - average_list[j]))

            print " "
            print "Please calculate HSD as follows:"
            print "Refer to q table for Tukey's test. (ex. http://www2.stat.duke.edu/courses/Spring98/sta110c/qtable.html)"
            print "q_threshold: 0.05, dof1: " + str(p-1) + ", dof2: " + str(WC_dof)
            print "HSD: q_threshold * " +str(math.sqrt(MSwc / (n * q))) + " (math.sqrt(MSwc / (n * q)))"
            print "if abs(average_list[k] - average_list[l]) > HSD, it is different significantly."
            print " "

    def evaluate_simple_main_effect(self, data, label_A, label_B, MSwc, WC_dof, is_data_size_equal):
        p = len(label_A)
        q = len(label_B)
        if is_data_size_equal:
            n = len(data[(data.keys())[0]])
        else:
            tmp = 0.0
            for i in range(len(data.keys())):
                tmp += 1.0 / len(data[(data.keys())[i]])
            n = p * q / tmp  # = n_tilde #
        average_list = []
        for i in range(len(data)):
            average_list.append(sum(data[(data.keys())[i]]) / float(len(data[(data.keys())[i]])))

        for i in range(len(label_A)):
            SSba = [0 for i in range(len(label_A))]
            MSba = [0 for i in range(len(label_A))]
            Fba = [0 for i in range(len(label_A))]
        for i in range(len(label_B)):
            SSab = [0 for i in range(len(label_B))]
            MSab = [0 for i in range(len(label_B))]
            Fab = [0 for i in range(len(label_B))]

        for i in range(len(label_B)):
            AB_jk_squared = 0.0
            AB_jk = 0.0
            for j in range(len(average_list)):
                if label_B[i] in (data.keys())[j]:
                    AB_jk += average_list[j]
                    AB_jk_squared += pow(average_list[j], 2.0)                  
            SSab[i] = n * (AB_jk_squared - pow(AB_jk, 2.0) / p)

        for i in range(len(label_A)):
            BA_jk_squared = 0.0
            BA_jk = 0.0
            for j in range(len(average_list)):
                if label_A[i] in (data.keys())[j]:
                    BA_jk += average_list[j]
                    BA_jk_squared += pow(average_list[j], 2.0)                  
            SSba[i] = n * (BA_jk_squared - pow(BA_jk, 2.0) / q) 

        for i in range(len(label_B)):
            MSab[i] = SSab[i] / (p - 1.0)

        for i in range(len(label_A)):
            MSba[i] = SSba[i] / (q - 1.0)

        for i in range(len(label_B)):
            Fab[i] = MSab[i] / MSwc

        for i in range(len(label_A)):
            Fba[i] = MSba[i] / MSwc
        
        F_threshold = calc_f.ppf(0.95, (p - 1) * (q - 1), WC_dof)
        
        b_list = []
        for i in range(len(label_B)):
            if F_threshold < Fab[i]:
                b_list.append(i)

        a_list = []
        for i in range(len(label_A)):
            if F_threshold < Fba[i]:
                a_list.append(i)

        for i in range(len(b_list)):
            a_list2 = []
            for j in range(len(average_list)):
                if label_B[i] in (data.keys())[j]:
                    a_list2.append(average_list[j])
            for k in range(len(a_list2)):
                for l in range(k+1, len(a_list2)):
                    print "a" + str(k) + " b" + str(b_list[i]) + " - " + "a" + str(l) + " b" + str(b_list[i]) + "= " + str(abs(average_list[k] - average_list[l]))

        print " "
        print "Please calculate HSD as follows:"
        print "Refer to q table for Tukey's test. (ex. http://www2.stat.duke.edu/courses/Spring98/sta110c/qtable.html)"
        print "q_threshold: 0.05, dof1: " + str(p) + ", dof2: " + str(WC_dof)
        print "HSD: q_threshold * " +str(math.sqrt(MSwc / n)) + " (math.sqrt(MSwc / n))"
        print "if abs(average_list[k] - average_list[l]) > HSD, it is different significantly."
        print " "

        for i in range(len(a_list)):
            b_list2 = []
            for j in range(len(average_list)):
                if label_A[i] in (data.keys())[j]:
                    b_list2.append(average_list[j])
            for k in range(len(b_list2)):
                for l in range(k+1, len(b_list2)):
                    print "a" + str(a_list[i]) + " b" + str(k) + " - " + "a" + str(a_list[i]) + " b" + str(l) +"= " + str(abs(average_list[k] - average_list[l]))
        
        print " "
        print "Please calculate HSD as follows:"
        print "Refer to q table for Tukey's test. (ex. http://www2.stat.duke.edu/courses/Spring98/sta110c/qtable.html)"
        print "q_threshold: 0.05, dof1: " + str(q) + ", dof2: " + str(WC_dof)
        print "HSD: q_threshold * " +str(math.sqrt(MSwc / n)) + " (math.sqrt(MSwc / n))"
        print "if abs(average_list[k] - average_list[l]) > HSD, it is different significantly."
        print " "
    
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
