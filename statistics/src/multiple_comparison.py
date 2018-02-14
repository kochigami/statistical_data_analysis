#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
import operator
from collections import OrderedDict

class MultipleComparison:
    def test(self, data, alpha=0.05):
        '''
        data: {A: [1,2,3], B: [2,4,6], ...} 
        
        alpha_dash = 2 * alpha / (m * ( r - 1 ))
        m: the number of step 
        r: the total number of step
        '''
        m = len(data.keys())
        data_average = {}
        data_new = OrderedDict()
        for r in range(m):
            data_average[(data.keys())[r]] = np.average(data[(data.keys())[r]])        
        data_tmp = sorted(data_average.items(), key=operator.itemgetter(1))
        for r in range(len(data_tmp)):
            data_new[(data_tmp[r])[0]] = (data_tmp[r])[1]
        
        print data
        print data_average
        print data_new

        for i in range(m):
            r = m - i
            if r > 1:
                print "r: " + str(r)
                for j in range(0, i+1):
                    # just print paired sample
                    # need to run test and get p value
                    print "1: "
                    print data_new[(data_new.keys())[j]]
                    print "2: "
                    print data_new[(data_new.keys())[j+r-1]]
                print "threshold is: " + str(2.0 * alpha / (m * ( r - 1 ))) # alpha_dash
                print "\n"

if __name__ == '__main__':
    multiple_comparison = MultipleComparison()
    #data = {"A": [12, 10, 8], "B": [5, 7, 20], "C": [7, 6, 7], "D": [1,3,4]}
    #data = {"A": [12, 10, 8], "B": [5, 7, 20], "C": [7, 6, 7]}
    data = {"A": [12, 10, 8], "B": [5, 7, 20], "C": [7, 6, 7], "D": [1,3,4], "E":[1,1,1]}
    multiple_comparison.test(data)
