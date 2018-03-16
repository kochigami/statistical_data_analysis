#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from draw.draw_graph import DrawGraph
from interval_and_ratio.paired_two_sample_test_of_interval_and_ratio_scale import PairedTwoSampleTestOfIntervalAndRatioScale
from interval_and_ratio.unpaired_two_sample_test_of_interval_and_ratio_scale import UnpairedTwoSampleTestOfIntervalAndRatioScale
from collections import OrderedDict

if __name__ == '__main__':
    args = sys.argv
    if len(args) is not 2:
        print "python sample_t_test.py <sample_type>"
        print "please choose sample type: "
        print "1: welch's test and unpaired-ttest"
        print "2: student's test and unpaired-ttest"
        print "3: student's test and paired-ttest"
    else:
        d = DrawGraph()
        # if we use normal dict, the order of contents sometimes is decided randomly.
        # ex: should be [A, B, C], but output is [A, C, B]
        data = OrderedDict()
        paired_two_sample_test_of_interval_and_ratio_scale = PairedTwoSampleTestOfIntervalAndRatioScale()
        unpaired_two_sample_test_of_interval_and_ratio_scale = UnpairedTwoSampleTestOfIntervalAndRatioScale()
        if args[1] == "1":
            # for welch's test
            # followed this website for sample: http://www.geisya.or.jp/~mwm48961/statistics/ttest_question2.htm
            data['HamburgerA'] = [15.3, 14.9, 14.5, 14.4, 14.0, 13.9, 14.1, 14.7, 15.3, 14.6]
            data['HamburgerB'] = [13.9, 14.2, 14.1, 14.3, 14.1, 13.7, 14.7, 13.9, 14.1, 13.8, 14.3]
            p = unpaired_two_sample_test_of_interval_and_ratio_scale.test(data)
            d.draw_graph(data, "test", "x", "y", p, tight_layout=True, sample_type="unpaired")
        elif args[1] == "2":
            # for student's test
            # followed this website for sample: http://kogolab.chillout.jp/elearn/hamburger/chap4/sec1.html
            data['HamburgerA'] = [70, 75, 70, 85, 90, 70, 80, 75]
            data['HamburgerB'] = [85, 80, 95, 70, 80, 75, 80, 90]
            p = unpaired_two_sample_test_of_interval_and_ratio_scale.test(data)
            d.draw_graph(data, "test", "x", "y", p, tight_layout=True, sample_type="unpaired")
        elif args[1] == "3":
            # followed this website for sample: http://kogolab.chillout.jp/elearn/hamburger/chap5/sec1.html
            data['HamburgerA'] = [90, 75, 75, 75, 80, 65, 75, 80]
            data['HamburgerB'] = [95, 80, 80, 80, 75, 75, 80, 85]
            p = paired_two_sample_test_of_interval_and_ratio_scale.test(data)
            d.draw_graph(data, "test", "x", "y", p, tight_layout=True, sample_type="paired")

        # if we use OrderedDict, but if we use the initialization below, 
        # the order of contents sometimes is still decided randomly.
        # data = {'HamburgerA':  [15.3, 14.9, 14.5, 14.4, 14.0, 13.9, 14.1, 14.7, 15.3, 14.6],
        #         'HamburgerB' : [13.9, 14.2, 14.1, 14.3, 14.1, 13.7, 14.7, 13.9, 14.1, 13.8, 14.3]}
        
        else:
            print "Please select 1-3."
            print "1: welch's test and unpaired-ttest"
            print "2: student's test and unpaired-ttest"
            print "3: student's test and paired-ttest"
