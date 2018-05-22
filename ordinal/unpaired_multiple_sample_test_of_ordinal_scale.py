#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import sys
from interval_and_ratio.multiple_comparison import MultipleComparison
import numpy
from collections import OrderedDict

"""
Kruskal-Wallis test

H, p= stats.mstats.kruskalwallis(data[0], data[1], data[2])
"""

class UnpairedMultipleSampleTestOfOrdinalScale:
    '''
    calc_ave:
    calculate average order

    [ex]
    diff:  [-1, +31, +23, +2, -5, +5]
    order: [1, 6, 5, 2, 3.5, 3.5]
    3.5 = (3 + 4) / 2
    (i: 3, count: 2)
    '''
    def calc_ave(self, order, count, i):
        tmp_sum = 0.0
        for j in range(count):
            tmp_sum += i+1+j
        for j in range(count):
            order.append(tmp_sum / float(count))

    def test(self, data, threshold=0.05):
        """
        data = {"A": [3.88,4.60,6.30,2.15,4.80,5.20], "B": [2.86,9.02,4.27,9.86,3.66,5.48], "C": [1.82,4.21,3.10,1.99,2.75,2.18]}

        conditionA: [3.88,4.60,6.30,2.15,4.80,5.20]
        conditionB: [2.86,9.02,4.27,9.86,3.66,5.48]
        conditionC: [1.82,4.21,3.10,1.99,2.75,2.18]

        example % () is rank
                 A         B           C
                -------------------------------
                3.88 (9)   2.86 (6)   1.82 (1)
                4.60 (12)  9.02 (17)  4.21 (10)
                6.30 (16)  4.27 (11)  3.10 (7)
                2.15 (3)   9.86 (18)  1.99 (2)
                4.80 (13)  3.66 (8)   2.75 (5)
                5.20 (14)  5.48 (15)  2.18 (4)
                -------------------------------        
        n_j  |    6          6          6
        R_j  |    67         75         29
        """

        '''
        N: sum of n_j (j=A,B,C) (ex. 18)
        sample_num_per_condition: [n_A, n_B, n_C]
        all_data: [3.88, 4.60, 6.30, ..., 2.18]
        '''
        all_data = []        
        sample_num_per_condition = []
        N = 0.0
        for i in range(len(data.keys())):
            sample_num_per_condition.append(len(data[(data.keys())[i]]))
            N += len(data[(data.keys())[i]])
            for j in range(len(data[(data.keys())[i]])):
                all_data.append(data[(data.keys())[i]][j])

        sorted_all_data = sorted(all_data)
        
        '''
        calculate order
        order = [9, 12, 16, 3, 13, 14, ... , 4]
        '''
        '''
        (1) check whether right and left component of a target component are same
        ex [a, b, b, c]
        => a: a vs b
        => b: a vs b, b vs b (set 1)
        => b: b vs b (set 1), b vs c
        => c: b vs c

        ==> [0, 1, 1, 0]
        '''
        order = []
        tmp = []
        if abs(sorted_all_data[0]) == abs(sorted_all_data[1]):
            tmp.append(1)
        else:
            tmp.append(0)

        for i in range(1, len(sorted_all_data)-1):
            if abs(sorted_all_data[i]) == abs(sorted_all_data[i+1]) or abs(sorted_all_data[i-1]) == abs(sorted_all_data[i]):
                tmp.append(1)
            else:
                tmp.append(0)

        if abs(sorted_all_data[len(sorted_all_data) -1]) == abs(sorted_all_data[len(sorted_all_data) -2]):
            tmp.append(1)
        else:
            tmp.append(0)

        '''
        (2) if 1 is found, calculate average order
        '''
        count = 1
        for i in range(len(tmp)-1):
            if tmp[i+count-1] == 1:
                count = 1
                for j in range(i+count-1, len(tmp)-1):
                    if tmp[j] == tmp[j+1]:
                        count += 1
                    else:
                        self.calc_ave(order, count, i)
                        break
            else:
                order.append(i+count-1.0+1.0)
                if i == len(tmp)-2:
                    '''
                    if last component of list is 0, we have to add the rank of last component here.
                    '''
                    order.append((i+1.0)+count-1.0+1.0)

        '''
        initializing all_rank
        all_rank = {"A":[], "B": [], "C":[]}
        '''
        all_rank = OrderedDict()
        for i in data.keys():
            all_rank[i] = []

        '''
        compare sorted_all_data and data
        if two values matches, fetch the order of sorted_all_data from order
        '''
        for i in range(len(sorted_all_data)):
            for j in range(len(data.keys())):
                for k in range(len(data[(data.keys())[j]])):
                    if sorted_all_data[i] == data[(data.keys())[j]][k]:
                        (all_rank[(all_rank.keys())[j]]).append(order[i])

        '''
        calculate H value
        '''
        H = 0.0
        for i in range(len(all_rank.keys())):
            print "mean rank ({}) : {}".format((all_rank.keys())[i], numpy.mean(all_rank[(all_rank.keys())[i]]))
            H += pow(sum(all_rank[(all_rank.keys())[i]]), 2.0) / len(all_rank[(all_rank.keys())[i]])
        H *= 12.0 / (N * (N + 1.0)) 
        H -= 3.0 * (N + 1.0)
        print "H value: {}".format(H)
        
        '''
        add conditions based on N and the number of conditions
        reference: https://kusuri-jouhou.com/statistics/ichigen.html
        '''
        p = -1.0
        if N == 17 or N < 17 and len(data.keys()) == 3:
            print "Please refer the ditribution list of H value from Kruskal-Wallis test"
            print "ex. https://kusuri-jouhou.com/statistics/bunpuhyou2.html"
        else:
            p = stats.chi2.cdf(H, N - 1.0)
            print "p value: {}".format(p)

            if p < threshold:
                multiple_comparison = MultipleComparison()
                multiple_comparison.test(data, test="mann-whitney")

        return p
