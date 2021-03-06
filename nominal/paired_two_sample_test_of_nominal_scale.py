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
        data = {"Before": [1,1,1,1,1,...,0], "After": [1,1,1,1,1,...,0]}
        
                       Yes   No   Total
        -------------------------------
        Yes            a     b    a+b
        No             c     d    c+d
        -------------------------------
        Total         a+c   b+d   n (= a+b+c+d)

        focus on Yes -> No & No -> Yes
        In this example,
        number of Yes => No: b
        number of No => Yes: c
        """
        # check data length is 2
        if len(data.keys()) != 2 and len(data[data.keys()[0]]) != len(data[data.keys()[1]]):
            print "Please check the components of your data."
            print "length of data should be four"
            sys.exit()
        else:
            b = 0
            c = 0
            for i in range(len(data[(data.keys())[0]])):
                if data[(data.keys())[0]][i] == 1 and data[(data.keys())[1]][i] == 0:
                    b += 1
                elif data[(data.keys())[0]][i] == 0 and data[(data.keys())[1]][i] == 1:
                    c += 1
            # z = abs(b-c)-1 / root(b+c)
            # z^2 = chi2
            chi2 = pow(abs(b-c) - 1.0, 2.0) / (b+c)
            p = stats.chi2.pdf(chi2, df=1)
            # pdf: probability density function
            # cdf: Cumulative distribution function
            # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2.html
            print "chi2 value: {}".format(chi2)
            print "p value: {}".format(p)
            return p
