#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from nominal.chi_squared_test import ChiSquaredTest
from nominal.fisher_test import FisherTest

class UnpairedTwoSampleTestOfNominalScale:
    def test(self, data):
        # check data length
        if len(data.keys()) != 2:
            print "len(data.keys()) should be two"
            sys.exit()
        elif len(data[(data.keys())[0]]) != len(data[(data.keys())[1]]):
            print "len(data[(data.keys())[0]]) and len(data[(data.keys())[1]]) should be same"
            sys.exit()
        else:
            """
            Is there any difference between the number of people who satisfies Condition1 and Yes (a) and that of people who satisfies Condition2 and Yes (c)?
            data = {"Condition1": [a, b], "Condition2": [c, d]}
            OrderedDict([('Illness', [52, 8]), ('Healty', [48, 42])])

                            Yes   No   Total <= sum_row
              --------------------------------------
              Condition1     a     b    a+b
              Condition2     c     d    c+d
              --------------------------------------
              Total         a+c   b+d    n (= a+b+c+d)
               ^
               |_ sum_column 

            """
            # calculate n
            n = sum(data[(data.keys())[0]]) + sum(data[(data.keys())[1]])

            sum_row = []
            sum_column = []

            # calculate sum_column
            for i in range(len(data[(data.keys())[0]])):
                tmp = 0.0
                for j in data.keys():
                    tmp += data[j][i]
                sum_column.append(tmp)

            # calculate sum_row
            for i in data.keys():
                sum_row.append(sum(data[i]))

            # calculate expected data
            data_exp = []
            for i in range(len(data[(data.keys())[0]])):
                for j in range(len(data.keys())):
                    data_exp.append(sum_row[j] * sum_column[i] / float(n))

            # select the way of calculation based on the minimum expected data (fisher's test or chi-square test)
            """
            fisher test is used in a certain condition (Cochran's rule); 
            see http://aoki2.si.gunma-u.ac.jp/lecture/Cross/warning.html and
                http://drmagician.exblog.jp/22086293/
            """
            if min(data_exp) < 5: 
                # use fisher's test
                # followd this link: http://aoki2.si.gunma-u.ac.jp/lecture/Cross/Fisher.html
                fisher_test = FisherTest()
                p = fisher_test.test(data)
                return p
            else:
                # use chi-square test
                chi_squared_test = ChiSquaredTest()
                '''
                squared: 検定統計量
                p: p value
                dof: 自由度
                ef: 期待度数
                '''
                squared, p, dof, ef = chi_squared_test.test(data)
                return squared, p, dof, ef
                
if __name__ == '__main__':
    pass
