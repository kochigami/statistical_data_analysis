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
         CM    |   A  B  C  D  E   sum
         -----------------------------
         person
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

        '''
        k: number of conditions (ex. [A,B,C,D,E] => 5)
        n: number of samples / condition (ex. A: [1,5,1,5,5,4,5] => 7)
        sum_of_order: T_j (ex. j = A,...,E)
        '''
        k = len(data.keys())
        n = len(data[(data.keys())[0]])
        sum_of_order = [0 for i in range(len(data.keys()))]

        '''
        calculate T_j and put each value in sum_of_order
        ex. sum_of_order = [T_A, ..., T_E] = [26, 16, 18, 22, 23]
        '''
        for i in range(len(data.keys())):
            for j in data[(data.keys())[i]]:
                sum_of_order[i] += j
        '''
        S = {12 / n*k*(k+1)} * (T_j)^2 (j=A,...,E) - 3*n*(k+1)
        S can be approximated chi-square distribution at dof: k-1
        '''
        S = 0.0
        for i in range(len(sum_of_order)):
            S += pow(sum_of_order[i], 2.0)
        S *= 12.0 / (n * k * (k + 1.0))
        S -= 3.0 * n * (k + 1.0)
        p = stats.chi2.cdf(S, k - 1.0)
        print "S value: {}".format(S)
        print "p value: {}".format(p)
        
        if p < threshold:
            multiple_comparison = MultipleComparison()
            multiple_comparison.test(data, test="signed-test")

        return p
