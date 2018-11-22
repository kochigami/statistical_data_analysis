#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from draw.draw_box_graph import DrawBoxGraph
from ordinal.unpaired_multiple_sample_test_of_ordinal_scale import UnpairedMultipleSampleTestOfOrdinalScale
from ordinal.paired_multiple_sample_test_of_ordinal_scale import PairedMultipleSampleTestOfOrdinalScale
from collections import OrderedDict

if __name__ == '__main__':
    args = sys.argv
    if len(args) is not 2:
        print "python sample_multiple_sample_test_of_ordinal_scale.py <sample_type>"
        print "please choose sample type: "
        print "1: unpaired test (Kruskal-Wallis test)"
        print "2: paired test (Friedman test)"
    else:
        draw_box_graph = DrawBoxGraph()
        if args[1] == "1":
            '''
            ABCの条件で ある刺激に対する幼児の反応時間を測定する．
            一人の幼児につき，A,B,Cのどれか一つの反応時間を調べるものとする．
            条件間に有意な差が認められるか．
           (心理学のためのデータ解析テクニカルブック p. 213 を参照)

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
            dof, H, p, mean_rank = unpaired_multiple_sample_test_of_ordinal_scale.test(data)
            y_data, y_error = draw_box_graph.draw_graph(data, "test", "x", "y")
            print "A Kruskal Wallis Test indicated that there was a statistically significant difference between the time which infants reacted to a specific stimulus (H({}) ={}, p={}), with a mean rank of {} for condition1, {} for condition2, {} for condition3. Post hoc comparisons using Ryan's test indicated that the mean score for the condition2 (M=12.5, SD=2.66) was significantly different than the condition3 (M=4.83, SD=0.81). The mean score for the condition1 (M=11.2, SD=1.27) was significantly different than the condition3 (M=4.83, SD=0.82). However, the condition1 did not significantly differ from codition2.".format(dof, H, p, mean_rank[0], mean_rank[1], mean_rank[2], y_data[0], y_error[0], y_data[1], y_error[1], y_data[2], y_error[2])

        elif args[1] == "2":
            '''
            CM 5本を 7人の評定者に順位付けしてもらう．
            5本のCMに対する好ましさの間に有意な差があるといえるか．
            (心理学のためのデータ解析テクニカルブック p. 215 を参照)

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
            S, p = paired_multiple_sample_test_of_ordinal_scale.test(data)
            y_data, y_error = draw_box_graph.draw_graph(data, "test", "x", "y")
            print "A non-parametric Friedman test of differences among repeated measures was conducted and rendered a Chi-square value of {}, which was not significant (p =  {}).".format(S, p)

        else:
            print "python sample_multiple_sample_test_of_ordinal_scale.py <sample_type>"
            print "please choose sample type: "
            print "1: unpaired test (Kruskal-Wallis test)"
            print "2: paired test (Friedman test)"
