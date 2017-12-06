#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import numpy as np
import sys

class ChiSquaredTest:
    def test(self, data):
        """
        """
        # check component type is 2
        if len(data) != 2 and len(data[0]) != 2 and len(data[1]) != 2: 
            print "Please check the component num of your data."
            print "The number of data type should be two."
            sys.exit()
        else:
            squared, p, dof, ef = stats.chi2_contingency(data)
            # squared: 検定統計量
            # p: p value
            # dof: 自由度
            # ef: 期待度数
            return p
