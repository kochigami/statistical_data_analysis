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
        # Q2 children
        # data = np.array([[43, 28],[19, 52]])
        # Q2 adults
        data = np.array([[8, 12],[11, 9]])
        # Q3 children
        # data = np.array([[4, 7],[4, 10]])
        # Q3 adults
        # data = np.array([[4, 6],[3, 7]])
        # enquette
        # data = np.array([[20, 9],[18, 9]])
        # data = np.array([[21, 9],[17, 9]])

        # data = np.array([[7, 22],[16, 11]])
        # data = np.array([[15, 15],[8, 18]])

        # data = np.array([[16, 13],[12, 15]])
        # data = np.array([[16, 14],[12, 14]])

        # data = np.array([[9, 20],[15, 12]])
        # data = np.array([[15, 12],[11, 15]])

        # d.draw_graph(data, ["Touch", "Speak"], "The ratio of children who touched or spoke to the robot \n on their own accord", "condition", "percentage", tight_layout=True, mode="paired")
        d.draw_graph(data, ["Touch", "Speak"], "The ratio of adults who touched or spoke to the robot \n on their own accord", "condition", "percentage", tight_layout=True, mode="paired")
        # TODO
        # draw table        
