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
                print "simple major effect"
                self.evaluate_simple_main_effect(data, label_A, label_B, MSwc, WC_dof, is_data_size_equal, mode="CRF")

            if p_1 < 0.05:
                print "major effect (factor1)"
                self.evaluate_main_effect(data, label_A, label_B, MSwc, WC_dof, is_data_size_equal)

            if p_2 < 0.05:
                print "major effect (factor2)"
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

            # sub effect tests
            if p_1x2 < 0.05:
                print "simple major effect"
                MSpool = (SSsa + SSbxsa) / float(SA_dof + BxSA_dof)
                POOL_dof = SA_dof + BxSA_dof
                print "q1: 0.05, p (see below), SA_dof: " + str(SA_dof)
                print "q2: 0.05, p (see below), BxSA_dof:" + str(BxSA_dof)
                print "MSsa: " + str(MSsa) + " MSbxsa: " + str(MSbxsa)
                print "------"
                self.evaluate_simple_main_effect(data, label_A, label_B, MSpool, POOL_dof, is_data_size_equal, MSbxsa, BxSA_dof, mode="SPF")

            if p_1 < 0.05:
                print "major effect (factor1)"
                self.evaluate_main_effect(data, label_A, label_B, MSsa, SA_dof, is_data_size_equal)

            if p_2 < 0.05:
                print "major effect (factor2)"
                self.evaluate_main_effect(data, label_B, label_A, MSbxsa, BxSA_dof, is_data_size_equal)

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
            # sub effect tests
            if p_1x2 < 0.05:
                print "simple major effect"
                MSpool_a = (SSaxs + SSaxbxs) / float(AxS_dof + AxBxS_dof)
                MSpool_b = (SSbxs + SSaxbxs) / float(BxS_dof + AxBxS_dof)
                POOL_A_dof = AxS_dof + AxBxS_dof
                POOL_B_dof = BxS_dof + AxBxS_dof
                print "q1-a: 0.05, p (see below), AxS_dof: " + str(AxS_dof)
                print "q1-b: 0.05, p (see below), BxS_dof: " + str(BxS_dof)
                print "q2: 0.05, p (see below), AxBxS_dof:" + str(AxBxS_dof)
                print "MSaxs: " + str(MSaxs) + " MSbxs: " + str(MSbxs) + " MSaxbxs: " + str(MSaxbxs)
                print "------"
                self.evaluate_simple_main_effect(data, label_A, label_B, MSpool_a, POOL_A_dof, True, MSpool_b, POOL_B_dof, mode="RBF")
                # data, label_A, label_B, MSwc, WC_dof, is_data_size_equal, MSbxsa=None, BxSA_dof=None, mode="CRF"

            if p_1 < 0.05:
                print "major effect (factor1)"
                self.evaluate_main_effect(data, label_A, label_B, MSaxs, AxS_dof, True)

            if p_2 < 0.05:
                print "major effect (factor2)"
                self.evaluate_main_effect(data, label_B, label_A, MSbxs, BxS_dof, True)

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
            average_list = {}
            new_average_list = {}
            for i in range(len(data)):
                average_list[(data.keys())[i]] = sum(data[(data.keys())[i]]) / float(len(data[(data.keys())[i]]))
            sum_list = [0 for i in range(len(label_A))]
            num_list = [0 for i in range(len(label_A))]
            for i in range(len(label_A)):
                for j in range(len(average_list.keys())):
                    if label_A[i] in (average_list.keys())[j]:
                        sum_list[i] += average_list[(average_list.keys())[j]]
                        num_list[i] += 1
                new_average_list[label_A[i]] = sum_list[i] / float(num_list[i])
            for i in range(len(new_average_list)):
                for j in range(i+1, len(new_average_list)):
                    print str((new_average_list.keys())[i]) + " - " + str((new_average_list.keys())[j]) + "= " + str(abs(new_average_list[(new_average_list.keys())[i]] - new_average_list[(new_average_list.keys())[j]]))

            print "------"
            print "Please calculate HSD as follows:"
            print "Refer to q table for Tukey's test. (ex. http://www2.stat.duke.edu/courses/Spring98/sta110c/qtable.html)"
            print "q_threshold: 0.05, dof1: " + str(p) + ", dof2: " + str(WC_dof)
            print "dof of factor1: " + str(p) + " dof of factor2: " + str(q)
            print "HSD: " + str(0.05 * math.sqrt(MSwc / (n * q))) + "(= q_threshold (0.05) * (math.sqrt(MSwc / (n * (dof of factor2)))))"
            print "if abs(average_list[k] - average_list[l]) > HSD, it is different significantly."
            print "------"
            print "------"

    def CRF_evaluate_simple_main_effect(self, label_A, label_B, MSwc, WC_dof, is_data_size_equal, p, q, MSab, MSba):
        for i in range(len(label_A)):
            Fba = [0 for i in range(len(label_A))]
        for i in range(len(label_B)):
            Fab = [0 for i in range(len(label_B))]
        for i in range(len(label_B)):
            Fab[i] = MSab[i] / MSwc
        for i in range(len(label_A)):
            Fba[i] = MSba[i] / MSwc
        F_threshold = calc_f.ppf(0.95, p - 1, WC_dof)
        b_list = []
        for i in range(len(label_B)):
            if F_threshold < Fab[i]:
                b_list.append(i)
        F_threshold = calc_f.ppf(0.95, q - 1, WC_dof)
        a_list = []
        for i in range(len(label_A)):
            if F_threshold < Fba[i]:
                a_list.append(i)
        return a_list, b_list

    def SPF_evaluate_simple_main_effect(self, label_A, label_B, MSpool, MSbxsa, POOL_dof, BxSA_dof, is_data_size_equal, p, q, MSab, MSba):
        for i in range(len(label_A)):
            Fba = [0 for i in range(len(label_A))]
        for i in range(len(label_B)):
            Fab = [0 for i in range(len(label_B))]
        for i in range(len(label_B)):
            Fab[i] = MSab[i] / MSpool
        for i in range(len(label_A)):
            Fba[i] = MSba[i] / MSbxsa
        F_threshold = calc_f.ppf(0.95, p - 1, POOL_dof)
        b_list = []
        for i in range(len(label_B)):
            if F_threshold < Fab[i]:
                b_list.append(i)
        F_threshold = calc_f.ppf(0.95, q - 1, BxSA_dof)
        a_list = []
        for i in range(len(label_A)):
            if F_threshold < Fba[i]:
                a_list.append(i)
        return a_list, b_list

    def RBF_evaluate_simple_main_effect(self, label_A, label_B, MSpool_a, MSpool_b, POOL_A_dof, POOL_B_dof, p, q, MSab, MSba):
        for i in range(len(label_A)):
            Fba = [0 for i in range(len(label_A))]
        for i in range(len(label_B)):
            Fab = [0 for i in range(len(label_B))]
        for i in range(len(label_B)):
            Fab[i] = MSab[i] / MSpool_a
        for i in range(len(label_A)):
            Fba[i] = MSba[i] / MSpool_b
        F_threshold = calc_f.ppf(0.95, p - 1, POOL_A_dof)
        b_list = []
        for i in range(len(label_B)):
            if F_threshold < Fab[i]:
                b_list.append(i)
        F_threshold = calc_f.ppf(0.95, q - 1, POOL_B_dof)
        a_list = []
        for i in range(len(label_A)):
            if F_threshold < Fba[i]:
                a_list.append(i)
        return a_list, b_list

    def evaluate_simple_main_effect(self, data, label_A, label_B, MSwc, WC_dof, is_data_size_equal, MSbxsa=None, BxSA_dof=None, mode="CRF"):
        p = len(label_A)
        q = len(label_B)
        if is_data_size_equal:
            n = len(data[(data.keys())[0]])
        else:
            tmp = 0.0
            for i in range(len(data.keys())):
                tmp += 1.0 / len(data[(data.keys())[i]])
            n = p * q / tmp  # = n_tilde #
        average_list = {}
        for i in range(len(data)):
            average_list[(data.keys())[i]] = sum(data[(data.keys())[i]]) / float(len(data[(data.keys())[i]]))

        for i in range(len(label_A)):
            SSba = [0 for i in range(len(label_A))]
            MSba = [0 for i in range(len(label_A))]
        for i in range(len(label_B)):
            SSab = [0 for i in range(len(label_B))]
            MSab = [0 for i in range(len(label_B))]

        for i in range(len(label_B)):
            AB_jk_squared = 0.0
            AB_jk = 0.0
            for j in range(len(average_list.keys())):
                if label_B[i] in (average_list.keys())[j]:
                    AB_jk += average_list[(average_list.keys())[j]]
                    AB_jk_squared += pow(average_list[(average_list.keys())[j]], 2.0)                  
            SSab[i] = n * (AB_jk_squared - pow(AB_jk, 2.0) / p)

        for i in range(len(label_A)):
            BA_jk_squared = 0.0
            BA_jk = 0.0
            for j in range(len(average_list.keys())):
                if label_A[i] in (average_list.keys())[j]:
                    BA_jk += average_list[(average_list.keys())[j]]
                    BA_jk_squared += pow(average_list[(average_list.keys())[j]], 2.0)                  
            SSba[i] = n * (BA_jk_squared - pow(BA_jk, 2.0) / q) 

        for i in range(len(label_B)):
            MSab[i] = SSab[i] / (p - 1.0)

        for i in range(len(label_A)):
            MSba[i] = SSba[i] / (q - 1.0)

        if mode == "CRF":
            a_list, b_list = self.CRF_evaluate_simple_main_effect(label_A, label_B, MSwc, WC_dof, is_data_size_equal, p, q, MSab, MSba)
        elif mode == "SPF":
            a_list, b_list = self.SPF_evaluate_simple_main_effect(label_A, label_B, MSwc, MSbxsa, WC_dof, BxSA_dof, is_data_size_equal, p, q, MSab, MSba)
            # MSwc: MSpool, WC_dof: POOL_dof
        elif mode == "RBF":
            a_list, b_list = self.RBF_evaluate_simple_main_effect(label_A, label_B, MSwc, MSbxsa, WC_dof, BxSA_dof, p, q, MSab, MSba)
            # MSwc: MSpool_a, MSbxsa: MSpool_b, WC_dof: POOL_A_dof, BxSA_dof: POOL_B_dof

        for i in range(len(b_list)):
            a_list2 = {}
            for j in range(len(average_list.keys())):
                if label_B[b_list[i]] in (average_list.keys())[j]:
                    a_list2[(average_list.keys())[j]] = average_list[(average_list.keys())[j]]
            for k in range(len(a_list2.keys())):
                for l in range(k+1, len(a_list2.keys())):
                    print str((a_list2.keys())[k]) + " - " + str((a_list2.keys())[l]) + " = " + str(abs(a_list2[(a_list2.keys())[k]] - a_list2[(a_list2.keys())[l]]))

        print "------"
        print "Please calculate HSD as follows:"
        print "Refer to q table for Tukey's test. (ex. http://www2.stat.duke.edu/courses/Spring98/sta110c/qtable.html)"
        if mode == "CRF":
            print "q_threshold: 0.05, m: " + str(p) + ", WC_dof: " + str(WC_dof)
            print "HSD:  " +str(0.05 * math.sqrt(MSwc / n)) + " (= q_threshold * math.sqrt(MSwc / n))"
        elif mode == "SPF":
            print "HSD: q_threshold(*) * " +str(math.sqrt(MSwc / n)) + " (math.sqrt(MSpool / n))"
            print "q_threshold(*): " + "(q1 * MSsa + q2 * MSbxsa * (q - 1)) / (MSsa + MSbxsa * (q - 1))"
            print "p: " + str(p) + " q: " + str(q)
        elif mode == "RBF":
            print "HSD: q_threshold(*) * " +str(math.sqrt(MSwc / n)) + " (math.sqrt(MSpool_a / n))"
            print "q_threshold(*): " + "(q1-a * MSaxs + q2 * MSaxbxs * (q - 1)) / (MSaxs + MSaxbxs * (q - 1))"
            print "p: " + str(p) + " q: " + str(q)
        print "if abs(average_list[k] - average_list[l]) > HSD, it is different significantly."
        print "------"
        print "------"

        for i in range(len(a_list)):
            b_list2 = {}
            for j in range(len(average_list.keys())):
                if label_A[a_list[i]] in (average_list.keys())[j]:
                    b_list2[(average_list.keys())[j]] = average_list[(average_list.keys())[j]]
            for k in range(len(b_list2.keys())):
                for l in range(k+1, len(b_list2.keys())):
                    print str((b_list2.keys())[k]) + " - " + str((b_list2.keys())[l]) + " = " + str(abs(b_list2[(b_list2.keys())[k]] - b_list2[(b_list2.keys())[l]]))
        
        print "------"
        print "Please calculate HSD as follows:"
        print "Refer to q table for Tukey's test. (ex. http://www2.stat.duke.edu/courses/Spring98/sta110c/qtable.html)"
        if mode == "CRF":
            print "q_threshold: 0.05, m: " + str(q) + ", WC_dof: " + str(WC_dof)
            print "HSD: " + str(0.05 * math.sqrt(MSwc / n)) + " (= q_threshold (0.05) * (math.sqrt(MSwc / n)))"
        elif mode == "SPF":
            print "q_threshold: 0.05, m: " + str(q) + ", BxSA_dof: " + str(BxSA_dof)
            print "HSD: " +str(0.05 * math.sqrt(MSbxsa / n)) + " (= q_threshold (0.05) * (math.sqrt(MSbxsa / n)))"
        elif mode == "RBF":
            print "HSD: q_threshold(*) * " +str(math.sqrt(MSbxsa / n)) + " (= math.sqrt(MSpool_b / n))"
            print "q_threshold(*): " + "(q1-b * MSbxs + q2 * MSaxbxs * (p - 1)) / (MSbxs + MSaxbxs * (p - 1))"
            print "p: " + str(p) + " q: " + str(q)
        print "if abs(average_list[k] - average_list[l]) > HSD, it is different significantly."
        print "------"
        print "------"

if __name__ == '__main__':
    pass
