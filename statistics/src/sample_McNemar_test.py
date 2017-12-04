#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from McNemar_test import McNemarTest

"""
focus on YES => NO & NO => YES
data[0]: number of YES => NO
data[1]: number of NO => YES
"""
if __name__ == '__main__':
    mcnemar_test = McNemarTest()
    p = mcnemar_test.test([1, 8])
    print p
