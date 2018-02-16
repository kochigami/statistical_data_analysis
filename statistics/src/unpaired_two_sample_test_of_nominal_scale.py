#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
#from chi_squared_test_draw_graph import ChiSquaredTestDrawGraph
#from chi_squared_test_draw_table import ChiSquaredTestDrawTable
from chi_squared_test import ChiSquaredTest
from fisher_test import FisherTest

class UnpairedTwoSampleTestOfNominalScale:
    def test(self, data):
        # check data length is 2
        if len(data.keys()) != 2 and len(data[(data.keys())[0]]) != 2 and len(data[(data.keys())[1]]) != 2:
            print "Please check the components of your data."
            print "length of data should be four"
            sys.exit()
        else:
            """
            data = {"Yes": [a, c], "No": [b, d]}
                            Yes   No   Total
              -------------------------------
              Condition1     a     b    a+b
              Condition2     c     d    c+d
              -------------------------------
              Total         a+c   b+d   n (= a+b+c+d)
            """
            a = data[(data.keys())[0]][0]
            c = data[(data.keys())[0]][1]
            b = data[(data.keys())[1]][0]
            d = data[(data.keys())[1]][1]
            n = a+b+c+d

            """
            fisher test is used in a certain condition; see http://aoki2.si.gunma-u.ac.jp/lecture/Cross/warning.html
                                                            and http://drmagician.exblog.jp/22086293/
            """
            a_exp = (a+c) * (a+b) / float(n)
            c_exp = (a+c) * (c+d) / float(n)
            b_exp = (b+d) * (a+b) / float(n)            
            d_exp = (b+d) * (c+d) / float(n)

            if a_exp < 5 or b_exp < 5 or c_exp < 5 or d_exp < 5:
                # use fisher's test
                # followd this link: http://aoki2.si.gunma-u.ac.jp/lecture/Cross/Fisher.html
                fisher_test = FisherTest()
                p = fisher_test.test(data)
                return p
            else:
                # use chi-squared test
                chi_squared_test = ChiSquaredTest()
                p = chi_squared_test.test(data)
                return p
                # d = ChiSquaredTestDrawGraph()
                # t = ChiSquaredTestDrawTable()
                # d.draw_graph(data, ["Condition1", "Condition2"], "test", "x", "y", tight_layout=True)
                # t.draw_table(data, ["Condition1", "Condition2"], "test")
                
if __name__ == '__main__':
    pass
