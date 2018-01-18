#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import math

"""
Spearman's rank correlation coefficient
"""

class SpearmansRankCorrelationCoefficient:
    def test(self, data):
        """
        data = [[4.3,3.9], [2.1,0.8], [1.4,0.9], [0.9,1.5], [0.5,0.5]]
        example
                     1 2  3 4 5 | sum | sum of square |
            -------------------------------------------
            x        1 2  3 4 5 | 15  | 55            |
            y        1 4  3 2 5 | 15  | 55            |
            -------------------------------------------
            d (=x-y) 0 -2 0 2 0 | 0   | 8
        """     
        N = len(data)
        sum_d_squared = 0.0
        list_of_x = []
        list_of_y = []

        for i in range(len(data)):
            list_of_x.append(data[i][0])
            list_of_y.append(data[i][1])

        list_of_x.sort()
        list_of_x.reverse()
        list_of_y.sort()
        list_of_y.reverse()

        for i in range(len(list_of_x)):
            for j in range(len(data)):
                if list_of_x[i] == data[j][0]:
                    data[j][0] = i + 1.0
        
        for i in range(len(list_of_y)):
            for j in range(len(data)):
                if list_of_y[i] == data[j][1]:
                    data[j][1] = i + 1.0

        for i in range(len(data)):
            sum_d_squared += (data[i][0] - data[i][1]) * (data[i][0] - data[i][1])

        r_s = 1.0 - ((6.0 * sum_d_squared) / (N * (N * N - 1.0))) 
        print "r value: " + str(r_s)
        return r_s
