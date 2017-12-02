#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import numpy as np
import math
from scipy.stats import t as calc_p
# referenced as calc_p because of the error below:
# File "/home/kochigami/my_tutorial/statistics/src/t_test/t_test.py", line 80, in unpaired_ttest
# p = t.sf(t_value, dof)
# UnboundLocalError: local variable 't' referenced before assignment

class TTEST:
    def paired_ttest(self, data):
        """
        data = {'Japanese':  [68, 75, 80, 71, 73, 79, 69, 65],
                'English': [80, 76, 84, 93, 76, 80, 79, 84]}
        """

        """
        If samples are paired,
        we use paired t-test
        I followed this website for calculation: 
        student's test: http://kogolab.chillout.jp/elearn/hamburger/chap5/sec3.html
        """
        # calculate t & p value
        x = data[(data.keys())[0]]
        y = data[(data.keys())[1]]
        if len(x) == len(y):
            t, p = stats.ttest_rel(x, y)
            print ("p value = %(p)s" %locals() )
            return p
        else:
            print "Please make sure the sample num is same in two conditions."
            return False

    def unpaired_ttest(self, data):
        """
        data = {'Japanese':  [68, 75, 80, 71, 73, 79, 69, 65],
                'English': [80, 76, 84, 93, 76, 80, 79, 84]}
        """
        """
        If samples are not paired,
        we use unpaired t-test.
        We have to investigate whether the distribution is equall (tou bunsan) 
        by calculating f.
        We have to choose larger one as numerator (bunshi)
        I followed this website for calculation: 
        student's test: http://kogolab.chillout.jp/elearn/hamburger/chap4/sec3.html
        welch's test: http://hs-www.hyogo-dai.ac.jp/%7Ekawano/HStat/?2015%2F13th%2FWelch%27s_Test
        """
        x = data[(data.keys())[0]]
        y = data[(data.keys())[1]]
        nx = len(data[(data.keys())[0]])
        ny = len(data[(data.keys())[1]])
        dfx = nx - 1.0
        dfy = ny - 1.0
        # https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.var.html
        # var = mean(abs(x - x.mean())**2).
        s_x = (1.0 / dfx) * np.var(x)
        s_y = (1.0 / dfy) * np.var(y)
        if s_x > s_y:
            # Usually, f value should be greater than 1.0,
            # I reverse s_x and s_y upside down
            # in order to let stats.f.cdf return p value less than 0.05
            # % for example:
            # % If I use s_x / s_y instead of s_y / s_x, it returns 0.96 instead of 0.04
            # % but I need the value less than 0.05.
            f = s_y / s_x
            p_value = stats.f.cdf(f, dfx, dfy)
        else:
            f = s_x / s_y
            p_value = stats.f.cdf(f, dfy, dfx)
            
        """
        After obtaining p value, 
        we can check whether the distribution of samples is equal or not.
        If p < 0.05, we use t-test with not equal variance
        otherwise, we use t-test with equal variance
        """
        # calculate t & p value
        if p_value < 0.05:
            # welch's test
            diff_average = np.average(x) - np.average(y)
            sample_variance_1 = 0.0
            for i in range(nx):
                sample_variance_1 += pow((x[i] - np.average(x)), 2.0)
            sample_variance_1 = (1.0 / dfx) * sample_variance_1

            sample_variance_2 = 0.0
            for i in range(ny):
                sample_variance_2 += pow((y[i] - np.average(y)), 2.0)
            sample_variance_2 = (1.0 / dfy) * sample_variance_2

            t = abs(diff_average / math.sqrt((sample_variance_1 / nx) + (sample_variance_2 / ny)))
            dof = pow((sample_variance_1 / nx) + (sample_variance_2 / ny), 2.0) / ((pow(sample_variance_1 / nx, 2.0) / dfx) + ((pow(sample_variance_2 / ny, 2.0) / dfy)))
            dof = math.ceil(dof)
            p = calc_p.sf(t, dof)
            ### heteroscedasticity: hi tou bunsan
            print ("t-test with heteroscedasticity")
        else:
            # student's test
            diff_average = np.average(x) - np.average(y)
            diff_variance = (np.var(x) * nx + np.var(y) * ny) / (nx + ny -2)
            diff_error = math.sqrt (diff_variance * (1.0 / nx + 1.0 / ny))
            t = abs(diff_average / diff_error)
            dof = nx + ny - 2
            p = calc_p.sf(t, dof)
            ### homoscedasticity: tou bunsan
            print ("t-test with homoscedasticity")

        print( "p value = %(p)s" %locals() )
        return p
