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
CRF: completely randomized factorial design

reference: 心理学のためのデータ解析テクニカルブック　 森 敏昭, 吉田 寿夫編著　北大路書房 p. 94-107
'''
class CRF_pq:
    def test(self, data, label_A, label_B, mode="equal"):
        # calculate common variables for both modes
        utils = Utils()

        # number of each condition A, B
        p = utils.condition_type_num(label_A)
        q = utils.condition_type_num(label_B)

        # ABS: squared sum of all the data
        ABS = utils.ABS(data)

        # AB: squared sum of each condition / sample num per condition (condition: NAO-Adult, NAO-Children, Pepper-Adult, Pepper-Children)
        AB = utils.AB(data)

        # dof
        A_dof = p - 1
        B_dof = q - 1
        AxB_dof = A_dof * B_dof

        if mode == "equal":
            '''
            data:

            data['a1-b1'] = [3,3,1,3,5]
            data['a1-b2'] = [4,3,4,5,7]
            data['a1-b3'] = [6,6,6,4,8]
            data['a1-b4'] = [5,7,8,7,9]
            data['a2-b1'] = [3,5,2,4,6]
            data['a2-b2'] = [2,6,3,6,4]
            data['a2-b3'] = [3,2,3,6,5]
            data['a2-b4'] = [2,3,3,4,6]

            label_A: ['a1', 'a2']
            label_B: ['b1', 'b2', 'b3', 'b4']

            results:
            Major Effect A
            Major Effect B
            Interaction  AxB
            Error        WC

            requires:
            n: number of data per category
            p: number of each condition A
            q: number of each condition B
            ABS: squared sum of all the data
            AB: squared sum of each condition / sample num per condition (condition: a1-b1, a1-b2, a1-b3, a1-b4, a2-b1, a2-b2, a2-b3, a2-b4)
            G: sum of all the data
            X: G^2 / npq
            A: Aj^2 / nq (j=0~len(A_sum), Aj: A_sum[j], sum list of category A)
            B: Bi^2 / np (i=0~len(B_sum), Bi: B_sum[i], sum list of category B)
            WC_dof: pq (n-1)

            SSa:   A-X
            SSb:   B-X
            SSaxb: AB-A-B+X
            SSwc:  ABS-AB
            SSt:   ABS-X

            MSa:   SSa / (p-1)
            MSb:   SSb / (q-1)
            MSaxb: SSaxb / (p-1) * (q-1)
            MSwc:  SSwc / WC_dof

            Fa:   MSa / MSwc
            Fb:   MSb / MSwc
            Faxb: MSaxb / MSwc
            '''

            # G: sum of all the data
            G = utils.G(data)

            # n: number of data per category
            # focus on (data.keys()[0]) in this case
            # because the number of data per each category is equal
            n = len(data[(data.keys()[0])])

            # WC_dof: dof of Error
            # WC_dof = T_dof - A_dof - B_dof - AxB_dof
            # = (npq-1) - (p-1) - (q-1) - (p-1)(q-1)
            # = npq-p-q-pq+p+q = npq - pq = pq (n-1)
            WC_dof = utils.WC_dof(p, q, n)

            # X: G^2 / npq
            X = utils.X(G, p, q, n)

            # A_sum: sum list of category A
            A_sum = utils.condition_sum(data, label_A)

            # A: Aj^2 / nq (j=0~len(A_sum), Aj: A_sum[j])
            A = 0.0
            for i in range(len(A_sum)):
                A += pow(A_sum[i], 2.0) / (n * q)

            # B_sum: sum list of category B
            B_sum = utils.condition_sum(data, label_B)

            # B: Bi^2 / np (i=0~len(B_sum), Bi: B_sum[i])
            B = 0.0
            for i in range(len(B_sum)):
                B += pow(B_sum[i], 2.0) / (n * p)

            # calculate each sum of square
            SSa = A - X
            SSb = B - X
            SSaxb = AB - A - B + X
            SSwc = ABS - AB
            SSt = ABS - X

            # calculate each mean square
            MSwc = SSwc / WC_dof
            MSa = SSa / A_dof
            MSb = SSb / B_dof
            MSaxb = SSaxb / AxB_dof

            # calculate F value
            Fa = MSa / MSwc
            Fb = MSb / MSwc
            Faxb = MSaxb / MSwc

            # calculate p value
            p_1 = calc_f.sf(Fa, A_dof, WC_dof)
            p_2 = calc_f.sf(Fb, B_dof, WC_dof)
            p_1x2 = calc_f.sf(Faxb, AxB_dof, WC_dof)
            
        else:
            '''
            data:

            data['a1-b1'] = [6,6,4,8,7,5]
            data['a1-b2'] = [3,1,2,2]
            data['a2-b1'] = [5,4,5,4]
            data['a2-b2'] = [5,2,4,6,3,4]

            label_A: ['a1', 'a2']
            label_B: ['b1', 'b2']

            results:
            Major Effect A
            Major Effect B
            Interaction  AxB
            Error        WC

            requires:
            p: number of each condition A
            q: number of each condition B
            ABS: squared sum of all the data
            AB: squared sum of each condition / sample num per condition (condition: a1-b1, a1-b2, a2-b1, a2-b2)
            unweighted_mean: list of mean value per condition (condition: a1-b1, a1-b2, a2-b1, a2-b2)
            A_sum: list of unweighted mean of category A ['a1', 'a2']
            (A_sum('a1'): (unweighted_mean(a1-b1) + unweighted_mean(a1-b2)) / 2, A_sum('a2'): (unweighted_mean(a2-b1) + unweighted_mean(a2-b2)) / 2)
            B_sum: list of unweighted mean of category B ['b1', 'b2']
            (B_sum('b1'): (unweighted_mean(a1-b1) + unweighted_mean(a2-b1)) / 2, B_sum('b2'): (unweighted_mean(a1-b2) + unweighted_mean(a2-b2)) / 2)
            G_dash:  sum of all the data of unweighted_mean
            X_dash:  G_dash^2 / pq
            A_dash:  sum of q * A_sum[j]^2 (j=0~len(A_sum))
            B_dash:  sum of p * B_sum[i]^2 (i=0~len(B_sum))
            AB_dash: sum of unweighted_mean[i]^2 (i=0~len(unweighted_mean))
            n_tilde: adjusted n value, pq / sum of (1/njk) (j=0,..,len(A_sum), k=0,..,len(B_sum))
            N: total number of samples (ex. 20 in this example)
            WC_dof: N - p*q

            SSa:   n_tilde * (A_dash-X_dash)
            SSb:   n_tilde * (B_dash-X_dash)
            SSaxb: n_tilde * (AB_dash - A_dash -B_dash + X_dash)
            SSwc:  ABS - AB

            MSa:   SSa / (p-1)
            MSb:   SSb / (q-1)
            MSaxb: SSaxb / (p-1) * (q-1)
            MSwc:  SSwc / WC_dof

            Fa:   MSa / MSwc
            Fb:   MSb / MSwc
            Faxb: MSaxb / MSwc
            '''

            # the number of each condition is not same

            # unweighted_mean: list of mean value per condition
            # sum per each condition / number of data per each condition
            unweighted_mean = []
            for i in data.keys():
                unweighted_mean.append(sum(data[i]) / float(len(data[i])))

            # G_dash: sum of unweighted_mean
            G_dash = sum(unweighted_mean)

            # A_sum: list of unweighted mean [NAO, Pepper]
            A_sum = utils.condition_sum_of_unweighted_mean(data, label_A, unweighted_mean)
            # B_sum: list of unweighted mean [Adult, Children]
            B_sum = utils.condition_sum_of_unweighted_mean(data, label_B, unweighted_mean)

            # N: total number of samples
            N = 0
            for i in range(len(data.keys())):
                N += len(data[(data.keys())[i]])

            # WC_dof: dof of Error
            # N -(p-1) -(q-1) -(p-1)(q-1) = N -p +1 -q +1 -pq +p +q -1
            # = N -pq
            WC_dof = N - p * q

            # X_dash: G_dash^2 / pq
            X_dash = pow(G_dash, 2.0) / (p * q)

            # A_dash: q * Aj^2 (j=0,..,len(A_sum), Aj: A_sum[j])
            A_dash = 0.0
            for i in range(len(A_sum)):
                A_dash += pow(A_sum[i], 2.0)
            A_dash *= q

            # B_dash: p * Bi^2 (i=0,..,len(B_sum), Bi: B_sum[i])
            B_dash = 0.0
            for i in range(len(B_sum)):
                B_dash += pow(B_sum[i], 2.0)
            B_dash *= p

            # AB_dash: sum of unweighted_mean[j]^2 (j=0,..,len(unweighted_mean))
            AB_dash = 0.0
            for i in range(len(unweighted_mean)):
                AB_dash += pow(unweighted_mean[i], 2.0)

            # n_tilde: adjusted n value
            # pq / sum of (1/njk) (j=0,..,len(A_sum), k=0,..,len(B_sum))
            tmp = 0.0
            for i in range(len(data.keys())):
                tmp += 1.0 / len(data[(data.keys())[i]])
            n_tilde = p * q / tmp

            # calculate each sum of square
            SSa = n_tilde * float(A_dash - X_dash)
            SSb = n_tilde * float(B_dash - X_dash)
            SSaxb = n_tilde * float(AB_dash - A_dash - B_dash + X_dash)
            SSwc = ABS - float(AB)
            SSt = SSa + SSb + SSaxb + SSwc

            # calculate each mean square
            MSwc = SSwc / WC_dof
            MSa = SSa / A_dof
            MSb = SSb / B_dof
            MSaxb = SSaxb / AxB_dof

            # calculate F value
            Fa = MSa / MSwc
            Fb = MSb / MSwc
            Faxb = MSaxb / MSwc

            # calculate p value
            p_1 = calc_f.sf(Fa, A_dof, WC_dof)
            p_2 = calc_f.sf(Fb, B_dof, WC_dof)
            p_1x2 = calc_f.sf(Faxb, AxB_dof, WC_dof)

        return SSa, SSb, SSaxb, SSwc, SSt, A_dof, B_dof, AxB_dof, WC_dof, MSa, MSb, MSaxb, MSwc, Fa, Fb, Faxb, p_1, p_2, p_1x2
