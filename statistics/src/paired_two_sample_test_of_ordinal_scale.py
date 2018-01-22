#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import sys
import copy

'''
signed rank sum test
'''

class PairedTwoSampleTestOfOrdinalScale:
    def test(self, data):
        """
        data = {'Product_A': [25, 62, 58, 26, 42, 18, 11, 33, 50, 34]
                'Product_B': [26, 31, 35, 24, 47, 13, 11, 21, 42, 18]}
        """
        x = data[(data.keys())[0]]
        y = data[(data.keys())[1]]
        # note: nx == ny
        nx = len(data[(data.keys())[0]])
        if len(x) != len(y):
            print "Please check the contents of your data."
            print "The number of data type should be two."
            sys.exit()
        else:
            diff = []
            for i in range(nx):
                if x[i] - y[i] != 0.0:
                    diff.append(x[i] - y[i])

            for i in range(len(diff)):
                for j in range(i+1, len(diff)):
                    if abs(diff[i]) > abs(diff[j]):
                        tmp = diff[i]
                        diff[i] = diff[j]
                        diff[j] = tmp

            # TODO: fix bug
            order = []            
            for i in range(len(diff)):
                tmp = 1
                for j in range(i+1, len(diff)):
                    if len(order) == 0:
                        if abs(diff[i]) == abs(diff[j]):
                            tmp +=1
                            print tmp
                    elif len(order) > 0 and order[len(order) -1] != diff[j]:
                        if abs(diff[i]) == abs(diff[j]):
                            tmp +=1
                print "hoge"
                print tmp
                val = 0.0
                for k in range(1, tmp):
                    val += i+k
                for l in range(1, tmp):
                    order.append(val / tmp)
            print diff
            print order
            ###

            t_plus = 0.0
            t_minus = 0.0
            for i in range(len(diff)):
                if diff[i] < 0.0:
                    t_minus += order[i]
                else:
                    t_plus += order[i]
            print t_minus
            print t_plus
            
            if t_minus < t_plus:
                t = t_minus
            else:
                t = t_plus
            
            print "t: " + str(t)
            print "n: " + str(len(diff))
            return True
