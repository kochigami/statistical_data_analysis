#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from draw.draw_graph import DrawGraph
from nominal.unpaired_multiple_sample_test_of_nominal_scale import UnpairedMultipleSampleTestOfNominalScale
from nominal.paired_multiple_sample_test_of_nominal_scale import PairedMultipleSampleTestOfNominalScale
from collections import OrderedDict

if __name__ == '__main__':
    args = sys.argv
    if len(args) is not 2:
        print "python sample_multiple_sample_test_of_nominal_scale.py <sample_type>"
        print "please choose sample type: "
        print "1: unpaired test (chi-square test)"
        print "2: paired test (Cochran's Q test)"
    else:
        draw_graph = DrawGraph()
        if args[1] == "1":
            '''
            刺激条件を変えて，複数の単語を記憶する．自由再生実験した時に，一番最初に再生された単語のリストでの位置を調べる．
                        First      Middle      End      Total
            ---------------------------------------------------
            Audition    12          10          8        30
            Vision      5           5           20       30     
            Audition
               +        7           6           7        20   
             Vision
            --------------------------------------------------
                        24          21          35       80
            data = {"First": [12,5,7], "Middle": [10,5,6], "End": [8,20,7]}
            '''

            data = OrderedDict()
            data["Audition"] = [12, 10, 8]
            data["Vision"] = [5, 5, 20]
            data["Audition+Vision"] = [7, 6, 7]
            unpaired_multiple_sample_test_of_nominal_scale = UnpairedMultipleSampleTestOfNominalScale()
            unpaired_multiple_sample_test_of_nominal_scale.test(data)
            draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, sample_type="unpaired", is_scale_nominal=True)

        elif args[1] == "2":
            '''
            20人の有権者に，A, B, C候補のそれぞれを支持するかどうかを尋ねる．
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
            data = OrderedDict()
            data["CandidateA"] = [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            data["CandidateB"] = [1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
            data["CandidateC"] = [1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0]
            paired_multiple_sample_test_of_nominal_scale = PairedMultipleSampleTestOfNominalScale()
            paired_multiple_sample_test_of_nominal_scale.test(data)
            draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, sample_type="paired", is_scale_nominal=True)

        else:
            print "please choose sample type: "
            print "1: unpaired test (chi-square test)"
            print "2: paired test (Cochran's Q test)"