#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy.stats import chi2_contingency
import scipy.stats as fisher_exact
from scipy.stats.contingency import expected_freq

class UnpairedTwoSampleTestOfNominalScale:
    def test(self, data):
        # check data length
        if len(data.keys()) != 2:
            print "The number of your data type should be two"
            sys.exit()
        else:
            label_x = data.keys()[0]
            label_y = data.keys()[1]
            data_x = data[label_x]
            data_y = data[label_y]

            if len(data_x) != len(data_y):
                print "The number of data length should be same."
                sys.exit()
            else:
                """
                Is there any difference between the number of people who satisfies Condition1 and Yes (a) and that of people who satisfies Condition2 and Yes (c)?
                data = {"Condition1": [a, b], "Condition2": [c, d]}
                
                             Yes   No   Total
                --------------------------------------
                Condition1     a     b    a+b
                Condition2     c     d    c+d
                --------------------------------------
                Total         a+c   b+d    n (= a+b+c+d)
                """

                # (data.keys())[0]: "Condition1"
                # data[(data.keys())[0]]: [a, b]
                data_exp = expected_freq([data[(data.keys())[0]], data[(data.keys())[1]]])
                
                # select the way of calculation based on the minimum expected data (fisher's test or chi-square test)
                """
                fisher test is used in a certain condition (Cochran's rule); 
                see http://aoki2.si.gunma-u.ac.jp/lecture/Cross/warning.html and
                http://drmagician.exblog.jp/22086293/
                """
                if min(min(data_exp[0]), min(data_exp[1])) < 5:
                    # use fisher's test
                    oddsratio, p = stats.fisher_exact([data[(data.keys())[0]], data[(data.keys())[1]]])
                else:
                    # use chi-square test
                    chi2, p, dof, expected = chi2_contingency([data[(data.keys())[0]], data[(data.keys())[1]]])
                return p
                
if __name__ == '__main__':
    pass
