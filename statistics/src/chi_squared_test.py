#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import numpy as np
import sys

class ChiSquaredTest:
    def test(self, data):
        """
        """
        # check component type is 2
        if len(data.keys()) != 2 and len(data[(data.keys())[0]]) != 2 and len(data[(data.keys())[1]]) != 2: 
            print "Please check the component num of your data."
            print "The number of data type should be two."
            sys.exit()
        else:
            # convert dict to list
            # data = {"Yes": [a, c], "No": [b, d]} -> data_tmp = [[a, b], [c, d]]
            data1 = []
            data2 = []
            for i in range(len(data[(data.keys())[0]])):
                data1.append(data[(data.keys())[0]][i])

            for i in range(len(data[(data.keys())[1]])):
                data2.append(data[(data.keys())[1]][i])
            data_tmp = [data1, data2]
            squared, p, dof, ef = stats.chi2_contingency(data_tmp)
            # squared: 検定統計量
            # p: p value
            # dof: 自由度
            # ef: 期待度数
            print "chi_squared: " + str(squared)
            print "p_value: " + str(p)
            return p
