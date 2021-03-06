#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from draw.chi_squared_test_draw_table import ChiSquaredTestDrawTable
from nominal.paired_two_sample_test_of_nominal_scale import PairedTwoSampleTestOfNominalScale
from nominal.unpaired_two_sample_test_of_nominal_scale import UnpairedTwoSampleTestOfNominalScale
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

            '''
            convert data as data["Agree"] = [54, 25], data["Disagree"] = [36, 65]
            (Before, After)
            '''
            data_converted = OrderedDict()
            data_converted["Agree"] = []
            data_converted["Disagree"] = []
            for i in data.keys():
                tmp_agree = 0
                tmp_disagree = 0
                for j in range(len(data[i])):
                    if data[i][j] == 1:
                        tmp_agree +=1
                    elif data[i][j] == 0:
                        tmp_disagree +=1
                data_converted["Agree"].append(tmp_agree)
                data_converted["Disagree"].append(tmp_disagree)

            print "A McNemar Test was performed to examine the relation between approval of a question and a lecture from a company. The relation between these variables was significant, X^2(dof=1)=18.23, p<.01. People after taking a lecture from a company were less likely to show an approval of a question than were people before taking a lecture from a company."
            draw_table.draw_table(p, data_converted, ["Before", "After"], ["Agree", "Disagree"], "Change in opinions about approval of a question before and after a lecture from a company")

        elif args[1] == "2":
            '''
            病気の患者，健常者のうち，喫煙者と非喫煙者の分布を調べる．
                           Smoker Non-Smoker Total
             -------------------------------------
             Illness         52       8       60
             Healty          48      42       90
             ------------------------------------
             Total          100      50      150

             OrderedDict([('Illness', [52, 8]), ('Healthy', [48, 42])])
            '''
            data = OrderedDict()
            data["Illness"] = [52, 8]
            data["Healthy"] = [48, 42]
            unpaired_two_sample_test_of_nominal_scale = UnpairedTwoSampleTestOfNominalScale() 
            squared, p, dof, ef = unpaired_two_sample_test_of_nominal_scale.test(data)
            print "A chi-square test of independence was performed to examine the relation between the habit of smoking and health conditions. The relation between these variables was significant, X^2(dof={}) = {}, p={} (Note: It may be better to write 'p<.01'). Non-smokers were less likely to have illness than were smokers.".format(dof, squared, p)
            print "カイ二乗検定を喫煙率に実施した．その結果，病気の患者の喫煙率({}%)は，健常者の喫煙率({}%)より有意に高いことが明らかになった．(x_2 ({}) = {}, p < 0.01)".format(5200/60.0, 4800/90.0, dof, squared)
            draw_table.draw_table(p, data, ["Illness", "Healthy"], ["Smoker", "Non-Smoker"], "The number of smokers who have illness and don't have illness")

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
            print "Fisher's Exact Test indicated that primary outcome results indicated a non-significant reduction in the tendency of taking care of non-social behavior in the teacher group with a prevelence of {}% ({}/{}), compared to {}% ({}/{}) in the counselor group (p={}).".format(100/(1+12.0), 1, 1+12, 400/(4+6.0), 4, 10, p)
            draw_table.draw_table(p, data, ["Teacher", "Counselor"], ["Non-social", "Antisocial"], "Evaluation about children's problematic behaviors by teachers and counselors")

        else:
            print "python sample_two_sample_test_of_nominal_scale.py <sample_type>"
            print "please choose sample type: "
            print "1: paired test"
            print "2: unpaired test + big data"
            print "3: unpaired test + small data"
