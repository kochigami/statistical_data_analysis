#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy.stats import f as calc_f
from utils import Utils
'''
referenced as calc_p because of the error below:
File "/home/kochigami/my_tutorial/statistics/src/t_test/t_test.py", line 80, in unpaired_ttest
p = t.sf(t_value, dof)
UnboundLocalError: local variable 't' referenced before assignment
t test
'''

'''
SPF: split-plot design

reference: 心理学のためのデータ解析テクニカルブック　 森 敏昭, 吉田 寿夫編著　北大路書房 p. 107-121
'''
class SPF_pq:
    # 要因Aには異なる被験者が割り当てられている (例えばa1, a2 のどちらか)
    # 要因Bは全ての被験者が試している (例えばb1-b4全部試す)
    def test(self, data, label_A, label_B, mode="equal"):
        utils = Utils()
        # number of each condition A, B
        p = utils.condition_type_num(label_A)
        q = utils.condition_type_num(label_B)

        # ABS: squared sum of all the data
        ABS = utils.ABS(data)

        # AB: squared sum of each condition / sample num (condition: a1-b1, a1-b2, a2-b1, a2-b2)
        AB = utils.AB(data)

        # dof
        A_dof = p - 1
        B_dof = q - 1
        AxB_dof = A_dof * B_dof

        # n_j: list of sample number (category A)
        # ex. [a1, a2] = [5, 4]
        # each sample number of a1 / a2 is same
        # len(data['a1-b1']) == len(data['a1-b2']) == len(data['a1-b3']) == len(data['a1-b4']) = 5
        # len(data['a2-b1']) == len(data['a2-b2']) == len(data['a2-b3']) == len(data['a2-b4']) = 4 
        n_j = utils.condition_num(data, label_A)

        # Sij: total sum list of data per subject
        # ex. [18, 19, 19, 19, 29, 10, 16, 11, 20, 21]
        Sij = utils.Sij(data, n_j, label_A)

        # AS: sum of Sij^2 / q
        AS = 0.0
        for i in range(len(Sij)):
            AS += pow(Sij[i], 2.0) / q

        # A_sum: category1 sum list
        A_sum = utils.condition_sum(data, label_A)

        if mode == "equal":
            '''
            data:

            data['a1-b1'] = [3,3,1,3,5]
            data['a1-b2'] = [4,3,4,5,7]
            data['a2-b3'] = [6,6,6,4,8]
            data['a2-b4'] = [5,7,8,7,9]
            data['a2-b1'] = [3,5,2,4,6]
            data['a2-b2'] = [2,6,3,6,4]
            data['a2-b3'] = [3,2,3,6,5]
            data['a2-b4'] = [2,3,3,4,6]

            label_a = ["a1", "a2"]
            label_b = ["b1", "b2", "b3", "b4"]

            results:
            Major Effect A
            Error of Major Effect A S(A)
            Major Effect B
            Interaction  AxB
            Error        BxS(A)

            requires:
            p: number of each condition A
            q: number of each condition B
            A_dof:   dof of category A
            B_dof:   dof of category B
            AxB_dof: dof of AxB
            BxSA_dof: p * (q - 1) * (n - 1)
            unweighted_mean: list of mean value per condition (condition: a1-b1, a1-b2, a1-b3, a1-b4, a2-b1, a2-b2, a2-b3, a2-b4)

            n_j: list of sample number (category A)
            A_sum: category1 sum list
            ABS: squared sum of all the data
            AB: squared sum of each condition / sample num per condition (condition: a1-b1, a1-b2, a1-b3, a1-b4, a2-b1, a2-b2, a2-b3, a2-b4)
            G: sum of all the data
            X: G^2 / npq
            A: Aj^2 / nq (j=0~len(A_sum), Aj: A_sum[j], sum list of category A)
            B: Bi^2 / np (i=0~len(B_sum), Bi: B_sum[i], sum list of category B)
            WC_dof: pq (n-1)
            Sij: total sum of data per subject
            AS: sum of Sij^2 / q

            SSa:   A-X
            SSb:   B-X
            SSaxb: AB-A-B+X
            SSwc:  ABS-AB
            SSsa: AS - A
            SSbxsa: ABS - AB - AS + A

            MSa = SSa / A_dof
            MSsa = SSsa / SA_dof
            MSb = SSb / B_dof
            MSaxb = SSaxb / AxB_dof
            MSbxsa = SSbxsa / BxSA_dof

            Fa = MSa / MSsa
            Fb = MSb / MSbxsa
            Faxb = MSaxb / MSbxsa
            '''
            # G: sum of all the data
            G = utils.G(data)

            # n: number of data per each category
            # focus on (data.keys()[0]) in this case
            # because the number of data per each category is equal
            n = len(data[(data.keys()[0])])

            # WC_dof: dof of Error
            # (npq-1) - (p-1) - (q-1) - (p-1)(q-1)
            # = npq-p-q-pq+p+q = npq - pq = pq (n-1)
            WC_dof = utils.WC_dof(p, q, n)

            # X: G^2 / npq
            X = utils.X(G, p, q, n)

            # A: sum of Aj^2/ n*q
            A = 0.0
            for i in range(len(A_sum)):
                A += pow(A_sum[i], 2.0) / (n * q)

            # B_sum: category2 sum
            B_sum = utils.condition_sum(data, label_B)

            # B: sum of Bk^2 / n*p
            B = 0.0
            for i in range(len(B_sum)):
                B += pow(B_sum[i], 2.0) / (n * p)
                
            # calculate SS
            # same as CRFpq & size is equal #
            SSa = A - X
            SSb = B - X
            SSaxb = AB - A - B + X
            SSt = ABS - X
            
            # These are new for SPF design
            SSsa = AS - A
            SSbxsa = ABS - AB - AS + A
            SA_dof = p * (n - 1)
            BxSA_dof = p * (q - 1) * (n - 1)

            # same as CRFpq & size is equal #
            MSa = SSa / A_dof
            MSb = SSb / B_dof
            MSaxb = SSaxb / AxB_dof
             
            # These are new for SPF design
            MSsa = SSsa / SA_dof
            MSbxsa = SSbxsa / BxSA_dof

            # calculate F
            Fa = MSa / MSsa
            Fb = MSb / MSbxsa
            Faxb = MSaxb / MSbxsa

            # calculate p
            p_1 = calc_f.sf(Fa, A_dof, BxSA_dof)
            p_2 = calc_f.sf(Fb, B_dof, BxSA_dof)
            p_1x2 = calc_f.sf(Faxb, AxB_dof, BxSA_dof)

        else:
            '''
            data:

            data['a1-b1'] = [3,3,1,3,5]
            data['a1-b2'] = [4,3,4,5,7]
            data['a2-b3'] = [6,6,6,4,8]
            data['a2-b4'] = [5,7,8,7,9]
            data['a2-b1'] = [3,5,2,4]
            data['a2-b2'] = [2,6,3,6]
            data['a2-b3'] = [3,2,3,6]
            data['a2-b4'] = [2,3,3,4]

            label_a = ["a1", "a2"]
            label_b = ["b1", "b2", "b3", "b4"]

            results:
            Major Effect A
            Error of Major Effect A S(A)
            Major Effect B
            Interaction  AxB
            Error        BxS(A)

            requires:
            p: number of each condition A
            q: number of each condition B
            SA_dof: p * (n - 1)
            A_dof:   dof of category A
            B_dof:   dof of category B
            AxB_dof: dof of AxB
            BxSA_dof: p * (q - 1) * (n - 1)
            unweighted_mean: list of mean value per condition (condition: a1-b1, a1-b2, a1-b3, a1-b4, a2-b1, a2-b2, a2-b3, a2-b4)

            ABS: squared sum of all the data
            Sij: total sum of data per subject
            AS: sum of Sij^2 / q
            AB: squared sum of each condition / sample num per condition (condition: a1-b1, a1-b2, a1-b3, a1-b4, a2-b1, a2-b2, a2-b3, a2-b4)
            A_sum: category1 sum list
            B_sum: category2 sum list
            n_j: list of sample number (category A)
            A: Aj^2 / nj * q (j=0~len(A_sum), Aj: A_sum[j], sum list of category A)

            G_dash: sum of non-weighted average per condition
            X_dash: G_dash^2 / p * q
            A_dash: q * Aj^2 (j=0~len(A_sum), Aj: A_sum[j], sum list of category A)
            B_dash: p * Bk^2 (k=0~len(B_sum), Bk: B_sum[k], sum list of category B)
            AB_dash: squared sum of unweighted_mean
            n_tilde: p / (sum of 1/n_j[i])

            SSsa: AS - A
            SSbxsa: ABS - AB - AS + A
            SSa:   n_tilde * (A_dash -X_dash)
            SSb:   n_tilde * (B_dash -X_dash)
            SSaxb: n_tilde * (AB_dash - A_dash - B_dash + X_dash)

            MSa = SSa / A_dof
            MSsa = SSsa / SA_dof
            MSb = SSb / B_dof
            MSaxb = SSaxb / AxB_dof
            MSbxsa = SSbxsa / BxSA_dof

            Fa = MSa / MSsa
            Fb = MSb / MSbxsa
            Faxb = MSaxb / MSbxsa
            '''
            # A: Aj^2 / nj * q
            A = 0.0
            for i in range(len(A_sum)):
                A += pow(A_sum[i], 2.0) / (n_j[i] * q)

            # unweighted_mean
            unweighted_mean = []
            for i in data.keys():
                unweighted_mean.append(sum(data[i]) / float(len(data[i])))

            A_sum = utils.condition_sum_of_unweighted_mean(data, label_A, unweighted_mean)
            B_sum = utils.condition_sum_of_unweighted_mean(data, label_B, unweighted_mean)

            # G_dash: sum of non-weighted average per condition
            G_dash = sum(unweighted_mean)

            # X_dash: G_dash^2 / p * q
            X_dash = pow(G_dash, 2.0) / (p * q)

            # A_dash: q * Aj^2 (j=0~len(A_sum), Aj: A_sum[j], sum list of category A)
            A_dash = 0.0
            for i in range(len(A_sum)):
                A_dash += pow(A_sum[i], 2.0)
            A_dash *= q

            # B_dash: p * Bk^2 (k=0~len(B_sum), Bk: B_sum[k], sum list of category B)
            B_dash = 0.0
            for i in range(len(B_sum)):
                B_dash += pow(B_sum[i], 2.0)
            B_dash *= p
        
            # AB_dash: squared sum of unweighted_mean
            AB_dash = 0.0
            for i in range(len(unweighted_mean)):
                AB_dash += pow(unweighted_mean[i], 2.0)
            
            # n_tilde: p / (sum of 1/n_j[i])
            tmp = 0.0
            for i in range(len(n_j)):
                tmp += 1.0 / n_j[i]
            n_tilde = p / tmp

            # calculate SS
            SSsa = AS - A
            SSbxsa = ABS - AB - AS + A
            SSa = n_tilde * (A_dash - X_dash)
            SSb = n_tilde * (B_dash - X_dash)
            SSaxb = n_tilde * (AB_dash - A_dash - B_dash + X_dash)

            N = sum(n_j) 
            SA_dof = N - p
            BxSA_dof = (N - p) * (q - 1)

            # calculate MS
            MSsa = SSsa / SA_dof
            MSa = SSa / A_dof
            MSb = SSb / B_dof
            MSaxb = SSaxb / AxB_dof
            MSbxsa = SSbxsa / BxSA_dof

            # calculate F
            Fa = MSa / MSsa
            Fb = MSb / MSbxsa
            Faxb = MSaxb / MSbxsa

            # calculate p
            p_1 = calc_f.sf(Fa, A_dof, BxSA_dof)
            p_2 = calc_f.sf(Fb, B_dof, BxSA_dof)
            p_1x2 = calc_f.sf(Faxb, AxB_dof, BxSA_dof)
        
        return SSa, SSsa, SSb, SSaxb, SSbxsa, A_dof, SA_dof, B_dof, AxB_dof, BxSA_dof, MSa, MSsa, MSb, MSaxb, MSbxsa, Fa, Fb, Faxb, p_1, p_2, p_1x2

