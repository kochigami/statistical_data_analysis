#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import numpy as np
import sys

"""
Followed this link: http://hs-www.hyogo-dai.ac.jp/~kawano/HStat/?2009%2F13th%2FMcNemar_Test
"""

class McNemarTest:
    def test(self, data):
        """
        focus on YES => NO & NO => YES
        data[0]: number of YES => NO
        data[1]: number of NO => YES
        """
        # check data length is 2
        if len(data) == 2 and isinstance(data[0], list) == False and isinstance(data[1], list) == False: 
            if (data[0] + data[1]) * 0.5 > 5:
                chi2 = pow(data[0]-data[1], 2.0) / (data[0] + data[1])
            else:
                chi2 = pow(abs(data[0]-data[1]) - 1.0, 2.0) / (data[0] + data[1])
            p = stats.chi2.cdf(chi2, df=1)
            p = 1.0 - p
            return p
        else:
            print "Please check the components of your data."
            print "data[0]: number of YES => NO"
            print "data[1]: number of NO => YES"
            sys.exit()
