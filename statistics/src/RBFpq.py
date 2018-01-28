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

class RBF_pq:
    def test(self, data, label_A, label_B):
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

        BS = 0.0
        Sik = []
        n_k = []
        for j in range(len(label_B)):
            for i in range(len(data.keys())):
                if label_B[j] in (data.keys())[i]:
                    n_k.append(len(data[(data.keys())[i]]))
                    break

        tmp = [[] for i in range(len(n_k))]
        for i in range(len(label_B)):
            tmp[i] = [0 for s in range(n_k[i])]
            for j in range(n_k[i]):
                for k in range(len(data.keys())):
                    if label_B[i] in (data.keys())[k]:
                        tmp[i][j] += data[(data.keys())[k]][j]
                Sik.append(tmp[i][j])

        for i in range(len(Sik)):
            BS += pow(Sik[i], 2.0) / p

        print "BS: " + str(BS)

        tmp = [0 for j in range(len(data[(data.keys())[0]]))]
        for i in range(len(data.keys())):
            for j in range(len(data[(data.keys())[0]])):
                tmp[j] += data[(data.keys())[i]][j]
        
        S = 0.0
        for i in range(len(tmp)):
            S += pow(tmp[i], 2.0) / (p * q)
        print "S: " + str(S)

        G = 0.0
        for i in range(len(data.keys())):
            for j in range(len(data[(data.keys()[i])])):
                G += (data[(data.keys()[i])])[j]

        n = len(data[(data.keys()[0])])

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
        SSt = ABS - X
        SSs = S - X
        SSaxs = AS - A - S + X
        SSbxs = BS - B - S + X
        SSaxbxs = ABS - AB - AS - BS + A + B + S - X

        AxS_dof = (p - 1) * (n - 1)
        S_dof = n - 1
        BxS_dof = (q - 1) * (n - 1)
        AxBxS_dof = (p - 1) * (q - 1) * (n - 1)
        T_dof = n * p * q - 1

        MSs = SSs / S_dof
        MSa = SSa / A_dof
        MSaxs = SSaxs / AxS_dof
        MSb = SSb / B_dof
        MSbxs = SSbxs / BxS_dof
        MSaxb = SSaxb / AxB_dof
        MSaxbxs = SSaxbxs / AxBxS_dof

        Fa = MSa / MSaxs
        Fb = MSb / MSbxs
        Faxb = MSaxb / MSaxbxs

        print "Fa: " + str(Fa)
        print "Fb: " + str(Fb)
        print "Faxb: " + str(Faxb)
        
        p_1 = calc_f.sf(Fa, A_dof, AxS_dof)
        p_2 = calc_f.sf(Fb, B_dof, BxS_dof)
        p_1x2 = calc_f.sf(Faxb, AxB_dof, AxBxS_dof)        

        return SSs, SSa, SSaxs, SSb, SSbxs, SSaxb, SSaxbxs, SSt, S_dof, A_dof, AxS_dof, B_dof, BxS_dof, AxB_dof, AxBxS_dof, T_dof, MSs, MSa, MSaxs, MSb, MSbxs, MSaxb, MSaxbxs, Fa, Fb, Faxb, p_1, p_2, p_1x2
