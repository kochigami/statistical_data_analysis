#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from fisher_test import FisherTest

"""
              Yes   No   Total
-------------------------------
Condition1     a     b    a+b
Condition2     c     d    c+d
-------------------------------
Total         a+c   b+d   n (= a+b+c+d)

data: [a, b, c, d]

followd this link: http://aoki2.si.gunma-u.ac.jp/lecture/Cross/Fisher.html
fisher test is used in a certain condition; see http://aoki2.si.gunma-u.ac.jp/lecture/Cross/warning.html
http://drmagician.exblog.jp/22086293/
"""
if __name__ == '__main__':
    fisher_test = FisherTest()
    p = fisher_test.test([13, 4, 6, 14])
    #p = fisher_test.test([228, 863, 284, 851])
    print p
