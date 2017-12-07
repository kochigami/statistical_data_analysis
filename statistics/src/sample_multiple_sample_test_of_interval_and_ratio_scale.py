#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from one_way_anova_draw_table import OneWayAnovaDrawTable
from two_way_anova_draw_table import TwoWayAnovaDrawTable
from draw_graph import DrawGraph
from collections import OrderedDict

if __name__ == '__main__':
    args = sys.argv
    if len(args) is not 2:
        print "python sample_multiple_sample_test_of_interval_and_ratio_scale.py <sample_type>"
        print "please choose sample type:"
        print "1: unpaired & one-way"
        print "2: unpaired & two-way"
        print "3: paired & one-way"
        print "4: paired & two-way"
        sys.exit()

    one_way_anova_draw_table = OneWayAnovaDrawTable()
    two_way_anova_draw_table = TwoWayAnovaDrawTable()
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
        # unpaired & one-way
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
        
        one_way_anova_draw_table.draw_table(data)
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, test_mode="between-anova")
        
    elif args[1] == "2":
        # unpaired & two-way
        # each person - each condition 
        # (conditionA-robot1, conditionA-robot2, conditionB-robot1, conditionB-robot2)

        #           robot1-condition1 robot1-condition2 robot2-condition3 robot2-condition4  
        # person1          100
        # person2                         120
        # person3                                            40
        # person4                                                              60
        # person5          120
        # ...

        data = {'NAO-Adult':       [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
                'NAO-Children':    [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
                'Pepper-Adult':    [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
                'Pepper-Children': [70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]}
        label_a = ["NAO", "Pepper"]
        label_b = ["Adult", "Children"]

        two_way_anova_draw_table.draw_table(data, label_a, label_b, mode="between")
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, test_mode="between-anova")

    elif args[1] == "3":
        # paired & one-way
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

        one_way_anova_draw_table.draw_table(data, mode="within")
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, test_mode="within-anova")

    elif args[1] == "4":
        # paired & two-way
        # each person - all conditions (personal difference + time) 

        #           time1    time2     time3  
        # person1    100     110       120
        # person2    120     130       140   
        # person3    200     210       130
        # person4    120     140       160
        # person5    110     80        150

        data = {'Box-Tsukurioki':  [65, 75, 70, 75, 90, 80, 65, 50, 55, 80, 90, 70, 75, 80, 75],
                'Box-Order': [70, 80, 75, 75, 95, 80, 75, 55, 50, 85, 80, 70, 75, 80, 60],
                'Paper-Tsukurioki' : [50, 55, 70, 75, 80, 85, 65, 55, 55, 75, 80, 75, 70, 65, 55],
                'Paper-Order' : [60, 65, 75, 80, 90, 80, 80, 55, 60, 82, 80, 70, 90, 70, 60]}
        label_a = ["Box", "Paper"]
        label_b = ["Tsukurioki", "Order"]

        two_way_anova_draw_table.draw_table(data, label_a, label_b, mode="within")
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, test_mode="within-anova")

    else:
        print "Please select 1, 2, 3, 4"
