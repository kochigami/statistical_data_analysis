#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from interval_and_ratio.one_way_anova_draw_table import OneWayAnovaDrawTable
from interval_and_ratio.two_way_anova_draw_table import TwoWayAnovaDrawTable
from draw.draw_graph import DrawGraph
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
        print "11: two-way anova RBFpq"
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
        print "A one-way between subjects ANOVA was conducted to compare the effect of a type of hamburger on the score of taste. An analysis of variance showed that the effect of a type of hamburger on the score was significant at the p<.05 level, F(2, 55)=12.26, p=0.001. Post hoc comparisons using the holm test indicated that the mean score for the HamburgerA (M=84.0, SD=5.39) was significantly different than the HamburgerB (M=79.5, SD=5.45) (p<.001). The HamburgerA (M=84.0, SD=5.39) was significantly different than the HamburgerC (M=88.5, SD=5.52) (p=0.0076). The HamburgerB (M=79.5, SD=5.45) was significantly different than the HamburgerC (M=88.5, SD=5.52) (p=0.0091). "
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, sample_type="unpaired")

    elif args[1] == "2":
        '''
        別々の人に，20個の単語を4つの条件のどれかを使って覚えてもらう．
        いくつ覚えられるか．
        '''
        data['a1'] = [9,7,8,8,12,11,8,13]
        data['a2'] = [6,5,6,3,6,7,10,9]
        data['a3'] = [10,13,8,13,12,14,14,16]
        data['a4'] = [9,11,13,14,16,12,15,14]
        one_way_anova_draw_table.draw_table(data, mode="CR")
        print "A one-way between subjects ANOVA was conducted to compare the effect of a type of study on the number of word learned. An analysis of variance showed that the effect of a type of study on the number of word learned was significant at the p<.05 level, F(3, 31)=13.72, p=0.001. Post hoc comparisons using the holm test indicated that the mean number for a1 (M=9.5, SD=2.1) was significantly different than a2 (M=6.5, SD=2.1) (p=0.01). The mean number of a1 was significantly different than the mean number of a3 (M=12.5, SD=2.3) (p=0.01). The mean number of a1 was significantly different than the mean number of a4 (M=13.0, SD=2.1) (p=0.004). The mean number of a2 was significantly different than the mean number of a3 (p<.005). The mean number of a2 was significantly different than the mean number of a4 (p<.005). "
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, sample_type="unpaired")
    
    elif args[1] == "3":
        '''
        別々の人に，20個の単語を4つの条件のどれかを使って覚えてもらう．
        いくつ覚えられるか．
        '''
        data['a1'] = [9,7,8,8,12,11,8,13]
        data['a2'] = [5,6,3,6,7,10]
        data['a3'] = [13,8,13,12,14,16,10]
        data['a4'] = [11,13,14,16,12]
        one_way_anova_draw_table.draw_table(data, mode="CR")
        print "A one-way between subjects ANOVA was conducted to compare the effect of a type of study on the number of word learned. An analysis of variance showed that the effect of a type of study on the number of word learned was significant at the p<.05 level, F(3, 25)=11.09, p=0.001. Post hoc comparisons using the holm test indicated that the mean number for a1 (M=9.5, SD=2.1) was significantly different than a2 (M=6.17, SD=2.1) (p=0.01). The mean number of a1 was significantly different than the mean number of a3 (M=12.3, SD=2.4) (p=0.018). The mean number of a1 was significantly different than the mean number of a4 (M=13.2, SD=2.7) (p=0.008). The mean number of a2 was significantly different than the mean number of a3 (p<.005). The mean number of a2 was significantly different than the mean number of a4 (p<.005). "
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, sample_type="unpaired")

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
        print "A one-way repeated measures ANOVA was conducted to compare the effect of a type of hamburger on the score of taste. These data consist of the scores of 20 people. Each person was evaluated under three conditions. The results of a one-way repeated measures ANOVA show that the score of taste was significantly affected by a type of hamburger, F(2, 38)=23.17, p=0.001. The score of taste was significantly affected by a type of subject, F(19, 38)=3.69, p=0.001. Post hoc comparisons using the Holm test indicated that there was no significant difference between HamburgerA (M=84.0, SD=5.39), HamburgerB (M=79.5, SD=5.45) and HamburgerC (M=88.2, SD=5.34)."
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, sample_type="paired")

    elif args[1] == "5":
        '''
        児童をIQに応じてグループ分けし，
        4つの教授法を国語理解度に注目して評価する．
        '''
        data['a1'] = [9,7,8,8,12,11,8,13]
        data['a2'] = [6,5,6,3,6,7,10,9]
        data['a3'] = [10,13,8,13,12,14,14,16]
        data['a4'] = [9,11,13,14,16,12,15,14]

        one_way_anova_draw_table.draw_table(data, mode="RB")
        print "A one-way repeated measures ANOVA was conducted to compare the effect of a type of study on the score of test. These data consist of the scores of 8 people. Each person was evaluated under four conditions. The results of a one-way repeated measures ANOVA show that the score of test was significantly affected by a type of study, F(3, 21)=21.45, p=0.001. The score of test was not significantly affected by a type of subject, F(7, 21)=3.26, p=0.017. Post hoc comparisons using the Holm test indicated that there was no significant difference between a1 (M=9.5, SD=2.06), a2 (M=6.5, SD=2.06), a3 (M=12.5, SD=2.35) and a4 (M=13.0, SD=2.12)."
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, sample_type="paired")

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

        two_way_anova_draw_table.draw_table(data, label_a, label_b, mode="CRFpq")
        print "A two-way between subjects ANOVA was conducted on the influence of two independent variables (robot type and people age) on the number of a score of people's satisfactiory of interaction with a robot. Robot type included two levels (NAO and Pepper) and people age consisted of two levels (Adult and Children). All effects were statistically significant at the .05 significance level except for robot type. The main effect for robot type type yielded an F ratio of F(1, 54)=1.48, p=0.23, indicating a significant difference between NAO (M=75.3, SD=8.56), Pepper (M=72.9, SD=7.49). The main effect for people age yielded an F ratio of F(1, 54)=4.15, p=0.047, indicating a significant difference between Children (M=72.0, SD=7.36) and Adults (M=76.2, SD=8.33). The interaction effect was significant, F(1, 54)=5.02, p=0.03. Post hoc comparisons using the HSD test indicated a significant difference between NAO & Adults (M=79.67, SD=7.63) and Pepper & Adults (M=72.67, SD=7.50), and NAO & Children (M=71.0, SD=7.12) and NAO & Adults (M=79.67, SD=7.63). No other comparisons were statically significant."
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, sample_type="unpaired")

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

        two_way_anova_draw_table.draw_table(data, label_a, label_b, mode="CRFpq")
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, sample_type="unpaired")

    elif args[1] == "8":
        '''
        条件A:他者のいる条件・他者のいない条件
        条件B:不安傾向高・不安傾向低
        
        児童に課題をやってもらう．成績を評価．
        '''
        data['a1-b1'] = [6,6,4,8,7,5]
        data['a1-b2'] = [3,1,2,2]
        data['a2-b1'] = [5,4,5,4]
        data['a2-b2'] = [5,2,4,6,3,4]
        label_a = ["a1", "a2"]
        label_b = ["b1", "b2"]

        two_way_anova_draw_table.draw_table(data, label_a, label_b, mode="CRFpq")
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, sample_type="unpaired")

    elif args[1] == "9":
        '''
        要因Aには異なる被験者が無作為に割り当てられている．
        要因Bには同一の被験者が全ての条件を行う or 被験者をブロック化し，そのブロック内の被験者を各条件に無作為に割り当てる．
        '''
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
        two_way_anova_draw_table.draw_table(data, label_a, label_b, mode="SPFpq")
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, sample_type="unpaired")

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
        two_way_anova_draw_table.draw_table(data, label_a, label_b, mode="SPFpq")
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, sample_type="unpaired")

    elif args[1] == "11":
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
        two_way_anova_draw_table.draw_table(data, label_a, label_b, mode="RBFpq")
        print "The sleep quality (percentage of time spent in delta sleep) of people with a1 and a2 (N=2x5) was measured when sleeping with b1, b2, b3 and b4. A 2 x 4 ANOVA with category of a1 & a2 as an independent factor and category of b1, b2, b3 and b4 as a within-subjects factor was run. The analysis revealed a main effect of a category of a1 & a2 (F(1, 4)=8.1, p=0.047) in the predicted direction, a main effect of a category of b1, b2, b3 and b4 (F(3, 12)=6.04, p=0.01) and an interaction between a category of a1 & a2 and a category of b1, b2, b3 and b4 (F(3, 12)=7.08, p=0.006). "
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, sample_type="paired")

    else:
        print "Please select 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11"
