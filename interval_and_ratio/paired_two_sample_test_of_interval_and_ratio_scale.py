#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import numpy as np
import math
from scipy.stats import t as calc_p
# referenced as calc_p because of the error below:
# File "/home/kochigami/my_tutorial/statistics/src/t_test/t_test.py", line 80, in unpaired_ttest
# p = t.sf(t_value, dof)
# UnboundLocalError: local variable 't' referenced before assignment
# t test

class PairedTwoSampleTestOfIntervalAndRatioScale:
    def test(self, data):
        """
        data = {'Japanese':  [68, 75, 80, 71, 73, 79, 69, 65],
                'English': [80, 76, 84, 93, 76, 80, 79, 84]}
        """

        """
        If samples are paired,
        we use paired t-test
        I followed this website for calculation: 
        student's test: http://kogolab.chillout.jp/elearn/hamburger/chap5/sec3.html
        """
        # calculate t & p value
        x = data[(data.keys())[0]]
        y = data[(data.keys())[1]]
        if len(x) == len(y):
            t, p = stats.ttest_rel(x, y)
            print ("p value = %(p)s" %locals() )
            return p
        else:
            print "Please make sure the sample num is same in two conditions."
            return False
