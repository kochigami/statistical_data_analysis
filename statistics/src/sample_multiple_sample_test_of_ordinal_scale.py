#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
from unpaired_multiple_sample_test_of_ordinal_scale import UnpairedMultipleSampleTestOfOrdinalScale
from paired_multiple_sample_test_of_ordinal_scale import PairedMultipleSampleTestOfOrdinalScale

if __name__ == '__main__':
    args = sys.argv
    if len(args) is not 2:
        print "python sample_multiple_sample_test_of_ordinal_scale.py <sample_type>"
        print "please choose sample type: "
        print "1: unpaired test"
        print "2: paired test"
    else:
        if args[1] == "1":
            data = [[3.88,4.60,6.30,2.15,4.80,5.20], [2.86,9.02,4.27,9.86,3.66,5.48], [1.82,4.21,3.10,1.99,2.75,2.18]]
            unpaired_multiple_sample_test_of_ordinal_scale = UnpairedMultipleSampleTestOfOrdinalScale()
            unpaired_multiple_sample_test_of_ordinal_scale.test(data)
            
        elif args[1] == "2":
            data = [[1,2,3,5,4], [5,1,3,2,4], [1,2,3,4,5], [5,1,4,2,3], [5,4,2,3,1], [4,2,1,3,5], [5,4,2,3,1]]
            paired_multiple_sample_test_of_ordinal_scale = PairedMultipleSampleTestOfOrdinalScale()
            paired_multiple_sample_test_of_ordinal_scale.test(data)
