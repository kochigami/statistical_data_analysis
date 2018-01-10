#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
from unpaired_multiple_sample_test_of_nominal_scale import UnpairedMultipleSampleTestOfNominalScale

if __name__ == '__main__':
    args = sys.argv
    if len(args) is not 2:
        print "python sample_multiple_sample_test_of_nominal_scale.py <sample_type>"
        print "please choose sample type: "
        print "1: unpaired test"
    else:
        if args[1] == "1":
            data = np.array([[12, 10, 8],[5, 5, 20], [7, 6, 7]])
            unpaired_multiple_sample_test_of_nominal_scale = UnpairedMultipleSampleTestOfNominalScale()
            unpaired_multiple_sample_test_of_nominal_scale.test(data)
