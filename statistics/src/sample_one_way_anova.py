#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from one_way_anova_draw_table import DrawTable
from draw_graph import DrawGraph
from collections import OrderedDict

if __name__ == '__main__':
    args = sys.argv
    if len(args) is not 2:
        print "python sample_one_way_anova.py <sample_type>"
        print "please choose sample type: "
        print "between: welch's test and unpaired-ttest"
        print "within: student's test and unpaired-ttest"
        sys.exit()

    draw_table = DrawTable()
    draw_graph = DrawGraph()
    # if we use normal dict, the order of contents sometimes is decided randomly.
    # ex: should be [A, B, C], but output is [A, C, B]
    data = OrderedDict()

    # followed this website for sample: http://kogolab.chillout.jp/elearn/hamburger/chap6/sec0.html
    data['HamburgerA'] = [80, 75, 80, 90, 95, 80, 80, 85, 85, 80, 90, 80, 75, 90, 85, 85, 90, 90, 85, 80]
    data['HamburgerB'] = [75, 70, 80, 85, 90, 75, 85, 80, 80, 75, 80, 75, 70, 85, 80, 75, 80, 80, 90, 80]
    data['HamburgerC'] = [80, 80, 80, 90, 95, 85, 95, 90, 85, 90, 95, 85, 98, 95, 85, 85, 90, 90, 85, 85]
    
    # if we use OrderedDict, but if we use the initialization below, 
    # the order of contents sometimes is still decided randomly.
    # data = {'HamburgerA':  [80, 75, 80, 90, 95, 80, 80, 85, 85, 80, 90, 80, 75, 90, 85, 85, 90, 90, 85, 80],
    #         'HamburgerB':  [75, 70, 80, 85, 90, 75, 85, 80, 80, 75, 80, 75, 70, 85, 80, 75, 80, 80, 90, 80],
    #         'HamburgerC' : [80, 80, 80, 90, 95, 85, 95, 90, 85, 90, 95, 85, 98, 95, 85, 85, 90, 90, 85, 85]}
 
    if args[1] == "between":
        draw_table.draw_table(data)
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, test_mode="between-anova")
    elif args[1] == "within":
        draw_table.draw_table(data, mode="within")
        draw_graph.draw_graph(data, "test", "x", "y", tight_layout=True, test_mode="within-anova")
    else:
        print "Please select between or within."
