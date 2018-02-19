#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import sys
from multiple_comparison import MultipleComparison

"""
Chi-squared test
"""

class UnpairedMultipleSampleTestOfNominalScale:
    def test(self, data, threshold=0.05):
        """
        data = {"Yes": [a,d,g], "No": [b,e,h], "Yes&No": [c,f,i]}
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
        sum_column = []

        len_max = -1000
        for i in range(len(data.keys())):
            if len(data[(data.keys())[i]]) > len_max:
                len_max = len(data[(data.keys())[i]])

        sum_row = [0 for i in range(len_max)]
        
        for i in range(len(data.keys())):
            sum_column.append(sum(data[(data.keys())[i]]))
            for j in range(len(data[(data.keys())[i]])):
                sum_row[j] += data[(data.keys())[i]][j]

        N = sum(sum_row)

        is_data_category_size_equal = True
        for i in range(len(data.keys())):
            if len(data[(data.keys())[0]]) != len(data[(data.keys())[i]]):
                is_data_category_size_equal = False

        if is_data_category_size_equal == False:
            print "Please check your data again. Data should be equal size per each condition."
            sys.exit()
        else:
            chi_squared = 0.0
            for i in range(len(data.keys())):
                for j in range(len(data[(data.keys())[i]])):
                    chi_squared += (data[(data.keys())[i]][j] * data[(data.keys())[i]][j]) / float (sum_row[j] * sum_column[i])  
            chi_squared -= 1.0
            chi_squared *= N
            df = (len(sum_row) - 1.0) * (len(sum_column) - 1.0)
            p = 1.0 - stats.chi2.cdf(chi_squared, df)
            print "chi_squared: " + str(chi_squared)
            print "df: " + str(df)
            print "p: " + str(p)

            if p < threshold:
                multiple_comparison = MultipleComparison()
                multiple_comparison.test(data, test="chi-squared")
            
            return p
