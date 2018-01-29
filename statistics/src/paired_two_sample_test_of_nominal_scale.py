#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import numpy as np
import sys

"""
McNemar Test:
reference: http://hs-www.hyogo-dai.ac.jp/~kawano/HStat/?2009%2F13th%2FMcNemar_Test
"""

class PairedTwoSampleTestOfNominalScale:
    def test(self, data):
        """
        data = [[a, b], [c, d]]

        focus on YES => NO & NO => YES
        number of YES => NO: data[0][1]: b 
        number of NO => YES: data[1][0]: c 
        
                       Yes   No   Total
        -------------------------------
        Yes            a     b    a+b
        No             c     d    c+d
        -------------------------------
        Total         a+c   b+d   n (= a+b+c+d)
        """
        a = data[0][0]
        b = data[0][1]
        c = data[1][0]
        d = data[1][1]
        # check data length is 2
        if len(data) != 2 and len(data[0]) != 2 and len(data[1]) != 2:
            print "Please check the components of your data."
            print "length of data should be four"
            sys.exit()
        else:
            chi2 = pow(abs(b-c) - 1.0, 2.0) / (b+c)
            p = stats.chi2.cdf(chi2, df=1)
            p = 1.0 - p
            print "p value: "+ str(p)
            return p
