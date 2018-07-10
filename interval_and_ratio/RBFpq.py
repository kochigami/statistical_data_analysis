#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils import Utils
from scipy.stats import f as calc_f
'''
referenced as calc_p because of the error below:
# File "/home/kochigami/my_tutorial/statistics/src/t_test/t_test.py", line 80, in unpaired_ttest
# p = t.sf(t_value, dof)
# UnboundLocalError: local variable 't' referenced before assignment
# t test
'''

'''
RBF: randomized block factorial design

reference: 心理学のためのデータ解析テクニカルブック　 森 敏昭, 吉田 寿夫編著　北大路書房 p. 116-121
'''
class RBF_pq:
    def test(self, data, label_A, label_B):
        '''
        data:
                        s1 2 3 4 5
        data['a1-b1'] = [3,3,1,3,5]
        data['a1-b2'] = [4,3,4,5,7]
        data['a1-b3'] = [6,6,6,4,8]
        data['a1-b4'] = [5,7,8,7,9]
        data['a2-b1'] = [3,5,2,4,6]
        data['a2-b2'] = [2,6,3,6,4]
        data['a2-b3'] = [3,2,3,6,5]
        data['a2-b4'] = [2,3,3,4,6]

        label_a = ["a1", "a2"]
        label_b = ["b1", "b2", "b3", "b4"]

        Subject                  S
        Major Effect A           A
        Error of Major Effect A  AxS
        Major Effect B           B
        Error of Major Effect B  BxS
        Interaction              AxB
        Error                    AxBxS
        '''
        utils = Utils()
        # number of each condition A, B
        p = utils.condition_type_num(label_A)
        q = utils.condition_type_num(label_B)

        # ABS: squared sum of each sample
        ABS = utils.ABS(data)

        # AB: squared sum of each condition / sample num (condition: a1-b1, a1-b2, a2-b1, a2-b2)
        AB = utils.AB(data)

        # dof
        A_dof = p - 1
        B_dof = q - 1
        AxB_dof = A_dof * B_dof
        
        # n_j: list of sample number
        # ex. [a1, a2] = [5, 5]
        n_j = utils.condition_num(data, label_A)

        # Sij: total sum of data per subject
        Sij = utils.Sij(data, n_j, label_A)

        # AS: sum of Sij^2 / q
        AS = 0.0
        for i in range(len(Sij)):
            AS += pow(Sij[i], 2.0) / q

        # n_k: list of sample number
        # ex. [b1, b2] = [5, 5]
        n_k = utils.condition_num(data, label_B)

        # Sik: total sum of data per subject
        Sik = utils.Sij(data, n_k, label_B)

        # BS: sum of Sik^2 / p
        BS = 0.0
        for i in range(len(Sik)):
            BS += pow(Sik[i], 2.0) / p

        # TODO From here
        tmp = [0 for j in range(len(data[(data.keys())[0]]))]
        for i in range(len(data.keys())):
            for j in range(len(data[(data.keys())[0]])):
                tmp[j] += data[(data.keys())[i]][j]
        
        S = 0.0
        for i in range(len(tmp)):
            S += pow(tmp[i], 2.0) / (p * q)

        # G: sum of all the data
        G = utils.G(data)

        # n: number of data per each category
        # focus on (data.keys()[0]) in this case
        # because the number of data per each category is equal
        n = len(data[(data.keys()[0])])

        # X: G^2 / npq
        X = utils.X(G, p, q, n)

        A_sum = utils.condition_sum(data, label_A)
        A = 0.0
        for i in range(len(A_sum)):
            A += pow(A_sum[i], 2.0) / (n * q)

        B_sum = utils.condition_sum(data, label_B)
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

        p_1 = calc_f.sf(Fa, A_dof, AxS_dof)
        p_2 = calc_f.sf(Fb, B_dof, BxS_dof)
        p_1x2 = calc_f.sf(Faxb, AxB_dof, AxBxS_dof)        

        return SSs, SSa, SSaxs, SSb, SSbxs, SSaxb, SSaxbxs, SSt, S_dof, A_dof, AxS_dof, B_dof, BxS_dof, AxB_dof, AxBxS_dof, T_dof, MSs, MSa, MSaxs, MSb, MSbxs, MSaxb, MSaxbxs, Fa, Fb, Faxb, p_1, p_2, p_1x2
