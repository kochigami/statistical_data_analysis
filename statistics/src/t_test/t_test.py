#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import numpy as np

class TTEST:
    def paired_ttest(self, data):
        """
        data = {'Japanese':  [68, 75, 80, 71, 73, 79, 69, 65],
                'English': [80, 76, 84, 93, 76, 80, 79, 84]}
        """

        """
        If samples are paired,
        we use paired t-test
        """
        # calculate t & p value
        t, p = stats.ttest_rel(data[(data.keys())[0]], data[(data.keys())[1]])
        print( "p value = %(p)s" %locals() )
        return p

    def unpaired_ttest(self, data):
        """
        data = {'Japanese':  [68, 75, 80, 71, 73, 79, 69, 65],
                'English': [80, 76, 84, 93, 76, 80, 79, 84]}
        label: ["Japanese", "English"] 
        """
        """
        If samples are not paired,
        we use unpaired t-test.
        We have to investigate whether the distribution is equall (tou bunsan) 
        by calculating f.
        We have to choose larger one as numerator (bunshi)
        """
        if np.var(data[(data.keys())[0]]) > np.var(data[(data.keys())[1]]):
            f = np.var(data[(data.keys())[0]]) / np.var(data[(data.keys())[1]])
        else:
            f = np.var(data[(data.keys())[1]]) / np.var(data[(data.keys())[0]])
        dfx = len(data[(data.keys())[0]]) - 1
        dfy = len(data[(data.keys())[1]]) - 1
        p_value = stats.f.cdf(f, dfx, dfy)

        """
        After obtaining p value, 
        we can check whether the distribution of samples is equal or not.
        If p < 0.05, we use t-test with not equal variance
        otherwise, we use t-test with equal variance
        """
        # calculate t & p value
        if p_value < 0.05:
            t, p = stats.ttest_ind(data[(data.keys())[0]], data[(data.keys())[1]], equal_var = False)
            ### heteroscedasticity: hi tou bunsan
            print ("t-test with heteroscedasticity")
        else:
            t, p = stats.ttest_ind(data[(data.keys())[0]], data[(data.keys())[1]], equal_var = True)
            ### homoscedasticity: tou bunsan
            print ("t-test with homoscedasticity")

        print( "p value = %(p)s" %locals() )
        return p
