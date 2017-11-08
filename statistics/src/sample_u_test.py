#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from draw_graph import DrawGraph
from collections import OrderedDict

if __name__ == '__main__':
    args = sys.argv
    if len(args) is not 2:
        print "python sample_u_test.py <sample_type>"
        print "please choose sample type: "
        print "1: paired-utest (sign test)"
        print "2: paired-utest (z test)"
        print "3: unpaired-ttest (mann-whitney test)"
    else:
        d = DrawGraph()
        # if we use normal dict, the order of contents sometimes is decided randomly.
        # ex: should be [A, B, C], but output is [A, C, B]
        data = OrderedDict()
        if args[1] == "1":
            data['Cusine_A'] = [5, 3, 4, 4, 3, 4, 4, 1, 3, 3, 5, 3]
            data['Cusine_B'] = [3, 5, 3, 3, 5, 2, 2, 1, 4, 2, 2, 3]
            d.draw_graph(data, "test", "x", "y", tight_layout=True, test_mode="paired-utest")

        elif args[1] == "2":
            data['Cusine_A'] = [5, 3, 4, 4, 3, 4, 4, 1, 3, 2, 5, 3, 2, 3, 5, 4, 2, 3, 5, 4, 1, 2, 3, 2, 3, 5, 2, 3, 3, 5]
            data['Cusine_B'] = [3, 5, 3, 3, 5, 2, 2, 1, 4, 1, 2, 3, 4, 3, 2, 3,
 5, 2, 3, 3, 3, 2, 2, 4, 1, 4, 4, 5, 4, 4]
            d.draw_graph(data, "test", "x", "y", tight_layout=True, test_mode="paired-utest")

        elif args[1] == "3":
            data['Children'] = [20, 18, 15, 13, 10, 6]
            data['Adults'] = [17, 16, 12, 9, 8, 6, 4, 2]
            d.draw_graph(data, "test", "x", "y", tight_layout=True, test_mode="unpaired-utest")

            # if we use OrderedDict, but if we use the initialization below,
            # the order of contents sometimes is still decided randomly.
            # data = {'HamburgerA':  [15.3, 14.9, 14.5, 14.4, 14.0, 13.9, 14.1, 14.7, 15.3, 14.6],
            #         'HamburgerB' : [13.9, 14.2, 14.1, 14.3, 14.1, 13.7, 14.7, 13.9, 14.1, 13.8, 14.3]}
