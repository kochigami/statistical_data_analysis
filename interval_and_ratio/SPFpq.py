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

class SPF_pq:
    def test(self, data, label_A, label_B, mode="equal"):
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

        if mode == "equal":
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
        
        return SSa, SSsa, SSb, SSaxb, SSbxsa, A_dof, SA_dof, B_dof, AxB_dof, BxSA_dof, MSa, MSsa, MSb, MSaxb, MSbxsa, Fa, Fb, Faxb, p_1, p_2, p_1x2

