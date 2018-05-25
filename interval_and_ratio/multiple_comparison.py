#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
import operator
from collections import OrderedDict
from nominal.paired_two_sample_test_of_nominal_scale import PairedTwoSampleTestOfNominalScale
from nominal.unpaired_two_sample_test_of_nominal_scale import UnpairedTwoSampleTestOfNominalScale
from ordinal.paired_two_sample_test_of_ordinal_scale import PairedTwoSampleTestOfOrdinalScale
from ordinal.unpaired_two_sample_test_of_ordinal_scale import UnpairedTwoSampleTestOfOrdinalScale

class MultipleComparison:
    def test(self, data, test="none", alpha=0.05):
        '''
        ryan method

        data: {A: [1,2,3], B: [2,4,6], ...}

        alpha_dash = 2 * alpha / (m * ( r - 1 ))
        m: the number of step 
        r: the number of step - the total number of step
        '''
        m = len(data.keys())
        '''
        calculate
        data_average: {A: 2, B: 4, ...}
        '''
        data_average = {}
        for r in range(m):
            data_average[(data.keys())[r]] = np.average(data[(data.keys())[r]])
        '''
        sort data_average
        set a result as data_tmp
        '''
        data_tmp = sorted(data_average.items(), key=operator.itemgetter(1))
        '''
        make OrderedDict "data_new" by copying data_tmp
        '''
        data_new = OrderedDict()
        for r in range(len(data_tmp)):
            data_new[(data_tmp[r])[0]] = (data_tmp[r])[1]
        
        '''
        r: the number of step - the total number of step
        '''
        for i in range(m):
            r = m - i
            if r > 1:
                print "\n[Step {}]".format(i+1)
                '''
                show alpha_dash as threshold of p
                '''
                print "threshold is: {}".format(2.0 * alpha / (m * ( r - 1 )))
                for j in range(0, i+1):
                    '''
                    create data of a chosen pair
                    '''
                    test_data = OrderedDict()
                    test_data[(data_new.keys())[j]] = data[(data_new.keys())[j]]
                    test_data[(data_new.keys())[j+r-1]] = data[(data_new.keys())[j+r-1]]
                    '''
                    print paired sample
                    '''
                    print "\ncomparison of {} and {}".format((data_new.keys())[j], (data_new.keys())[j+r-1])
                    '''
                    run test and get p value
                    '''
                    # FIXME: add explanation about what test variable means
                    if test == "chi-squared":
                        # fisher's exact test and chi-squared test
                        unpaired_two_sample_test_of_nominal_scale = UnpairedTwoSampleTestOfNominalScale()
                        unpaired_two_sample_test_of_nominal_scale.test(test_data)
                    elif test == "mcnemar":
                        # mcnemar
                        paired_two_sample_test_of_nominal_scale = PairedTwoSampleTestOfNominalScale()
                        paired_two_sample_test_of_nominal_scale.test(test_data)
                    elif test == "mann-whitney":
                        # Kruskal-Wallis
                        unpaired_two_sample_test_of_ordinal_scale = UnpairedTwoSampleTestOfOrdinalScale()
                        unpaired_two_sample_test_of_ordinal_scale.test(test_data)
                    elif test == "signed-test":
                        paired_two_sample_test_of_ordinal_scale = PairedTwoSampleTestOfOrdinalScale()
                        paired_two_sample_test_of_ordinal_scale.test(test_data, mode="signed_test")
                    else:
                        print "Please input test name"
