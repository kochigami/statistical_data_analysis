#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
import math
from scipy.stats import t as calc_p
from scipy.stats import f as calc_f
from utils import Utils
# referenced as calc_p because of the error below:
# File "/home/kochigami/my_tutorial/statistics/src/t_test/t_test.py", line 80, in unpaired_ttest
# p = t.sf(t_value, dof)
# UnboundLocalError: local variable 't' referenced before assignment
# t test
import operator

class OneWayAnova:
    '''
    data = {'Japanese': [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
            'English':  [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
            'French' :  [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75]}
    mode: string. CR or RB.
    
    CR: completely randomized design
    RB: randomized block design
    '''
    def one_way_anova(self, data, mode="CR", threshold=0.05, comparison_mode="holm"):
        utils = Utils()
        # if mode is RB, sample num should be same in each category
        if mode == "RB":
            for i in range(len(data.keys()) - 1):
                if len(data[(data.keys())[i]]) != len(data[(data.keys())[i+1]]):
                    print "Be sure that sample num of each category is same."
                    sys.exit()

        if mode == "CR":
            """
            completely randomized design (CR design)

                   | sum of squares |     dof     |    mean squares    |          F            |      
            ------------------------------------------------------------------------------------
            gunkan | ss_between     | between_dof | mean_square_between| ms_between/ ms_within |
            gunnai | ss_within      | within_dof  | mean_square_within |                       |
            -------|----------------------------------------------------------------------------
            total  | ss_b+ss_w      | b_dof+w_dof | 

            p: the number of condition
            n: the number of each data per condition
            """

            # p: the number of condition
            p = len(data.keys())

            # N: the total number of data in all the conditions
            N = 0.0
            for i in range(len(data.keys())):
                N += len(data[(data.keys())[i]])
            
            # G: total sum of all data
            G = utils.G(data)

            # X: G^2 / n*p
            X = pow(G, 2.0) / float(N)

            # AS: square sum of each data
            AS = 0.0
            for i in range(len(data.keys())):
                for j in range(len(data[(data.keys())[i]])):
                    AS += pow(data[(data.keys())[i]][j], 2.0)

            # A: sum of each category
            A = 0.0
            for i in range(len(data.keys())):
                A += pow(sum(data[(data.keys())[i]]), 2.0) / len(data[(data.keys())[i]])

            # calculate squared sum
            SSa = A - X
            SSwc = AS - A
            SSr = AS - X

            # calculate dof
            between_dof = p - 1
            total_dof = N - 1
            within_dof = total_dof - between_dof

            # calculate mean square
            MSa = SSa / between_dof
            MSwc = SSwc / within_dof
            F = MSa / MSwc

            # calculate p
            p = calc_f.sf(F, between_dof, within_dof)

            answer_list = [[math.ceil(SSa * 100.0) * 0.01, int(between_dof), math.ceil(MSa * 100.0) * 0.01, math.ceil(F * 100.0) * 0.01, math.ceil(p * 1000.0) * 0.001],
                           [math.ceil(SSwc * 100.0) * 0.01, int(within_dof), math.ceil(MSwc * 100.0) * 0.01, '--', '--'], 
                           [math.ceil((SSr) * 100.0) * 0.01, int(between_dof + within_dof),'--', '--', '--']]
            self.comparison(data, MSwc, between_dof, threshold, comparison_mode)
            return answer_list

        elif mode == "RB":
            """            
            randomized block (RB design)

                   | sum of squares |   dof       |     mean squares    |                   F                    |       
            ------------------------------------------------------------------------------------------------------
            youin  | ss_between     | between_dof | mean_square_between | mean_square_between/ mean_square_error |
            subject| ss_subject     | subject_dof | mean_square_subject |                                        |
            error  | ss_error       | error_dof   | mean_square_error   |                                        |
            ------------------------------------------------------------------------------------------------------
            Total  | ss_b+s+e       | b+s+e_dof   | 
            """
            
            # p: the number of condition
            p = len(data.keys())

            # n: the number of each data per condition
            # note: It is same in all the conditions in RB design.
            n = len(data[(data.keys())[0]])
            
            # G: total sum of all data
            G = utils.G(data)

            # X: G^2 / n*p
            X = pow(G, 2.0) / (float(p) * n)

            # AS: square sum of each data
            AS = 0.0
            for i in range(len(data.keys())):
                for j in range(len(data[(data.keys())[i]])):
                    AS += pow(data[(data.keys())[i]][j], 2.0)

            # A: sum of each category
            A = 0.0
            for i in range(len(data.keys())):
                A += pow(sum(data[(data.keys())[i]]), 2.0) / len(data[(data.keys())[i]])

            # S: sum of each data per subject
            S = 0.0
            for i in range(len(data[(data.keys())[0]])):
                tmp = 0.0
                for j in range(len(data.keys())):
                    tmp += data[(data.keys())[j]][i]
                S += pow(tmp, 2.0) / p

            # calculate squared sum
            SSs = S - X
            SSa = A - X
            SSres = AS - A - S + X
            SSr = AS - X

            # calculate dof (group type & sample number of each type)
            between_dof = p - 1.0
            subject_dof = n - 1.0
            error_dof =  n * p - 1 - between_dof - subject_dof

            # calculate mean square
            MSa = SSa / between_dof
            MSs = SSs / subject_dof
            MSres = SSres / error_dof 
            Fa = MSa / MSres
            Fs = MSs / MSres

            # calculate p
            pa = calc_f.sf(Fa, between_dof, error_dof)
            ps = calc_f.sf(Fs, subject_dof, error_dof)
 
            answer_list = [[math.ceil(SSa *100.0) *0.01, int(between_dof), math.ceil(MSa *100.0) *0.01, math.ceil(Fa *100.0) *0.01, math.ceil(pa *1000.0) *0.001],
                           [math.ceil(SSs *100.0) *0.01, int(subject_dof), math.ceil(MSs *100.0) *0.01, math.ceil(Fs *100.0) *0.01, math.ceil(ps *1000.0) *0.001],
                           [math.ceil(SSres *100.0) *0.01, int(error_dof), math.ceil(MSres *100.0) *0.01, '--', '--'],
                           [math.ceil((SSa + SSs + SSres) *100.0) *0.01, int(between_dof + subject_dof + error_dof),'--', '--', '--']]
            self.comparison(data, SSa, between_dof, threshold, comparison_mode)
            self.comparison(data, SSs, subject_dof, threshold, comparison_mode)
            return answer_list

        else:
            print "Please choose mode 'CR' or 'RB'."
            return False

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
        """
        average = []
        num = []
        for i in range(len(data.keys())):
            average.append(np.mean(data[(data.keys())[i]]))
            num.append(len(data[(data.keys())[i]]))
        
        pairs = {}
        dof = {}
        for i in range(len(data.keys())):
            for j in range(i+1, len(data.keys())):
                pairs[str((data.keys())[i]) + " + " + str((data.keys())[j])] = abs(average[i] - average[j]) / math.sqrt(mean_square_between * ((1.0 / num[i]) + (1.0 / num[j])))
                dof[str((data.keys())[i]) + " + " + str((data.keys())[j])] = num[i] + num[j] -2
        p = {}
        for i in range(len(pairs.keys())):
            p[str((pairs.keys())[i])] = calc_p.sf(pairs[(pairs.keys())[i]], dof[(pairs.keys())[i]])

        modified_threshold = []
        for i in range(len(pairs.keys())):
            if mode == "bonferroni":
                modified_threshold.append(threshold / len(pairs.keys()))
            elif mode == "holm":
                modified_threshold.append(threshold / (len(pairs.keys()) - i))
            else:
                print "Please choose bonferroni or holm."
                sys.exit()

        tmp = 0
        # ref: https://docs.python.org/2/howto/sorting.html (Operator Module Functions)
        for i, j in sorted(p.items(), key=operator.itemgetter(1)):
            if j < modified_threshold[tmp]:
                print("key: " + str(i) + " t: " + str(pairs[i]) + " p: " + str(j) + " threshold: " + str(modified_threshold[tmp]) + " O")
            else:
                print("key: " + str(i) + " t: " + str(pairs[i]) + " p: " + str(j) + " threshold: " + str(modified_threshold[tmp]) + " X")
                if mode == "holm":
                    print "test ends here."
                    break
            tmp += 1

        print "Note that if holm, test finishes once p value is larger than threshold p."

if __name__ == '__main__':
    pass
