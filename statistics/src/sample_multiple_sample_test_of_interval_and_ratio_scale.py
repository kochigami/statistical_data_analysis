#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from two_way_anova import TwoWayAnova
from one_way_anova_draw_table import OneWayAnovaDrawTable
from two_way_anova_draw_table import TwoWayAnovaDrawTable
from draw_graph import DrawGraph
from collections import OrderedDict

if __name__ == '__main__':
    args = sys.argv
    if len(args) is not 2:
        print "python sample_multiple_sample_test_of_interval_and_ratio_scale.py <sample_type>"
        print "please choose sample type:"
        print "1: one-way anova CR(1)"
        print "2: one-way anova CR(2)"
        print "3: one-way anova CR(3)"
        print "4: one-way anova RB(1)"
        print "5: one-way anova RB(2)"
        print "6: two-way anova CRFpq(1)"
        print "7: two-way anova CRFpq(2)"
        print "8: two-way anova CRFpq(3)"
        print "9: two-way anova SPFpq(1)"
        print "10: two-way anova SPFpq(2)"
        sys.exit()

    one_way_anova_draw_table = OneWayAnovaDrawTable()
    two_way_anova_draw_table = TwoWayAnovaDrawTable()
    two_way_anova = TwoWayAnova()
    draw_graph = DrawGraph()
    # if we use normal dict, the order of contents sometimes is decided randomly.
    # ex: should be [A, B, C], but output is [A, C, B]
    data = OrderedDict()
    
    # if we use OrderedDict, but if we use the initialization below, 
    # the order of contents sometimes is still decided randomly.
    # data = {'HamburgerA':  [80, 75, 80, 90, 95, 80, 80, 85, 85, 80, 90, 80, 75, 90, 85, 85, 90, 90, 85, 80],
    #         'HamburgerB':  [75, 70, 80, 85, 90, 75, 85, 80, 80, 75, 80, 75, 70, 85, 80, 75, 80, 80, 90, 80],
    #         'HamburgerC' : [80, 80, 80, 90, 95, 85, 95, 90, 85, 90, 95, 85, 98, 95, 85, 85, 90, 90, 85, 85]}
 
    if args[1] == "1":
        # repeated & one-way
        # each person - each condition (conditionA, conditionB, condiitonC)

        #           condition1 condition2 condition3 condition4  
        # person1       100
        # person2                 120
        # person3                             40
        # person4                                        60
        # person5       120
        # ...

        # followed this website for sample: http://kogolab.chillout.jp/elearn/hamburger/chap6/sec0.html
        data['HamburgerA'] = [80, 75, 80, 90, 95, 80, 80, 85, 85, 80, 90, 80, 75, 90, 85, 85, 90, 90, 85, 80]
        data['HamburgerB'] = [75, 70, 80, 85, 90, 75, 85, 80, 80, 75, 80, 75, 70, 85, 80, 75, 80, 80, 90, 80]
        data['HamburgerC'] = [80, 80, 80, 90, 95, 85, 95, 90, 85, 90, 95, 85, 98, 95, 85, 85, 90, 90]
        one_way_anova_draw_table.draw_table(data, mode="CR")
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, test_mode="between-anova")

    elif args[1] == "2":
        
        data['a1'] = [9,7,8,8,12,11,8,13]
        data['a2'] = [6,5,6,3,6,7,10,9]
        data['a3'] = [10,13,8,13,12,14,14,16]
        data['a4'] = [9,11,13,14,16,12,15,14]
        one_way_anova_draw_table.draw_table(data, mode="CR")
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, test_mode="between-anova")
    
    elif args[1] == "3":
        
        data['a1'] = [9,7,8,8,12,11,8,13]
        data['a2'] = [5,6,3,6,7,10]
        data['a3'] = [13,8,13,12,14,16,10]
        data['a4'] = [11,13,14,16,12]
        one_way_anova_draw_table.draw_table(data, mode="CR")
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, test_mode="between-anova")

    elif args[1] == "4":
        # factorical & one-way
        # each person - all conditions (conditionA, conditionB, condiitonC)

        #           condition1    condition2     condition3  
        # person1    100             110            120
        # person2    120             130            140   
        # person3    200             210            130
        # person4    120             140            160
        # person5    110              80            150

        # followed this website for sample: http://kogolab.chillout.jp/elearn/hamburger/chap6/sec0.html
        data['HamburgerA'] = [80, 75, 80, 90, 95, 80, 80, 85, 85, 80, 90, 80, 75, 90, 85, 85, 90, 90, 85, 80]
        data['HamburgerB'] = [75, 70, 80, 85, 90, 75, 85, 80, 80, 75, 80, 75, 70, 85, 80, 75, 80, 80, 90, 80]
        data['HamburgerC'] = [80, 80, 80, 90, 95, 85, 95, 90, 85, 90, 95, 85, 98, 95, 85, 85, 90, 90, 85, 85]
        
        one_way_anova_draw_table.draw_table(data, mode="RB")
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, test_mode="within-anova")

    elif args[1] == "5":

        data['a1'] = [9,7,8,8,12,11,8,13]
        data['a2'] = [6,5,6,3,6,7,10,9]
        data['a3'] = [10,13,8,13,12,14,14,16]
        data['a4'] = [9,11,13,14,16,12,15,14]

        one_way_anova_draw_table.draw_table(data, mode="RB")
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, test_mode="within-anova")


    elif args[1] == "6":
        # repeated & two-way
        # each person - each condition 
        # (conditionA-robot1, conditionA-robot2, conditionB-robot1, conditionB-robot2)

        #           robot1-condition1 robot1-condition2 robot2-condition3 robot2-condition4  
        # person1          100
        # person2                         120
        # person3                                            40
        # person4                                                              60
        # person5          120
        # ...

        data['NAO-Adult'] = [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90]
        data['NAO-Children'] = [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75]
        data['Pepper-Adult'] = [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75]
        data['Pepper-Children'] = [70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70]
        label_a = ["NAO", "Pepper"]
        label_b = ["Adult", "Children"]

        two_way_anova_draw_table.draw_table(data, label_a, label_b, mode="two-factor-repeated")
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, test_mode="between-anova")

    elif args[1] == "7":
        data['a1-b1'] = [3,3,1,3,5]
        data['a1-b2'] = [4,3,4,5,7]
        data['a1-b3'] = [6,6,6,4,8]
        data['a1-b4'] = [5,7,8,7,9]
        data['a2-b1'] = [3,5,2,4,6]
        data['a2-b2'] = [2,6,3,6,4]
        data['a2-b3'] = [3,2,3,6,5]
        data['a2-b4'] = [2,3,3,4,6]
        label_a = ["a1", "a2"]
        label_b = ["b1", "b2", "b3", "b4"]

        two_way_anova_draw_table.draw_table(data, label_a, label_b, mode="two-factor-repeated")
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, test_mode="between-anova")

    elif args[1] == "8":
        data['a1-b1'] = [6,6,4,8,7,5]
        data['a1-b2'] = [3,1,2,2]
        data['a2-b1'] = [5,4,5,4]
        data['a2-b2'] = [5,2,4,6,3,4]
        label_a = ["a1", "a2"]
        label_b = ["b1", "b2"]

        two_way_anova_draw_table.draw_table(data, label_a, label_b, mode="two-factor-repeated")
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, test_mode="between-anova")

    elif args[1] == "9":
        data['a1-b1'] = [3,3,1,3,5]
        data['a1-b2'] = [4,3,4,5,7]
        data['a1-b3'] = [6,6,6,4,8]
        data['a1-b4'] = [5,7,8,7,9]
        data['a2-b1'] = [3,5,2,4,6]
        data['a2-b2'] = [2,6,3,6,4]
        data['a2-b3'] = [3,2,3,6,5]
        data['a2-b4'] = [2,3,3,4,6]
        label_a = ["a1", "a2"]
        label_b = ["b1", "b2", "b3", "b4"]
        two_way_anova.two_way_anova(data, label_a, label_b, mode="SPFpq")
        #two_way_anova_draw_table.draw_table(data, label_a, label_b, mode="two-factor-repeated")
        #draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, test_mode="between-anova")

    elif args[1] == "10":
        data['a1-b1'] = [3,3,1,3,5]
        data['a1-b2'] = [4,3,4,5,7]
        data['a1-b3'] = [6,6,6,4,8]
        data['a1-b4'] = [5,7,8,7,9]
        data['a2-b1'] = [3,5,2,4]
        data['a2-b2'] = [2,6,3,6]
        data['a2-b3'] = [3,2,3,6]
        data['a2-b4'] = [2,3,3,4]
        label_a = ["a1", "a2"]
        label_b = ["b1", "b2", "b3", "b4"]

        two_way_anova.two_way_anova(data, label_a, label_b, mode="SPFpq")

    else:
        print "Please select 1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
