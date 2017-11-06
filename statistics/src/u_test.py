#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import sys

class UTEST:
    def mann_whitney_utest(self, data):
        """
        data = {'Children':  [20, 18, 15, 13, 10, 6],
                'Adults': [17, 16, 12, 9, 8, 6, 4, 2]}
        # use mannwhitneyu() from scipy
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html
        # however, alternative keyword cannnot be used
        # TypeError: mannwhitneyu() got an unexpected keyword argument 'alternative'
        """
        if len(data.keys()) != 2:
            print "Please check the contents of your data."
            print "The number of data type should be two."
            sys.exit()
        result = stats.mannwhitneyu(data[(data.keys())[0]], data[(data.keys())[1]], use_continuity=True)
        # return pvalue
        return result[1]
