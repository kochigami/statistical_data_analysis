#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy.stats import mannwhitneyu
import sys
import numpy

'''
Mann-Whitney test
'''

class UnpairedTwoSampleTestOfOrdinalScale:
    def test(self, data):
        """
        data = {'Children':  [20, 18, 15, 13, 10, 6],
                'Adults': [17, 16, 12, 9, 8, 6, 4, 2]}
        # https://kusuri-jouhou.com/statistics/mann.html
        => comparison of two median
        """
        if len(data.keys()) != 2:
            print "Please check the contents of your data."
            print "The number of data type should be two."
            sys.exit()
        x_label = (data.keys())[0]
        y_label = (data.keys())[1]
        x_data = data[x_label]
        y_data = data[y_label]
        statistic, p = mannwhitneyu(x_data, y_data, use_continuity=True)
        print "median ({}): {}".format(x_label, numpy.median(x_data))
        print "median ({}): {}".format(y_label, numpy.median(y_data))
        print "U value: {}".format(statistic)
        print "p value: {}".format(p)
        return p
