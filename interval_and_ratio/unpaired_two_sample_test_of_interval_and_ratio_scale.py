#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import numpy as np
import math

class UnpairedTwoSampleTestOfIntervalAndRatioScale:
    def test(self, data):
        '''
        data = {'Japanese':  [68, 75, 80, 71, 73, 79, 69, 65],
                'English': [80, 76, 84, 93, 76, 80, 79, 84]}
        If samples are not paired, we use unpaired t-test.
        Currently, we don't care whether two samples are considered to have equal population variance.
        reference: https://bellcurve.jp/statistics/course/9446.html
        '''

        x = data[(data.keys())[0]]
        y = data[(data.keys())[1]]
        nx = len(data[(data.keys())[0]])
        ny = len(data[(data.keys())[1]])
        dof = nx + ny - 2.0

        # welch's test
        t, p = stats.ttest_ind(x, y, equal_var=False)
        print("dof = {}".format(dof))
        print("t value = {}".format(t))
        print("p value = {}".format(p))
        return t, dof, p
