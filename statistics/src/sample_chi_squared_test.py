#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
from chi_squared_test_draw_graph import ChiSquaredTestDrawGraph
from chi_squared_test_draw_table import ChiSquaredTestDrawTable

if __name__ == '__main__':
    args = sys.argv
    if len(args) is not 1:
        print "python sample_chi_squared_test.py"
    else:
        d = ChiSquaredTestDrawGraph()
        t = ChiSquaredTestDrawTable()
        data = np.array([[1625, 5],[1022, 11]])
        d.draw_graph(data, ["Condition1", "Condition2"], "test", "x", "y", tight_layout=True)
        t.draw_table(data, ["Condition1", "Condition2"], "test")
