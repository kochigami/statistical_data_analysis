#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import sys
from multiple_comparison.multiple_comparison import MultipleComparison

"""
Cochran's Q test
"""

class PairedMultipleSampleTestOfNominalScale:
    def test(self, data, threshold=0.05):
        """
        data["CandidateA"] = [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        data["CandidateB"] = [1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
        data["CandidateC"] = [1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0]
        ##data = [[1,1,1], [1,1,1], [0,1,1], [0,1,1], [0,1,1], [0,0,1], [0,0,1], [0,0,1], [0,0,1], [0,0,0], [0,0,0]]
        example
                  CandidateA  CandidateB  CandidateC  Total (sum_row)
        ---------------------------------------------------
        Subject1      1           1           1        3
        Subject2      1           1           1        3     
        Subject3      1           1           1        3     
        Subject4      1           1           1        3
        Subject5      1           0           1        2
        Subject6      1           0           1        2
        Subject7      0           1           1        2
        Subject8      0           1           1        2
        Subject9      0           1           1        2
        Subject10     0           1           1        2
        Subject11     0           1           0        1
        Subject12     0           1           0        1     
        Subject13     0           0           1        1     
        Subject14     0           0           1        1
        Subject15     0           0           1        1
        Subject16     0           0           1        1
        Subject17     0           0           0        0
        Subject18     0           0           0        0
        Subject19     0           0           0        0
        Subject20     0           0           0        0
        --------------------------------------------------
        Total         6          10           14       30
        (sum_column)

        1: agree 0: disagree
        """
        '''
        k: the number of conditions (ex: k = len(data.keys()) (= 3 in this example))
        sum_C_j: sum of each column (ex: sum_C_j = sum(data["CandidateA"]) + sum(data["CandidateB"]) + sum(data["CandidateC"]) = 30)
        sum_C_j2: squared sum of each column (ex: sum_C_j2 = sum(data["CandidateA"])^2 + sum(data["CandidateB"])^2 + sum(data["CandidateC"])^2)
        sum_R_j2: squared sum of each row (ex: sum_R_j2 = sum(data['Subject1'])^2 + ... + sum(data['Subject20'])^2)
        
        => q = ((k-1) * (k * sum_C_j2 - sum_C_j ** 2)) / (k * sum_C_j - sum_R_j2)
        '''

        k = len(data.keys())

        sum_C_j = 0.0
        sum_C_j2 = 0.0
        for i in range(k):
            sum_C_j += sum(data[data.keys()[i]])
            sum_C_j2 += sum(data[data.keys()[i]]) ** 2
        
        sum_R_j2 = 0.0
        # n: the number of column (data size of data['Candidate1'])
        # This test is executed under the hypothesis that data size of data['Candidate1'] == data size of data['Candidate2'] == data size of data['Candidate3']
        n = len(data[data.keys()[i]])
        for i in range(n):
            tmp = 0.0
            for j in range(k):
                tmp += data[data.keys()[j]][i]
            sum_R_j2 += tmp ** 2
        
        q = ((k-1) * (k * sum_C_j2 - sum_C_j ** 2)) / (k * sum_C_j - sum_R_j2)

        df = k - 1.0
        p = stats.chi2.pdf(q, df)
        # q can be an approximate of X^2
        print "X^2: {}".format(q)
        print "df: {}".format(df)
        print "p: {}".format(p)

        if p < threshold:
            multiple_comparison = MultipleComparison()
            multiple_comparison.test(data, test="cochran")
            
        return p
