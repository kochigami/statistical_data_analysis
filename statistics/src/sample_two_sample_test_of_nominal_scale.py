#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
from paired_two_sample_test_of_nominal_scale import PairedTwoSampleTestOfNominalScale
from unpaired_two_sample_test_of_nominal_scale import UnpairedTwoSampleTestOfNominalScale

"""
              Yes   No   Total
-------------------------------
Condition1     a     b    a+b
Condition2     c     d    c+d
-------------------------------
Total         a+c   b+d   n (= a+b+c+d)

data: [[a, b], [c, d]]
"""

if __name__ == '__main__':
    args = sys.argv
    if len(args) is not 2:
        print "python sample_two_sample_test_of_nominal_scale.py <sample_type>"
        print "please choose sample type: "
        print "1: paired test + big data"
        print "2: paired test + small data"
        print "3: unpaired test + big data"
        print "4: unpaired test + small data"
    else:
        if args[1] == "1":
            data = np.array([[1625, 5],[1022, 11]])
            paired_two_sample_test_of_nominal_scale = PairedTwoSampleTestOfNominalScale()
            paired_two_sample_test_of_nominal_scale.test(data)

        elif args[1] == "2":
            data = np.array([[13, 4], [6, 14]])
            paired_two_sample_test_of_nominal_scale = PairedTwoSampleTestOfNominalScale()
            paired_two_sample_test_of_nominal_scale.test(data)

        elif args[1] == "3":
            data = np.array([[1625, 5],[1022, 11]])
            unpaired_two_sample_test_of_nominal_scale = UnpairedTwoSampleTestOfNominalScale()    
            unpaired_two_sample_test_of_nominal_scale.test(data)

        elif args[1] == "4":
            data = np.array([[13, 4], [6, 14]])
            unpaired_two_sample_test_of_nominal_scale = UnpairedTwoSampleTestOfNominalScale()
            unpaired_two_sample_test_of_nominal_scale.test(data)
