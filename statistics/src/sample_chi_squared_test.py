#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
from chi_squared_test_draw_graph import ChiSquaredTestDrawGraph

# TODO
# draw graph and table
# See: http://www.f.kpu-m.ac.jp/c/kouza/joho/kiso/topics/kentei/top.html#fig

if __name__ == '__main__':
    args = sys.argv
    if len(args) is not 1:
        print "python sample_chi_squared_test.py"
    else:
        d = ChiSquaredTestDrawGraph()
        # Q2
        # data = np.array([[26, 27],[7, 10]])
        # Q3 children
        data = np.array([[43, 28],[19, 52]])
        # Q3 adults
        #data = np.array([[8, 12],[11, 9]])
        d.draw_graph(data, ["Condition1", "Condition2"], "test", "x", "y", tight_layout=True, mode="paired")
        # TODO
        # draw table        
