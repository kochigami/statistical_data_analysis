#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from draw.chi_squared_test_draw_table import ChiSquaredTestDrawTable
from nominal.one_condition_nominal_scale import TestOfOneConditionWithNominalScale
from collections import OrderedDict

if __name__ == '__main__':
    args = sys.argv
    if len(args) is not 2:
        print "python sample_one_sample_test_of_nominal_scale.py <sample_type>"
        print "please choose sample type: "
        print "1: one condition test + two factors (binominal test)"
        print "2: one condition test + more than two factors (chi-square test)"
    else:
        draw_table = ChiSquaredTestDrawTable()
        if args[1] == "1":
            '''
            世界中でのO型血液者の比率は45%であることが知られている．
            ある国で120人を無作為に抽出．そのうち34人がO型だった．
            この国におけるO型血液者の割合は，世界全体より低いか．
            (心理学のためのデータ解析テクニカルブック p. 180 を参照)
            '''
            data = OrderedDict()
            data["O"] = 34
            data["Others"] = 86
            test_of_one_condition_with_nominal_scale = TestOfOneConditionWithNominalScale()
            p = test_of_one_condition_with_nominal_scale.test(data,p_threshold=0.45)

        elif args[1] == "2":
            '''
            養育態度診断テストより，F県下の無作為に抽出された母親160人の養育態度を調べた．
            すると，過干渉型 72, 放任型 23, 拒否型 16, 溺愛型 49人となった．
            F県下の母親においては，各養育態度タイプの人数に偏りがあるか．
            (心理学のためのデータ解析テクニカルブック p. 181 を参照)
            '''
            data = OrderedDict()
            data["Kakansho"] = 72
            data["Honin"] = 23
            data["Kyohi"] = 16
            data["Dekiai"] = 49
            test_of_one_condition_with_nominal_scale = TestOfOneConditionWithNominalScale()
            p = test_of_one_condition_with_nominal_scale.test(data)
            
        else:
            print "python sample_one_sample_test_of_nominal_scale.py <sample_type>"
            print "please choose sample type: "
            print "1: one condition test: binominal test"
            print "2: one condition test: chi-square test"
