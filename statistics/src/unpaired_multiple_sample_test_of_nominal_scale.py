#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import sys

"""
Chi-squared test
"""

class UnpairedMultipleSampleTestOfNominalScale:
    def test(self, data):
        """
        data = [[a,b,c], [d,e,f], [g,h,i]]
        example
                       Yes   No   Yes&No  Total (Sum row)
        ---------------------------------------
        Condition1     a     b      c     a+b+c
        Condition2     d     e      f     d+e+f
        Condition3     g     h      i     g+h+i
        ---------------------------------------
        Total        a+d+g  b+e+h   c+f+i (= a+b+c+d+e+f+g+h+i)
        (Sum column)
        """
        sum_row = []
        sum_column = [0 for i in range(len(data[0]))]
        
        for i in range(len(data)):
            sum_row.append(sum(data[i]))
            for j in range(len(data[i])):
                sum_column[j] += data[i][j]
        N = sum(sum_row)

        if 1 == 0:
            # TODO: check data length
            sys.exit()
        else:
            chi_squared = 0.0
            for i in range(len(data)):
                for j in range(len(data[i])):
                    chi_squared += (data[i][j] * data[i][j]) / float (sum_row[i] * sum_column[j])  
            chi_squared -= 1.0
            chi_squared *= N
            df = (len(sum_row) - 1.0) * (len(sum_column) - 1.0)
            p = 1.0 - stats.chi2.cdf(chi_squared, df)
            print "chi_squared: " + str(chi_squared)
            print "df: " + str(df)
            print "p: " + str(p)
            return p
