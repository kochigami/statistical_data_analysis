#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import sys

"""
Cochran's Q test
"""

class PairedMultipleSampleTestOfNominalScale:
    def test(self, data):
        """
        data = [[1,1,1], [1,1,1], [0,1,1], [0,1,1], [0,1,1], [0,0,1], [0,0,1], [0,0,1], [0,0,1], [0,0,0], [0,0,0]]
        example
                  CandidateA  CandidateB  CandidateC  Total (sum_row)
        ---------------------------------------------------
        Subject1      1           1           1        3
        Subject2      1           1           1        3     
        Subject3      0           1           1        2     
        Subject4      0           1           1        2
        Subject5      0           1           1        2
        Subject6      0           0           1        1
        Subject7      0           0           1        1
        Subject8      0           0           1        1
        Subject9      0           0           0        0
        Subject10     0           0           0        0
        --------------------------------------------------
        Total         2           5           8       15
        (sum_column)

        1: agree 0: disagree
        """
        sum_row = []
        sum_column = [0 for i in range(len(data[0]))]
        
        for i in range(len(data)):
            sum_row.append(sum(data[i]))
            for j in range(len(data[i])):
                sum_column[j] += data[i][j]
        k = len(sum_column)
        # in this example, k is 3

        is_data_size_equal = True
        for i in range(len(data)):
            if len(data[0]) != len(data[i]):
                is_data_size_equal = False
        if is_data_size_equal == False:
            print "Please check your data again. Data have to be same size per each subject."
            sys.exit()
        else:
            q_tmp1 = 0.0
            q_tmp2 = 0.0

            for i in range(len(sum_column)):
                q_tmp1 += sum_column[i] * sum_column[i]
                q_tmp2 += sum_column[i]
                
            q = (k - 1.0) * abs(k * q_tmp1 - pow(q_tmp2, 2.0))

            q_tmp3 = 0.0
            for j in range(len(sum_row)):
                q_tmp3 += sum_row[j] * sum_row[j]

            q /= k * q_tmp2 - q_tmp3

            df = k - 1.0
            p = 1.0 - stats.chi2.cdf(q, df)
            print "q: " + str(q)
            print "df: " + str(df)
            print "p: " + str(p)
            return p
