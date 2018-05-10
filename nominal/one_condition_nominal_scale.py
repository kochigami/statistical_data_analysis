#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math
from scipy import stats

class TestOfOneConditionWithNominalScale ():
    def test(self, data, p_threshold=None):
        if len(data.keys()) == 2:
            # binominal test
            if p_threshold == None:
                print "Please set p value."
                sys.exit()
            else:
                z = (abs(data[data.keys()[0]] - sum(data.values()) * p_threshold) - 0.5) / math.sqrt(sum(data.values()) * p_threshold * (1.0 - p_threshold))
                p = stats.norm.pdf(z)
        elif len(data.keys()) > 2:
            # chi-square test
            average = sum(data.values()) / float(len(data.keys()))
            if average > 5.0:
                chi2 = 0.0
                for i in range(len(data.keys())):
                    chi2 += (abs(data[data.keys()[i]] - average) -0.5) ** 2 / average
                df = len(data.keys()) - 1.0
                print "dof: {}".format(df)
                p = stats.chi2.pdf(chi2, df)
            else:
                print "Please calculate the possibility directly."
                sys.exit()

        else:
            print "Please check the number of conditions (should be >= 2)."
            sys.exit()

        print "p: {}".format(p)
        return p
