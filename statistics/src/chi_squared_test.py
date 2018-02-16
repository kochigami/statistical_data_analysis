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
            a = data[(data.keys())[0]][0]
            c = data[(data.keys())[0]][1]
            b = data[(data.keys())[1]][0]
            d = data[(data.keys())[1]][1]
            data_tmp = [[a, b], [c, d]]
            squared, p, dof, ef = stats.chi2_contingency(data_tmp)
            # squared: 検定統計量
            # p: p value
            # dof: 自由度
            # ef: 期待度数
            print "chi_squared: " + str(squared)
            print "p_value: " + str(p)
            return p
