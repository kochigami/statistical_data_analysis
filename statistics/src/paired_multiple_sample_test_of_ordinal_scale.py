#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import sys
import copy

"""
Friedman test

"""

class PairedMultipleSampleTestOfOrdinalScale:
    def test(self, data):
        """
        data = [[1,2,3,5,4], [5,1,3,2,4], [1,2,3,4,5], [5,1,4,2,3], [5,4,2,3,1], [4,2,1,3,5], [5,4,2,3,1]]

        example
                   A  B  C  D  E   sum
                ---------------------
             p1    1, 2, 3, 5, 4 | 15
             p2    5, 1, 3, 2, 4 | 15
             p3    1, 2, 3, 4, 5 | 15
             p4    5, 1, 4, 2, 3 | 15
             p5    5, 4, 2, 3, 1 | 15
             p6    4, 2, 1, 3, 5 | 15
             p7    5, 4, 2, 3, 1 | 15
                ---------------------        
            T_j  | 26 16 18 22 23| 105 
        """
        n = len(data)
        k = len(data[0])
        sum_of_order = [0 for i in range(len(data[0]))]

        # sort data[i] and input order instead of raw value
        for i in range(len(data)):
            data_i_copy = copy.deepcopy(data[i])
            data_i_copy.sort()
            for j in range(len(data_i_copy)):
                # we cannot use k because we used it as a variable
                for h in range(len(data[i])):
                    if data_i_copy[j] == data[i][h]:
                        data[i][h] = j + 1.0

        for i in range(len(data)):
            for j in range(len(data[i])):
                sum_of_order[j] += data[i][j]

        S = 0.0
        for i in range(len(sum_of_order)):
            S += sum_of_order[i] * sum_of_order[i]
        S *= 12.0 / (n * k * (k + 1.0))
        S -= 3.0 * n * (k + 1.0)
        p = stats.chi2.cdf(S, k - 1.0)
        print "S value: " + str(S)
        print "p value: " + str(p)
        
        return S
