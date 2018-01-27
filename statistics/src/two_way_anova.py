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

            is_data_size_equal = True
            for i in range(len(data.keys())):
                if len(data[(data.keys())[0]]) != len(data[(data.keys())[i]]):
                    is_data_size_equal = False
            ABS = 0.0
            for i in range(len(data.keys())):
                for j in range(len(data[(data.keys()[i])])):
                    ABS += pow((data[(data.keys()[i])])[j], 2.0)
            AB = 0.0
            for i in range(len(data.keys())):
                AB += pow(sum(data[(data.keys())[i]]), 2.0) / len(data[(data.keys())[i]])

            p = len(label_A)
            q = len(label_B)

            A_dof = p - 1
            B_dof = q - 1
            AxB_dof = A_dof * B_dof

            if is_data_size_equal:
                G = 0.0
                for i in range(len(data.keys())):
                    for j in range(len(data[(data.keys()[i])])):
                        G += (data[(data.keys()[i])])[j]

                n = len(data[(data.keys()[0])])

                WC_dof = p * q * (n - 1.0)

                X = pow(G, 2.0) / (n * p * q)

                A_sum = []
                A_sum_tmp = 0.0
                # category1 sum
                for i in range(len(label_A)):
                    for j in range(len(data.keys())):
                        if label_A[i] in (data.keys())[j]:
                            A_sum_tmp += sum(data[(data.keys())[j]])
                    A_sum.append(A_sum_tmp)
                    A_sum_tmp = 0.0

                A = 0.0
                for i in range(len(A_sum)):
                    A += pow(A_sum[i], 2.0) / (n * q)

                # category2 sum
                B_sum = []
                B_sum_tmp = 0.0
                for i in range(len(label_B)):
                    for j in range(len(data.keys())):
                        if label_B[i] in (data.keys())[j]:
                            B_sum_tmp += sum(data[(data.keys())[j]])
                    B_sum.append(B_sum_tmp)
                    B_sum_tmp = 0.0

                B = 0.0
                for i in range(len(B_sum)):
                    B += pow(B_sum[i], 2.0) / (n * p)

                SSa = A - X
                SSb = B - X
                SSaxb = AB - A - B + X
                SSwc = ABS - AB
                SSt = ABS - X

                MSwc = SSwc / WC_dof
                MSa = SSa / A_dof
                MSb = SSb / B_dof
                MSaxb = SSaxb / AxB_dof

                Fa = MSa / MSwc
                Fb = MSb / MSwc
                Faxb = MSaxb / MSwc

                # calculate p
                p_1 = calc_f.sf(Fa, A_dof, WC_dof)
                p_2 = calc_f.sf(Fb, B_dof, WC_dof)
                p_1x2 = calc_f.sf(Faxb, AxB_dof, WC_dof)

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

                answer_list = [[math.ceil(SSa * 100.0) * 0.01, int(A_dof), math.ceil(MSa * 100.0) * 0.01, math.ceil(Fa * 100.0) * 0.01, math.ceil(p_1 * 1000.0) * 0.001],
                               [math.ceil(SSb * 100.0) * 0.01, int(B_dof), math.ceil(MSb * 100.0) * 0.01, math.ceil(Fb * 100.0) * 0.01, math.ceil(p_2 * 1000.0) * 0.001],
                               [math.ceil(SSaxb * 100.0) * 0.01, int(AxB_dof), math.ceil(MSaxb * 100.0) * 0.01, math.ceil(Faxb * 100.0) * 0.01, math.ceil(p_1x2 * 1000.0) * 0.001],
                               [math.ceil(SSwc * 100.0) * 0.01, int(WC_dof), math.ceil(MSwc * 100.0) * 0.01, '--', '--'],
                               [math.ceil(SSt * 100.0) * 0.01, int(A_dof + B_dof + AxB_dof + WC_dof),'--', '--', '--']]
                return answer_list

            else:
                G_dash = 0.0
                unweighted_mean = []
                for i in range(len(data.keys())):
                    unweighted_mean.append(sum(data[(data.keys())[i]]) / float(len(data[(data.keys())[i]])))

                G_dash = sum(unweighted_mean)

                A_sum_tmp = 0.0
                A_num_tmp = 0.0
                A_sum = []
                for j in range(len(label_A)):
                    for i in range(len(data.keys())):
                        if label_A[j] in (data.keys())[i]:
                            A_sum_tmp += unweighted_mean[i]
                            A_num_tmp += 1
                    A_sum_tmp = A_sum_tmp / A_num_tmp
                    A_sum.append(A_sum_tmp)
                    A_sum_tmp = 0.0
                    A_num_tmp = 0.0

                B_sum_tmp = 0.0
                B_num_tmp = 0.0
                B_sum = []
                for j in range(len(label_B)):
                    for i in range(len(data.keys())):
                        if label_B[j] in (data.keys())[i]:
                            B_sum_tmp += unweighted_mean[i]
                            B_num_tmp += 1
                    B_sum_tmp = B_sum_tmp / B_num_tmp
                    B_sum.append(B_sum_tmp)
                    B_sum_tmp = 0.0
                    B_num_tmp = 0.0

                N = 0
                for i in range(len(data.keys())):
                    N += len(data[(data.keys())[i]])
                WC_dof = N - p * q

                X_dash = pow(G_dash, 2.0) / (p * q)

                A_dash = 0.0
                for i in range(len(A_sum)):
                    A_dash += pow(A_sum[i], 2.0)
                A_dash *= q

                B_dash = 0.0
                for i in range(len(B_sum)):
                    B_dash += pow(B_sum[i], 2.0)
                B_dash *= p

                AB_dash = 0.0
                for i in range(len(unweighted_mean)):
                    AB_dash += pow(unweighted_mean[i], 2.0)

                tmp = 0.0
                for i in range(len(data.keys())):
                    tmp += 1.0 / len(data[(data.keys())[i]])
                n_tilde = p * q / tmp

                SSa = n_tilde * float(A_dash - X_dash)
                SSb = n_tilde * float(B_dash - X_dash)
                SSaxb = n_tilde * float(AB_dash - A_dash - B_dash + X_dash)
                SSwc = ABS - float(AB)
                SSt = SSa + SSb + SSaxb + SSwc

                MSwc = SSwc / WC_dof
                MSa = SSa / A_dof
                MSb = SSb / B_dof
                MSaxb = SSaxb / AxB_dof

                Fa = MSa / MSwc
                Fb = MSb / MSwc
                Faxb = MSaxb / MSwc

                # calculate p
                p_1 = calc_f.sf(Fa, A_dof, WC_dof)
                p_2 = calc_f.sf(Fb, B_dof, WC_dof)
                p_1x2 = calc_f.sf(Faxb, AxB_dof, WC_dof)

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
            # same as CRFpq & size is equal #
            is_data_size_equal = True
            for i in range(len(data.keys())):
                if len(data[(data.keys())[0]]) != len(data[(data.keys())[i]]):
                    is_data_size_equal = False
            ABS = 0.0
            for i in range(len(data.keys())):
                for j in range(len(data[(data.keys()[i])])):
                    ABS += pow((data[(data.keys()[i])])[j], 2.0)
            AB = 0.0
            for i in range(len(data.keys())):
                AB += pow(sum(data[(data.keys())[i]]), 2.0) / len(data[(data.keys())[i]])

            p = len(label_A)
            q = len(label_B)

            A_dof = p - 1
            B_dof = q - 1
            AxB_dof = A_dof * B_dof

            AS = 0.0
            Sij = []
            n_j = []
            for j in range(len(label_A)):
                for i in range(len(data.keys())):
                    if label_A[j] in (data.keys())[i]:
                        n_j.append(len(data[(data.keys())[i]]))
                        break

            tmp = [[] for i in range(len(n_j))]
            for i in range(len(label_A)):
                tmp[i] = [0 for s in range(n_j[i])]
                for j in range(n_j[i]):
                    for k in range(len(data.keys())):
                        if label_A[i] in (data.keys())[k]:
                            tmp[i][j] += data[(data.keys())[k]][j]
                    Sij.append(tmp[i][j])

            for i in range(len(Sij)):
                AS += pow(Sij[i], 2.0) / q

            if is_data_size_equal:
                G = 0.0
                for i in range(len(data.keys())):
                    for j in range(len(data[(data.keys()[i])])):
                        G += (data[(data.keys()[i])])[j]

                n = len(data[(data.keys()[0])])

                WC_dof = p * q * (n - 1.0)

                X = pow(G, 2.0) / (n * p * q)

                A_sum = []
                A_sum_tmp = 0.0
                # category1 sum
                for i in range(len(label_A)):
                    for j in range(len(data.keys())):
                        if label_A[i] in (data.keys())[j]:
                            A_sum_tmp += sum(data[(data.keys())[j]])
                    A_sum.append(A_sum_tmp)
                    A_sum_tmp = 0.0

                A = 0.0
                for i in range(len(A_sum)):
                    A += pow(A_sum[i], 2.0) / (n * q)

                # category2 sum
                B_sum = []
                B_sum_tmp = 0.0
                for i in range(len(label_B)):
                    for j in range(len(data.keys())):
                        if label_B[i] in (data.keys())[j]:
                            B_sum_tmp += sum(data[(data.keys())[j]])
                    B_sum.append(B_sum_tmp)
                    B_sum_tmp = 0.0

                B = 0.0
                for i in range(len(B_sum)):
                    B += pow(B_sum[i], 2.0) / (n * p)
                # same as CRFpq & size is equal #
                                
                # same as CRFpq & size is equal #
                SSa = A - X
                SSb = B - X
                SSaxb = AB - A - B + X
                SSt = ABS - X
                # same as CRFpq & size is equal #

                SSsa = AS - A
                SSbxsa = ABS - AB - AS + A
    
                SA_dof = p * (n - 1)
                BxSA_dof = p * (q - 1) * (n - 1)

                # same as CRFpq & size is equal #
                MSa = SSa / A_dof
                MSb = SSb / B_dof
                MSaxb = SSaxb / AxB_dof
                # same as CRFpq & size is equal #
                MSsa = SSsa / SA_dof
                MSbxsa = SSbxsa / BxSA_dof

                Fa = MSa / MSsa
                Fb = MSb / MSbxsa
                Faxb = MSaxb / MSbxsa

                # calculate p
                p_1 = calc_f.sf(Fa, A_dof, BxSA_dof)
                p_2 = calc_f.sf(Fb, B_dof, BxSA_dof)
                p_1x2 = calc_f.sf(Faxb, AxB_dof, BxSA_dof)

                answer_list = [[math.ceil(SSa *100.0) *0.01, int(A_dof), math.ceil(MSa *100.0) *0.01, math.ceil(Fa *100.0) *0.01, math.ceil(p_1 *1000.0) *0.001],
                               [math.ceil(SSsa *100.0) *0.01, int(SA_dof), math.ceil(MSsa *100.0) *0.01, '--', '--'],
                               [math.ceil(SSb *100.0) *0.01, int(B_dof), math.ceil(MSb *100.0) *0.01, math.ceil(Fb *100.0) *0.01, math.ceil(p_2 *1000.0) *0.001],
                               [math.ceil(SSaxb *100.0) *0.01, int(AxB_dof), math.ceil(MSaxb *100.0) *0.01, math.ceil(Faxb *100.0) *0.01, math.ceil(p_1x2 *1000.0) *0.001],
                               [math.ceil(SSbxsa *100.0) *0.01, int(BxSA_dof), math.ceil(MSbxsa *100.0) *0.01, '--', '--'],
                               [math.ceil((SSa + SSsa + SSb + SSaxb + SSbxsa) *100.0) * 0.01, int(n * p * q - 1),'--', '--', '--']]
                return answer_list

            else:
                A_sum_tmp = 0.0
                A_sum = []
                for j in range(len(label_A)):
                    for i in range(len(data.keys())):
                        if label_A[j] in (data.keys())[i]:
                            A_sum_tmp += sum(data[(data.keys())[i]])
                    A_sum.append(A_sum_tmp)
                    A_sum_tmp = 0.0

                A = 0.0
                for i in range(len(A_sum)):
                    A += pow(A_sum[i], 2.0) / (n_j[i] * q)

                # same 
                G_dash = 0.0
                unweighted_mean = []
                for i in range(len(data.keys())):
                    unweighted_mean.append(sum(data[(data.keys())[i]]) / float(len(data[(data.keys())[i]])))

                A_sum_tmp = 0.0
                A_sum = []
                A_num_tmp = 0.0
                for j in range(len(label_A)):
                    for i in range(len(data.keys())):
                        if label_A[j] in (data.keys())[i]:
                            A_sum_tmp += unweighted_mean[i]
                            A_num_tmp += 1.0
                    A_sum_tmp = A_sum_tmp / A_num_tmp
                    A_sum.append(A_sum_tmp)
                    A_sum_tmp = 0.0
                    A_num_tmp = 0.0

                B_sum_tmp = 0.0
                B_num_tmp = 0.0
                B_sum = []
                for j in range(len(label_B)):
                    for i in range(len(data.keys())):
                        if label_B[j] in (data.keys())[i]:
                            B_sum_tmp += unweighted_mean[i]
                            B_num_tmp += 1
                    B_sum_tmp = B_sum_tmp / B_num_tmp
                    B_sum.append(B_sum_tmp)
                    B_sum_tmp = 0.0
                    B_num_tmp = 0.0

                G_dash = sum(unweighted_mean)
                X_dash = pow(G_dash, 2.0) / (p * q)

                A_dash = 0.0
                for i in range(len(A_sum)):
                    A_dash += pow(A_sum[i], 2.0)
                A_dash *= q

                B_dash = 0.0
                for i in range(len(B_sum)):
                    B_dash += pow(B_sum[i], 2.0)
                B_dash *= p
                
                AB_dash = 0.0
                for i in range(len(unweighted_mean)):
                    AB_dash += pow(unweighted_mean[i], 2.0)
                # same
                tmp = 0.0
                for i in range(len(n_j)):
                    tmp += 1.0 / n_j[i]
                n_tilde = p / tmp

                # same
                SSsa = AS - A
                SSbxsa = ABS - AB - AS + A
                # same
                SSa = n_tilde * (A_dash - X_dash)
                SSb = n_tilde * (B_dash - X_dash)
                SSaxb = n_tilde * (AB_dash - A_dash - B_dash + X_dash)

                N = sum(n_j) 
                SA_dof = N - p
                BxSA_dof = (N - p) * (q - 1)

                MSsa = SSsa / SA_dof
                MSa = SSa / A_dof
                MSb = SSb / B_dof
                MSaxb = SSaxb / AxB_dof
                MSbxsa = SSbxsa / BxSA_dof

                Fa = MSa / MSsa
                Fb = MSb / MSbxsa
                Faxb = MSaxb / MSbxsa

                # calculate p
                p_1 = calc_f.sf(Fa, A_dof, BxSA_dof)
                p_2 = calc_f.sf(Fb, B_dof, BxSA_dof)
                p_1x2 = calc_f.sf(Faxb, AxB_dof, BxSA_dof)

                answer_list = [[math.ceil(SSa *100.0) *0.01, int(A_dof), math.ceil(MSa *100.0) *0.01, math.ceil(Fa *100.0) *0.01, math.ceil(p_1 *1000.0) *0.001],
                               [math.ceil(SSsa *100.0) *0.01, int(SA_dof), math.ceil(MSsa *100.0) *0.01, '--', '--'],
                               [math.ceil(SSb *100.0) *0.01, int(B_dof), math.ceil(MSb *100.0) *0.01, math.ceil(Fb *100.0) *0.01, math.ceil(p_2 *1000.0) *0.001],
                               [math.ceil(SSaxb *100.0) *0.01, int(AxB_dof), math.ceil(MSaxb *100.0) *0.01, math.ceil(Faxb *100.0) *0.01, math.ceil(p_1x2 *1000.0) *0.001],
                               [math.ceil(SSbxsa *100.0) *0.01, int(BxSA_dof), math.ceil(MSbxsa *100.0) *0.01, '--', '--'],
                               [math.ceil((SSa + SSsa + SSb + SSaxb + SSbxsa) *100.0) * 0.01, int(A_dof + SA_dof + B_dof + AxB_dof + BxSA_dof),'--', '--', '--']]
                print answer_list
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
