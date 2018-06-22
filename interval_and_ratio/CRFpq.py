#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scipy.stats import f as calc_f
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
        '''
        data: 

        data['NAO-Adult'] = [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90]
        data['NAO-Children'] = [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75]
        data['Pepper-Adult'] = [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75]
        data['Pepper-Children'] = [70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70]

        label_A: ["NAO", "Pepper"]
        label_B: ["Adult", "Children"]

        Major Effect A
        Major Effect B
        Interaction  AxB
        Error        WC
        '''
        # number of each condition A, B
        p = len(label_A)
        q = len(label_B)

        # ABS: squared sum of each sample
        ABS = 0.0
        for i in data.keys():
            for j in range(len(data[i])):
                ABS += pow((data[i])[j], 2.0)
        # AB: squared sum of each condition / sample num (condition: NAO-Adult, NAO-Children, Pepper-Adult, Pepper-Children)
        AB = 0.0
        for i in data.keys():
            AB += pow(sum(data[i]), 2.0) / len(data[i])

        # dof
        A_dof = p - 1
        B_dof = q - 1
        AxB_dof = A_dof * B_dof

        if mode == "equal":
            # G: sum of all the data
            G = 0.0
            for i in range(len(data.keys())):
                for j in range(len(data[(data.keys()[i])])):
                    G += (data[(data.keys()[i])])[j]

            # n: number of data per each category
            # focus on (data.keys()[0]) in this case
            # because the number of data per each category is equal
            n = len(data[(data.keys()[0])])

            # WC_dof: dof of Error
            # (npq-1) - (p-1) - (q-1) - (p-1)(q-1)
            # = npq-p-q-pq+p+q = npq - pq = pq (n-1)
            WC_dof = p * q * (n - 1.0)

            # X: G^2 / npq
            X = pow(G, 2.0) / (n * p * q)

            # A_sum: sum list of category A
            A_sum = []
            A_sum_tmp = 0.0
            for i in range(len(label_A)):
                for j in range(len(data.keys())):
                    if label_A[i] in (data.keys())[j]:
                        A_sum_tmp += sum(data[(data.keys())[j]])
                A_sum.append(A_sum_tmp)
                A_sum_tmp = 0.0

            # A: Aj^2 / nq (j=0~len(A_sum), Aj: A_sum[j])
            A = 0.0
            for i in range(len(A_sum)):
                A += pow(A_sum[i], 2.0) / (n * q)

            # B_sum: sum list of category B
            B_sum = []
            B_sum_tmp = 0.0
            for i in range(len(label_B)):
                for j in range(len(data.keys())):
                    if label_B[i] in (data.keys())[j]:
                        B_sum_tmp += sum(data[(data.keys())[j]])
                B_sum.append(B_sum_tmp)
                B_sum_tmp = 0.0

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
            # the number of each condition is not same

            # unweighted_mean: list of mean value per condition
            # sum per each condition / number of data per each condition
            unweighted_mean = []
            for i in range(len(data.keys())):
                unweighted_mean.append(sum(data[(data.keys())[i]]) / float(len(data[(data.keys())[i]])))

            # G_dash: sum of unweighted_mean
            G_dash = sum(unweighted_mean)

            # A_sum: list of unweighted mean [NAO, Pepper]
            A_sum_tmp = 0.0
            A_num_tmp = 0.0
            A_sum = []
            for j in range(len(label_A)):
                for i in range(len(data.keys())):
                    if label_A[j] in (data.keys())[i]:
                        A_sum_tmp += unweighted_mean[i]
                        A_num_tmp += 1
                # calculate unweighted mean per each condition of A (NAO, Pepper)
                A_sum_tmp = A_sum_tmp / A_num_tmp
                A_sum.append(A_sum_tmp)
                A_sum_tmp = 0.0
                A_num_tmp = 0.0

            # B_sum: list of unweighted mean [Adult, Children]
            B_sum_tmp = 0.0
            B_num_tmp = 0.0
            B_sum = []
            for j in range(len(label_B)):
                for i in range(len(data.keys())):
                    if label_B[j] in (data.keys())[i]:
                        B_sum_tmp += unweighted_mean[i]
                        B_num_tmp += 1
                # calculate unweighted mean per each condition of B (Adult, Children)
                B_sum_tmp = B_sum_tmp / B_num_tmp
                B_sum.append(B_sum_tmp)
                B_sum_tmp = 0.0
                B_num_tmp = 0.0

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
