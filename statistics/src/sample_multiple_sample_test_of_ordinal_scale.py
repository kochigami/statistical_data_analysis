#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 参照：心理学のためのデータ解析テクニカルブック　北大路書房
import sys
import numpy as np
from unpaired_multiple_sample_test_of_ordinal_scale import UnpairedMultipleSampleTestOfOrdinalScale
from paired_multiple_sample_test_of_ordinal_scale import PairedMultipleSampleTestOfOrdinalScale
from collections import OrderedDict

if __name__ == '__main__':
    args = sys.argv
    if len(args) is not 2:
        print "python sample_multiple_sample_test_of_ordinal_scale.py <sample_type>"
        print "please choose sample type: "
        print "1: unpaired test (Kruskal-Wallis test)"
        print "2: paired test (Friedman test)"
    else:
        if args[1] == "1":
            '''
            ABCの条件で ある刺激に対する幼児の反応時間を測定する．
            Condition    A     B     C
                        3.88  2.86  1.82
                        4.60  9.02  4.21
                        6.30  4.27  3.10
                        2.15  9.86  1.99
                        4.80  3.66  2.75
                        5.20  5.48  2.18
            '''
            data = OrderedDict()
            data["A"] = [3.88,4.60,6.30,2.15,4.80,5.20]
            data["B"] = [2.86,9.02,4.27,9.86,3.66,5.48] 
            data["C"] = [1.82,4.21,3.10,1.99,2.75,2.18]
            unpaired_multiple_sample_test_of_ordinal_scale = UnpairedMultipleSampleTestOfOrdinalScale()
            unpaired_multiple_sample_test_of_ordinal_scale.test(data)
            
        elif args[1] == "2":
            '''
            CM 5本を 7人の評定者に順位付けしてもらう．

            Subject  ConditionA  B  C  D  E 
            1            1       2  3  5  4
            2            5       1  3  2  4
            3            1       2  3  4  5
            4            5       1  4  2  3
            5            5       4  2  3  1
            6            4       2  1  3  5
            7            5       4  2  3  1
            -------------------------------
            Total       26      16 18 22 23
            '''
            data = OrderedDict()
            data["A"] = [1,5,1,5,5,4,5]
            data["B"] = [2,1,2,1,4,2,4]
            data["C"] = [3,3,3,4,2,1,2]
            data["D"] = [5,2,4,2,3,3,3]            
            data["E"] = [4,4,5,3,1,5,1]
            paired_multiple_sample_test_of_ordinal_scale = PairedMultipleSampleTestOfOrdinalScale()
            paired_multiple_sample_test_of_ordinal_scale.test(data)
