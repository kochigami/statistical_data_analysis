#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import numpy as np
import sys

"""
McNemar Test:
Followed this link: http://hs-www.hyogo-dai.ac.jp/~kawano/HStat/?2009%2F13th%2FMcNemar_Test
"""

class PairedTwoSampleTestOfNominalScale:
    def test(self, data):
        """
        focus on YES => NO & NO => YES
        data[0]: number of YES => NO
        data[1]: number of NO => YES
        """
        """
                       Yes   No   Total
        -------------------------------
        Condition1     a     b    a+b
        Condition2     c     d    c+d
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
            if (b + c) * 0.5 > 5:
                chi2 = pow(b-c, 2.0) / (b+c)
            else:
                chi2 = pow(abs(b-c) - 1.0, 2.0) / (b+c)
            p = stats.chi2.cdf(chi2, df=1)
            p = 1.0 - p
            print p
            return p
