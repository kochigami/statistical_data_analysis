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
        if len(data.keys()) != 2:
            print "len(data.keys()) should be two"
            sys.exit()
        elif len(data[(data.keys())[0]]) != len(data[(data.keys())[1]]): 
            print "len(data[(data.keys())[0]]) and len(data[(data.keys())[1]]) should be same"
            sys.exit()
        else:
            '''
                        Non-social   Antisocial     Total                                                                                                    
            -------------------------------------------------                                                                                                          
            Teacher       1 (a)       12 (b)      13 (a+b)
            Counselor     4 (c)        6 (d)      10 (c+d)
            -------------------------------------------------                                                                                                        
            Total         5 (a+c)     18 (b+d)    23 (a+b+c+d)

            OrderedDict([('Teacher', [1, 12]), ('Counselor', [4, 6])]) 
            convert dict to list
            data= {'Teacher': [a, b], 'Counselor': [c, d]} => data_tmp = [[a, b], [c, d]]
            '''
            data1 = []
            data2 = []
            for i in range(len(data[(data.keys())[0]])):
                data1.append(data[(data.keys())[0]][i])

            for i in range(len(data[(data.keys())[1]])):
                data2.append(data[(data.keys())[1]][i])

            data_tmp = [data1, data2]
            '''
            # squared: 検定統計量
            # p: p value
            # dof: 自由度
            # ef: 期待度数
            '''
            squared, p, dof, ef = stats.chi2_contingency(data_tmp)
            print "chi_squared: {}".format(squared)
            print "dof: {}".format(dof)
            print "p_value: {}".format(p)
            return p
