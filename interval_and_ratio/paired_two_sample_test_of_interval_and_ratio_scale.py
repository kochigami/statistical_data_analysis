#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import sys

class PairedTwoSampleTestOfIntervalAndRatioScale:
    def test(self, data):
        '''
        data = {'Japanese':  [68, 75, 80, 71, 73, 79, 69, 65],
                'English':   [80, 76, 84, 93, 76, 80, 79, 84]}
        '''

        '''
        If samples are paired,
        we use paired t-test
        reference: 
        student's test: http://kogolab.chillout.jp/elearn/hamburger/chap5/sec3.html
        scipy documentation: https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.ttest_rel.html
        '''
        # calculate t & p value
        x = data[(data.keys())[0]]
        y = data[(data.keys())[1]]
        if len(x) == len(y):
            t, p = stats.ttest_rel(x, y)
            print ("dof = {}".format(len(x) - 1))
            print ("t value = {}".format(t))
            print ("p value = {}".format(p))
            return p
        else:
            print "Please make sure the sample num is same in two conditions."
            sys.exit()
