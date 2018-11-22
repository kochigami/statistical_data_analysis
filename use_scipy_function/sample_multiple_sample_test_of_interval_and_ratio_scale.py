#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from scipy.stats import f_oneway
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
        sys.exit()

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
        f, p = f_oneway(data['HamburgerA'], data['HamburgerB'], data['HamburgerC'])
        print f
        print p

    elif args[1] == "2":
        '''
        別々の人に，20個の単語を4つの条件のどれかを使って覚えてもらう．
        いくつ覚えられるか．
        '''
        data['a1'] = [9,7,8,8,12,11,8,13]
        data['a2'] = [6,5,6,3,6,7,10,9]
        data['a3'] = [10,13,8,13,12,14,14,16]
        data['a4'] = [9,11,13,14,16,12,15,14]
        f, p = f_oneway(data['a1'], data['a2'], data['a3'], data['a4'])
        print f
        print p
    
    elif args[1] == "3":
        '''
        別々の人に，20個の単語を4つの条件のどれかを使って覚えてもらう．
        いくつ覚えられるか．
        '''
        data['a1'] = [9,7,8,8,12,11,8,13]
        data['a2'] = [5,6,3,6,7,10]
        data['a3'] = [13,8,13,12,14,16,10]
        data['a4'] = [11,13,14,16,12]
        f, p = f_oneway(data['a1'], data['a2'], data['a3'], data['a4'])
        print f
        print p

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

        f, p = f_oneway(data['HamburgerA'], data['HamburgerB'], data['HamburgerC'])
        print f
        print p

    elif args[1] == "5":
        '''
        児童をIQに応じてグループ分けし，
        4つの教授法を国語理解度に注目して評価する．
        '''
        data['a1'] = [9,7,8,8,12,11,8,13]
        data['a2'] = [6,5,6,3,6,7,10,9]
        data['a3'] = [10,13,8,13,12,14,14,16]
        data['a4'] = [9,11,13,14,16,12,15,14]
        f, p = f_oneway(data['a1'], data['a2'], data['a3'], data['a4'])
        print f
        print p

    else:
        print "Please select 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11"
