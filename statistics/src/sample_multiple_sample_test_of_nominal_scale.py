#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from unpaired_multiple_sample_test_of_nominal_scale import UnpairedMultipleSampleTestOfNominalScale
from paired_multiple_sample_test_of_nominal_scale import PairedMultipleSampleTestOfNominalScale

if __name__ == '__main__':
    args = sys.argv
    if len(args) is not 2:
        print "python sample_multiple_sample_test_of_nominal_scale.py <sample_type>"
        print "please choose sample type: "
        print "1: unpaired test"
        print "2: paired test"
    else:
        if args[1] == "1":
            '''
                   CandidateA  CandidateB  CandidateC  Total
            ---------------------------------------------------
            Audition    12          10          8        30
            Vision      5           5           20       30     
            Audition
               +        7           6           7        20   
             Vision
            --------------------------------------------------
                        24          21          35       80
            data = [[12, 10, 8],[5, 5, 20], [7, 6, 7]]
            '''

            data = [[12, 10, 8],[5, 5, 20], [7, 6, 7]]
            unpaired_multiple_sample_test_of_nominal_scale = UnpairedMultipleSampleTestOfNominalScale()
            unpaired_multiple_sample_test_of_nominal_scale.test(data)
            
        elif args[1] == "2":
            '''
                   CandidateA  CandidateB  CandidateC  Total (sum_row)
            ---------------------------------------------------
            Subject1      1           1           1        3
            Subject2      1           1           1        3     
            Subject3      1           1           1        3     
            Subject4      1           1           1        3
            Subject5      1           0           1        2
            Subject6      1           0           1        2
            Subject7      0           1           1        2
            Subject8      0           1           1        2
            Subject9      0           1           1        2
            Subject10     0           1           1        2
            Subject11     0           1           0        1
            Subject12     0           1           0        1     
            Subject13     0           0           1        1     
            Subject14     0           0           1        1
            Subject15     0           0           1        1
            Subject16     0           0           1        1
            Subject17     0           0           0        0
            Subject18     0           0           0        0
            Subject19     0           0           0        0
            Subject20     0           0           0        0
            --------------------------------------------------
            Total         6          10           14       30
            (sum_column)
            '''
            data = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1], [0, 1, 1], [0, 1, 1], [0, 1, 1], [0, 1, 1], [0, 1, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
            paired_multiple_sample_test_of_nominal_scale = PairedMultipleSampleTestOfNominalScale()
            paired_multiple_sample_test_of_nominal_scale.test(data)
