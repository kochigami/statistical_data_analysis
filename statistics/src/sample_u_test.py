#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from draw_graph import DrawGraph
from collections import OrderedDict

if __name__ == '__main__':
    args = sys.argv
    if len(args) is not 1:
        print "python sample_u_test.py"
    else:
        d = DrawGraph()
        # if we use normal dict, the order of contents sometimes is decided randomly.
        # ex: should be [A, B, C], but output is [A, C, B]
        data = OrderedDict()
        data['Children'] = [20, 18, 15, 13, 10, 6]
        data['Adults'] = [17, 16, 12, 9, 8, 6, 4, 2]
        d.draw_graph(data, "test", "x", "y", tight_layout=True, test_mode="utest")
        
        # if we use OrderedDict, but if we use the initialization below, 
        # the order of contents sometimes is still decided randomly.
        # data = {'HamburgerA':  [15.3, 14.9, 14.5, 14.4, 14.0, 13.9, 14.1, 14.7, 15.3, 14.6],
        #         'HamburgerB' : [13.9, 14.2, 14.1, 14.3, 14.1, 13.7, 14.7, 13.9, 14.1, 13.8, 14.3]}
