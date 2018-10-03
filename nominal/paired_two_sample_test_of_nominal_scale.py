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
        There is a question which we can answer yes (1) or no (0).
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
        # check if the number of samples are appropriate 
        if len(data.keys()) != 2 or len(data[data.keys()[0]]) != len(data[data.keys()[1]]):
            print ("Please check the components of your data.")
            print ("the number of each data should be equal")
            sys.exit()
        else:
            b = 0
            c = 0
            for i in range(len(data[(data.keys())[0]])):
                if data[(data.keys())[0]][i] == 1 and data[(data.keys())[1]][i] == 0:
                    b += 1
                elif data[(data.keys())[0]][i] == 0 and data[(data.keys())[1]][i] == 1:
                    c += 1
            # calculating chi-square value with Yate's continuity correction (イェーツの連続修正) 
            chi2 = pow((abs(b-c)-1), 2.0) / (b+c)
            
            '''
            If there is no consideration on Yate's continuity correction:
            chi2 = pow(abs(b-c) - 1.0, 2.0) / (b+c)
            '''
            p = stats.chi2.pdf(chi2, df=1)
            print "chi2 value: {}".format(chi2)
            print "p value: {}".format(p)
            return p

if __name__ == '__main__':
    pass
