#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from draw.draw_graph import DrawGraph
from draw.chi_squared_test_draw_table import ChiSquaredTestDrawTable
from nominal.paired_two_sample_test_of_nominal_scale import PairedTwoSampleTestOfNominalScale
from nominal.unpaired_two_sample_test_of_nominal_scale import UnpairedTwoSampleTestOfNominalScale
from nominal.one_condition_nominal_scale import TestOfOneConditionWithNominalScale
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
        print "4: one condition test + two factors (binominal test)"
        print "5: one condition test + more than two factors (chi-square test)"
    else:
        draw_graph = DrawGraph()
        draw_table = ChiSquaredTestDrawTable()
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
            p = paired_two_sample_test_of_nominal_scale.test(data)
            draw_graph.draw_graph(data, "test", "x", "y", p, tight_layout=True, sample_type="paired", is_scale_nominal=True)

        elif args[1] == "2":
            '''
            病気の患者，健常者のうち，喫煙者と非喫煙者の分布を調べる．
                           Smoker Non-Smoker Total
             -------------------------------------
             Illness         52       8       60
             Healty          48      42       90
             ------------------------------------
             Total          100      50      150

             OrderedDict([('Illness', [52, 8]), ('Healty', [48, 42])])
            '''
            data = OrderedDict()
            data["Illness"] = [52, 8]
            data["Healty"] = [48, 42]
            unpaired_two_sample_test_of_nominal_scale = UnpairedTwoSampleTestOfNominalScale()    
            p = unpaired_two_sample_test_of_nominal_scale.test(data)
            print "カイ二乗検定を喫煙率に実施した．その結果，病気の患者の喫煙率(87%)は，健常者の喫煙率(53%)より有意に高いことが明らかになった．(x_2 (1) = 16.531, p < 0.01)"
            draw_table.draw_table(p, data, ["Illness", "Healthy"], ["Smoker", "Non-Smoker"], "test")

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

             OrderedDict([('Teacher', [1, 12]), ('Counselor', [4, 6])])
            '''
            data = OrderedDict()
            data["Teacher"] = [1, 12]
            data["Counselor"] = [4, 6]
            unpaired_two_sample_test_of_nominal_scale = UnpairedTwoSampleTestOfNominalScale()
            p = unpaired_two_sample_test_of_nominal_scale.test(data)
            draw_table.draw_table(p, data, ["Teacher", "Counselor"], ["Non-social", "Antisocial"], "test")

        elif args[1] == "4":
            data = OrderedDict()
            data["O"] = 34
            data["Others"] = 86
            test_of_one_condition_with_nominal_scale = TestOfOneConditionWithNominalScale()
            p = test_of_one_condition_with_nominal_scale.test(data,p_threshold=0.45)

        elif args[1] == "5":
            data = OrderedDict()
            data["Kakansho"] = 72
            data["Honin"] = 23
            data["Kyohi"] = 16
            data["Dekiai"] = 49
            test_of_one_condition_with_nominal_scale = TestOfOneConditionWithNominalScale()
            p = test_of_one_condition_with_nominal_scale.test(data)
            
        else:
            print "python sample_two_sample_test_of_nominal_scale.py <sample_type>"
            print "please choose sample type: "
            print "1: paired test"
            print "2: unpaired test + big data"
            print "3: unpaired test + small data"
            print "4: one condition test: binominal test"
            print "5: one condition test: chi-square test"
