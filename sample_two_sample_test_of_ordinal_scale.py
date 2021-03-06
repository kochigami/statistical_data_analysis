#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy
from draw.draw_box_graph import DrawBoxGraph
from ordinal.paired_two_sample_test_of_ordinal_scale import PairedTwoSampleTestOfOrdinalScale
from ordinal.unpaired_two_sample_test_of_ordinal_scale import UnpairedTwoSampleTestOfOrdinalScale
from collections import OrderedDict

if __name__ == '__main__':
    args = sys.argv
    if len(args) is not 2:
        print "python two_sample_test_of_ordinal_scale.py <sample_type>"
        print "please choose sample type: "
        print "1: paired test (signed test + small data)"
        print "2: paired test (signed test + big data)"
        print "3: paired test (signed rank sum test)"
        print "4: unpaired test (mann-whitney test)"
    else:
        paired_two_sample_test_of_ordinal_scale = PairedTwoSampleTestOfOrdinalScale()
        unpaired_two_sample_test_of_ordinal_scale = UnpairedTwoSampleTestOfOrdinalScale()
        # if we use normal dict, the order of contents sometimes is decided randomly.
        # ex: should be [A, B, C], but output is [A, C, B]
        data = OrderedDict()
        draw_box_graph = DrawBoxGraph()
        if args[1] == "1":
            '''
            ref: https://kusuri-jouhou.com/statistics/fugou.html
            12人にA, B両方の料理を食べてもらい，5点満点で採点してもらう．
            A, Bの料理のおいしさに差はあるか．

            data:

            Subject | CusineA | CusineB | 
            -----------------------------
            1           5         3               
            2           3         5      
            3           4         3      
            4           4         3        
            5           3         5         
            6           4         2        
            7           4         2                  
            8           1         1        
            9           3         4        
            10          3         2      
            11          5         2       
            12          3         3     
            '''
            data['Cusine_A'] = [5, 3, 4, 4, 3, 4, 4, 1, 3, 3, 5, 3]
            data['Cusine_B'] = [3, 5, 3, 3, 5, 2, 2, 1, 4, 2, 2, 3]
            p = paired_two_sample_test_of_ordinal_scale.test(data, mode="signed_test")
            print "A sign test indicated that there is not significant difference between the score of cusine A (Mdn=3.5) and that of cusine B (Mdn=3.0); p=0.34."
            draw_box_graph.draw_graph(data, "test", "x", "y")

        elif args[1] == "2":
            '''
            ref: https://kusuri-jouhou.com/statistics/fugou.html
            30人にA, B両方の料理を食べてもらい，5点満点で採点してもらう．
            A, Bの料理のおいしさに差はあるか．

            data:

            Subject | CusineA | CusineB |
            -----------------------------
            1           5         3
            2           3         5
            3           4         3
            4           4         3
            5           3         5
            6           4         2
            7           4         2
            8           1         1
            9           3         4
            10          3         2
            11          5         2
            12          3         3
            13          2         4
            14          3         3
            15          5         2
            16          4         3
            17          2         5
            18          3         2
            19          5         3
            20          4         3
            21          1         3
            22          2         2
            23          3         2
            24          2         4
            25          3         1
            26          5         4
            27          2         4
            28          3         5
            29          3         4
            30          5         4
            '''
            data['Cusine_A'] = [5, 3, 4, 4, 3, 4, 4, 1, 3, 2, 5, 3, 2, 3, 5, 4, 2, 3, 5, 4, 1, 2, 3, 2, 3, 5, 2, 3, 3, 5]
            data['Cusine_B'] = [3, 5, 3, 3, 5, 2, 2, 1, 4, 1, 2, 3, 4, 3, 2, 3, 5, 2, 3, 3, 3, 2, 2, 4, 1, 4, 4, 5, 4, 4]
            p = paired_two_sample_test_of_ordinal_scale.test(data, mode="signed_test")
            print "A sign test indicated that there is not significant difference between the score of cusine A (Mdn=3.0) and that of cusine B (Mdn=3.0); p=0.33."
            draw_box_graph.draw_graph(data, "test", "x", "y")

        elif args[1] == "3":
            '''
            10人の人に，A, B両方の商品を過去３ヶ月で使用した回数を尋ねる．
            Subject | ProductA | ProductB | a_i - b_i ||a_i - b_i| order
            ----------------------------------------------------------
            1           25         26         -1          1          
            2           62         31         +31         9
            3           58         35         +23         8
            4           26         24         +2          2
            5           42         47         -5          3.5
            6           18         13         +5          3.5
            7           11         11         0           ---
            8           33         21         +12         6
            9           50         42         +8          5
            10          34         18         +16         7
            ----------------------------------------------------------
            '''
            data['Product_A'] = [25, 62, 58, 26, 42, 18, 11, 33, 50, 34]
            data['Product_B'] = [26, 31, 35, 24, 47, 13, 11, 21, 42, 18]
            p = paired_two_sample_test_of_ordinal_scale.test(data, mode="signed_rank_sum_test")
            print "Signed rank sum test indicated that the number of times 10 people used product A in the three months (Mdn=33.5) was statistically significantly higher than the number of times they used product B in three months (Mdn=25.0)"
            draw_box_graph.draw_graph(data, "test", "x", "y")

        elif args[1] == "4":
            '''
            ラット 20匹に24時間ご飯をあげない．21匹には48時間あげない．その後学習を行わせ，学習基準に到達するまでの試行回数を調べる．
            両条件の試行数に有意な差が認められるか．
            (心理学のためのデータ解析テクニカルブック p. 207 を参照)
            '''
            data['24hour'] = [13, 14, 24, 28, 29, 35, 59, 83, 84, 89, 94, 97, 98, 117, 118, 128, 131, 175, 200, 200]
            data['48hour'] = [10, 12, 13, 16, 18, 21, 28, 28, 39, 40, 47, 57, 58, 62, 68, 69, 70, 82, 95, 111, 127]
            p = unpaired_two_sample_test_of_ordinal_scale.test(data)
            print "A Mann-Whitney test indicated that the number of trials which satisfied with the learning criteria was greater for mice which did not eat anything for 48 hours (Mdn=47.0) than for mice which did not eat anything for 24 hours (Mdn=91.5), U=117.5, p=0.008."
            draw_box_graph.draw_graph(data, "test", "x", "y") 
            
            # if we use OrderedDict, but if we use the initialization below,
            # the order of contents sometimes is still decided randomly.
            # data = {'HamburgerA':  [15.3, 14.9, 14.5, 14.4, 14.0, 13.9, 14.1, 14.7, 15.3, 14.6],
            #         'HamburgerB' : [13.9, 14.2, 14.1, 14.3, 14.1, 13.7, 14.7, 13.9, 14.1, 13.8, 14.3]}
