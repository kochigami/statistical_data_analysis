#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import itertools
import operator
from collections import OrderedDict
from nominal.paired_two_sample_test_of_nominal_scale import PairedTwoSampleTestOfNominalScale
from nominal.unpaired_two_sample_test_of_nominal_scale import UnpairedTwoSampleTestOfNominalScale
from ordinal.paired_two_sample_test_of_ordinal_scale import PairedTwoSampleTestOfOrdinalScale
from ordinal.unpaired_two_sample_test_of_ordinal_scale import UnpairedTwoSampleTestOfOrdinalScale

class MultipleComparison:
    def test(self, data, test="none", alpha=0.05, mode="ryan"):
        if mode == "ryan":
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
                    
                        test: executed test name (with multiple conditions (> 2 conditions))
                        '''

                        if test == "chi-square":
                            # using fisher's exact test and chi-squared test
                            unpaired_two_sample_test_of_nominal_scale = UnpairedTwoSampleTestOfNominalScale()
                            unpaired_two_sample_test_of_nominal_scale.test(test_data)
                        elif test == "cochran":
                            # using mcnemar test
                            paired_two_sample_test_of_nominal_scale = PairedTwoSampleTestOfNominalScale()
                            paired_two_sample_test_of_nominal_scale.test(test_data)
                        elif test == "kruskal-wallis":
                            # using mann-whitney test
                            unpaired_two_sample_test_of_ordinal_scale = UnpairedTwoSampleTestOfOrdinalScale()
                            unpaired_two_sample_test_of_ordinal_scale.test(test_data)
                        elif test == "friedman":
                            # using signed-test
                            paired_two_sample_test_of_ordinal_scale = PairedTwoSampleTestOfOrdinalScale()
                            paired_two_sample_test_of_ordinal_scale.test(test_data, mode="signed_test")
                        else:
                            print "Please input test name"

        elif mode == "holm":
            p_list = OrderedDict()
            sorted_p_list = OrderedDict()
            combinations = list(itertools.combinations(data.keys(), 2))
            '''
            create data of a chosen pair
            '''
            for i in range(len(combinations)):
                test_data = OrderedDict()
                test_data[combinations[i][0]] = data[combinations[i][0]]
                test_data[combinations[i][1]] = data[combinations[i][1]]
                '''
                print paired sample
                '''
                print "\ncomparison of {} and {}".format(combinations[i][0], combinations[i][1])
            
                if test == "chi-square":
                    # using fisher's exact test and chi-squared test
                    unpaired_two_sample_test_of_nominal_scale = UnpairedTwoSampleTestOfNominalScale()
                    p_list[str(combinations[i][0]) + "+" + str(combinations[i][1])] = unpaired_two_sample_test_of_nominal_scale.test(test_data)
                elif test == "cochran":
                    # using mcnemar test
                    paired_two_sample_test_of_nominal_scale = PairedTwoSampleTestOfNominalScale()
                    p_list[str(combinations[i][0]) + "+" + str(combinations[i][1])] = paired_two_sample_test_of_nominal_scale.test(test_data)
                elif test == "kruskal-wallis":
                    # using mann-whitney test
                    unpaired_two_sample_test_of_ordinal_scale = UnpairedTwoSampleTestOfOrdinalScale()
                    p_list[str(combinations[i][0]) + "+" + str(combinations[i][1])] = unpaired_two_sample_test_of_ordinal_scale.test(test_data)
                elif test == "friedman":
                    # using signed-test
                    paired_two_sample_test_of_ordinal_scale = PairedTwoSampleTestOfOrdinalScale()
                    p_list[str(combinations[i][0]) + "+" + str(combinations[i][1])] = paired_two_sample_test_of_ordinal_scale.test(test_data, mode="signed_test")
                else:
                    print "Please input test name"

            # decending sort
            for k, v in sorted(p_list.items(), key=lambda x: -x[1]):
                sorted_p_list[str(k)] = v
            # sorted_p_list: OrderedDict([('A+C', 0.8193893539627245), ('B+D', 0.6461080882133514), ('C+D', 0.498681672594716), ('A+D', 0.18558104194277167), ('B+C', 0.10205296671359539), ('A+B', 0.014271727596197067)])

            # adjust a possibility
            for i in range(1, len(p_list.keys())+1):
                tmp = sorted_p_list[sorted_p_list.keys()[i-1]]
                tmp *= i
                p_list[sorted_p_list.keys()[i-1]] = tmp

            print "\nFinal Results as Follows: (threshold is 0.05)"
            for i in range(len(p_list.keys())):
                print "\ncomparison of {}. modified p value is {}".format(p_list.keys()[i], p_list[p_list.keys()[i]])
