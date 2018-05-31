#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import sys
from multiple_comparison.multiple_comparison import MultipleComparison

"""
Chi-squared test
"""

class UnpairedMultipleSampleTestOfNominalScale:
    def test(self, data, threshold=0.05):
        # check component type is more than 2
        if len(data.keys()) <= 2:
            print "len(data.keys()) should be more than two (>= 3)"
            sys.exit()
        else:
            for i in range(len(data.keys())):
                if len(data[(data.keys())[0]]) != len(data[(data.keys())[i]]):
                    print "len(data[(data.keys())[0]]) and len(data[(data.keys())[{}]]) should be same".format(i)
                    sys.exit()

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
            data_tmp = []
            for i in data.keys():
                tmp = []
                for j in range(len(data[i])):
                    tmp.append(data[i][j])
                data_tmp.append(tmp)

            '''
            # squared: 検定統計量
            # p: p value
            # dof: 自由度
            # ef: 期待度数
            '''
            squared, p, dof, ef = stats.chi2_contingency(data_tmp)
            print "chi_squared: {}".format(squared)
            print "dof: {}".format(dof)
            # dof: (len(column) - 1) * (len(row) - 1)
            print "p_value: {}".format(p)
            return p

            if p < threshold:
                multiple_comparison = MultipleComparison()
                multiple_comparison.test(data, test="chi-square")
            
            return p
