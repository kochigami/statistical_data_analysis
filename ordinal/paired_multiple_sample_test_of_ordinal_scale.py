#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import sys
from interval_and_ratio.multiple_comparison import MultipleComparison

"""
Friedman test

"""

class PairedMultipleSampleTestOfOrdinalScale:
    def test(self, data, threshold=0.05):
        """
        
        data = {"A": [1,5,1,5,5,4,5], "B": [2,1,2,1,4,2,4], "C": [3,3,3,4,2,1,2], "D": [5,2,4,2,3,3,3], "E": [4,4,5,3,1,5,1]}

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
        k = len(data.keys())
        n = len(data[(data.keys())[0]])
        sum_of_order = [0 for i in range(len(data.keys()))]

        for i in range(len(data.keys())):
            for j in range(len(data[(data.keys())[i]])):
                sum_of_order[i] += data[(data.keys())[i]][j]
        S = 0.0
        for i in range(len(sum_of_order)):
            S += pow(sum_of_order[i], 2.0)
        S *= 12.0 / (n * k * (k + 1.0))
        S -= 3.0 * n * (k + 1.0)
        p = stats.chi2.cdf(S, k - 1.0)
        print "S value: " + str(S)
        print "p value: " + str(p)
        
        if p < threshold:
            multiple_comparison = MultipleComparison()
            multiple_comparison.test(data, test="signed-test")

        return p
