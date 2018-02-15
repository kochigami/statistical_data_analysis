#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
import operator
from collections import OrderedDict
from paired_two_sample_test_of_nominal_scale import PairedTwoSampleTestOfNominalScale

class MultipleComparison:
    def test(self, data, test="none", alpha=0.05):
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
        
        for i in range(m):
            r = m - i
            if r > 1:
                print "r: " + str(r)
                for j in range(0, i+1):
                    # just print paired sample
                    # need to run test and get p value
                    test_data = OrderedDict()
                    test_data[(data_new.keys())[j]] = data[(data_new.keys())[j]]
                    test_data[(data_new.keys())[j+r-1]] = data[(data_new.keys())[j+r-1]]
                    if test == "mcnemar":
                        paired_two_sample_test_of_nominal_scale = PairedTwoSampleTestOfNominalScale()
                        print "comparison of " + str((data_new.keys())[j]) + " and " + str((data_new.keys())[j+r-1])
                        paired_two_sample_test_of_nominal_scale.test(test_data)
                        #print data[(data_new.keys())[j]]
                        #print data[(data_new.keys())[j+r-1]]
                    else:
                        print "Please input test name"
                print "threshold is: " + str(2.0 * alpha / (m * ( r - 1 ))) # alpha_dash
                print "\n"

if __name__ == '__main__':
    multiple_comparison = MultipleComparison()
    #data = {"A": [12, 10, 8], "B": [5, 7, 20], "C": [7, 6, 7], "D": [1,3,4]}
    #data = {"A": [12, 10, 8], "B": [5, 7, 20], "C": [7, 6, 7]}
    #data = {"A": [12, 10, 8], "B": [5, 7, 20], "C": [7, 6, 7], "D": [1,3,4], "E":[1,1,1]}
    data = OrderedDict()
    data["CandidateA"] = [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    data["CandidateB"] = [1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
    data["CandidateC"] = [1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0]
    multiple_comparison.test(data, test="mcnemar")
