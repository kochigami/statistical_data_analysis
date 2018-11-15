#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy.stats import wilcoxon
from scipy.stats import ranksums
import sys
import numpy

'''
signed rank sum test
signed test
'''

class PairedTwoSampleTestOfOrdinalScale:
    def test(self, data, mode="signed_rank_sum_test"):
        '''
        signed rank sum test
        '''
        """
        data = {'Product_A': [25, 62, 58, 26, 42, 18, 11, 33, 50, 34]
                'Product_B': [26, 31, 35, 24, 47, 13, 11, 21, 42, 18]}
        """
        # check data length
        if len(data.keys()) != 2:
            print "The number of your data type should be two"
            sys.exit()

        else:
            label_x = data.keys()[0]
            label_y = data.keys()[1]
            data_x = data[label_x]
            data_y = data[label_y]

            if len(data_x) != len(data_y):
                print "The number of data length should be same."
                sys.exit()

            else:
                if mode == "signed_rank_sum_test":
                    statistic, p = ranksums(data_x, data_y)
                elif mode == "signed_test":
                    # https://kusuri-jouhou.com/statistics/fugou.html
                    statistic, p = wilcoxon(data_x, data_y)
                else:
                    print "Please choose mode: 'signed_test' or 'signed_rank_test'"
                    sys.exit()
                print "median ({}) = {}".format((label_x, numpy.median(data_x))
                print "median ({}) = {}".format((label_y, numpy.median(data_y))
                print "p value: {}".format(p)
                return p
