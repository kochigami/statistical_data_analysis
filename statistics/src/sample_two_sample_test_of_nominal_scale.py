#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
from paired_two_sample_test_of_nominal_scale import PairedTwoSampleTestOfNominalScale
from unpaired_two_sample_test_of_nominal_scale import UnpairedTwoSampleTestOfNominalScale
from collections import OrderedDict

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
        print "1: paired test (McNemar test)"
        print "2: unpaired test + big data (chi-square test)"
        print "3: unpaired test + small data (Fisher's exact test)"
    else:
        if args[1] == "1":
            '''
            講演会の前後で，ある質問に対して賛成か・反対かを尋ねる．
            賛成率に変化があったか調べる．
                          Subject  Before Lecture  After Lecture
             ---------------------------------------------------
              a group  |     1            1              1     
                       |     ...         ...            ...
                       |     18           1              1
             ---------------------------------------------------
              b group  |     19           1              0     
                       |     ...         ...            ...
                       |     54           1              0
             ---------------------------------------------------
              c group  |     55           0              1     
                       |     ...         ...            ...
                       |     61           0              1
             ---------------------------------------------------
              d group  |     62           0              0     
                       |     ...         ...            ...
                       |     90           0              0
             ---------------------------------------------------
            1: agree 0: disagree

            data = {"Before": [1,1,1,1,1,...,0], "After": [1,1,1,1,1,...,0]}

            focus on Yes -> No & No -> Yes
            number of Yes -> No : b 
            number of No -> Yes:  c 
        
                            Yes   No   Total
             -------------------------------
              Yes            a     b    a+b
              No             c     d    c+d
             -------------------------------
              Total         a+c   b+d   n (= a+b+c+d)

            '''

            data = OrderedDict()
            data["Before"] = [1,1,1,1,1,1, 1,1,1,1,1,1, 1,1,1,1,1,1, 
                              1,1,1,1,1,1, 1,1,1,1,1,1, 1,1,1,1,1,1, 1,1,1,1,1,1, 1,1,1,1,1,1, 1,1,1,1,1,1, 
                              0,0,0,0,0,0,0, 
                              0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0]
            data["After"] =  [1,1,1,1,1,1, 1,1,1,1,1,1, 1,1,1,1,1,1,
                              0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0,
                              1,1,1,1,1,1,1,
                              0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0]

            paired_two_sample_test_of_nominal_scale = PairedTwoSampleTestOfNominalScale()
            paired_two_sample_test_of_nominal_scale.test(data)

        elif args[1] == "2":
            '''
            病気の患者，健常者のうち，喫煙者と非喫煙者の分布を調べる．
                           Smoker Non-Smoker Total
             -------------------------------------
             Illness         52       8       60
             Healty          48      42       90
             ------------------------------------
             Total          100      50      150

             data: [[52, 8], [48, 42]]            
            '''
            data = OrderedDict()
            data["Smoker"] = [52, 48]
            data["Non-Smoker"] = [8, 42]
            unpaired_two_sample_test_of_nominal_scale = UnpairedTwoSampleTestOfNominalScale()    
            unpaired_two_sample_test_of_nominal_scale.test(data)

        elif args[1] == "3":
            '''
            児童の問題行動に対し，先生・カウンセラーのそれぞれで，
            非社会的行動・反社会的行動のどちらを重要視しているか分布を調べる．
                           Non-social Antisocial  Total
             ------------------------------------------
             Teacher         1          12         13
             Counselor       4           6         10
             -----------------------------------------
             Total           5          18         23

             data: [[1, 12], [4, 6]]            
            '''
            data = OrderedDict()
            data["Non-social"] = [1, 4]
            data["Antisocial"] = [12, 6]
            unpaired_two_sample_test_of_nominal_scale = UnpairedTwoSampleTestOfNominalScale()
            unpaired_two_sample_test_of_nominal_scale.test(data)

        else:
            print "python sample_two_sample_test_of_nominal_scale.py <sample_type>"
            print "please choose sample type: "
            print "1: paired test"
            print "2: unpaired test + big data"
            print "3: unpaired test + small data"
