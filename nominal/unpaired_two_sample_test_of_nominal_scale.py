#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
#from chi_squared_test_draw_graph import ChiSquaredTestDrawGraph
#from chi_squared_test_draw_table import ChiSquaredTestDrawTable
from nominal.chi_squared_test import ChiSquaredTest
from nominal.fisher_test import FisherTest

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
                            Yes   No   Yes/No   Total
              --------------------------------------
              Condition1     a     b    c      a+b+c
              Condition2     c     d    d      d+e+f
              --------------------------------------
              Total         a+c   b+d  c+d     n (= a+b+c+d)
            """
            data1 = []
            data2 = []

            for i in range(len(data[(data.keys())[0]])):
                data1.append(data[(data.keys())[0]][i])
            for i in range(len(data[(data.keys())[1]])):
                data2.append(data[(data.keys())[1]][i])
            
            sum_row = [] # ex. 3
            sum_column = [] # ex. 2
            for i in range(len(data[(data.keys())[0]])):
                sum_row.append(data[(data.keys())[0]][i] + data[(data.keys())[1]][i])
                
            for i in range(len(data.keys())):
                sum_column.append(sum(data[(data.keys())[i]]))
            
            n = sum(data[(data.keys())[0]]) + sum(data[(data.keys())[1]])

            data1_exp = []
            data2_exp = []
            for i in range(len(data[(data.keys())[0]])): # ex. 3
                data1_exp.append((sum_row[i] * sum_column[0]) / float(n))
            for i in range(len(data[(data.keys())[1]])): # ex. 3
                data2_exp.append((sum_row[i] * sum_column[1]) / float(n))

            """
            fisher test is used in a certain condition; see http://aoki2.si.gunma-u.ac.jp/lecture/Cross/warning.html
                                                            and http://drmagician.exblog.jp/22086293/
            """
            min_exp = 10000
            for i in range(len(data1_exp)):
                if min_exp > data1_exp[i]:
                    min_exp = data1_exp[i]
            for i in range(len(data2_exp)):
                if min_exp > data2_exp[i]:
                    min_exp = data2_exp[i]
            
            if min_exp < 5:
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
