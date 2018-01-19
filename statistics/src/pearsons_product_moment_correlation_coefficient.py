#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import math

"""
Pearson's product-moment correlation coefficient
.0 <&= |r| <&= .2　ほとんど相関なし
.2   < |r| <&= .4　弱い相関あり
.4   < |r| <&= .7　比較的強い相関あり
.7   < |r| <&= 1.0 強い相関あり
"""

class PearsonsProductMomentCorrelationCoefficient:
    def test(self, data):
        """
        data = [[3,1], [2,4], [0,1], [2,3], [3,6], [5,5], [4,3], [6,5], [3,5], [1,2]]
        example
                1 2 3 4  5  6  7  8  9  10 | sum | sum of square |
            -----------------------------------------------------
            x   3 2 0 2  3  5  4  6  3  1  | 29  | 113           |
            y   1 4 1 3  6  5  3  5  5  2  | 35  | 151           |
            -----------------------------------------------------
            xy  3 8 0 6 18 25 12 30 15  2  | 119
        """        
        sum_x = 0.0
        sum_y = 0.0
        sum_x_squared = 0.0
        sum_y_squared = 0.0
        sum_xy = 0.0
        for i in range(len(data)):
            sum_x += data[i][0]
            sum_y += data[i][1]
            sum_xy += data[i][0] * data[i][1]
            sum_x_squared += data[i][0] * data[i][0]
            sum_y_squared += data[i][1] * data[i][1]

        r = float(len(data)) * sum_xy - sum_x * sum_y
        r /= math.sqrt(len(data) * sum_x_squared - sum_x * sum_x) * math.sqrt(len(data) * sum_y_squared - sum_y * sum_y)
        print "r value: " + str(r)

        return r
