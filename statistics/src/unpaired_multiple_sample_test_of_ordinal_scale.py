#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import sys
import copy

"""
Kruskal-Wallis test

H, p= stats.mstats.kruskalwallis(data[0], data[1], data[2])
"""

class UnpairedMultipleSampleTestOfOrdinalScale:
    def test(self, data):
        """
        data = [[3.88,4.60,6.30,2.15,4.80,5.20], [2.86,9.02,4.27,9.86,3.66,5.48], [1.82,4.21,3.10,1.99,2.75,2.18]]

        [3.88,4.60,6.30,2.15,4.80,5.20]: conditionA
        [2.86,9.02,4.27,9.86,3.66,5.48]: conditionB
        [1.82,4.21,3.10,1.99,2.75,2.18]: conditionC

        example
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
        all_data = []        
        sample_num_per_condition = []

        N = 0.0
        for i in range(len(data)):
            sample_num_per_condition.append(len(data[i]))
            N += len(data[i])
            for j in range(len(data[i])):
                all_data.append(data[i][j])
        
        sorted_all_data = []
        # sort all_data
        all_data.sort()
        sorted_all_data = all_data

        data_copy = copy.deepcopy(data)
        all_data_order = data
        data = data_copy

        for i in range(len(sorted_all_data)):
            for j in range(len(data)):
                for k in range(len(data[j])):
                    if sorted_all_data[i] == data[j][k]:
                        all_data_order[j][k] = i+1.0

        # calc H value            
        H = 0.0
        for i in range(len(all_data_order)):
            # sum of order in each category
            H += sum(all_data_order[i]) * sum(all_data_order[i]) / len(all_data_order[i])
        H *= 12.0 / (N * (N + 1.0)) 
        H -= 3.0 * (N + 1.0)
        print "H value: " + str(H)
        
        # https://kusuri-jouhou.com/statistics/ichigen.html
        if N == 17 or N < 17 and len(data) == 3:
            print "Please refer the ditribution list of H value from Kruskal-Wallis test"
            print "ex. https://kusuri-jouhou.com/statistics/bunpuhyou2.html"
        else:
            p = stats.chi2.cdf(H, N - 1.0)
            print "p value: " + str(p)

        return H
