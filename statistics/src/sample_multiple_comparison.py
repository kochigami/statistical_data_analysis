#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from multiple_comparison import MultipleComparison
from collections import OrderedDict

if __name__ == '__main__':
    multiple_comparison = MultipleComparison()
    args = sys.argv
    if len(args) is not 2:
        print "python sample_comparison.py <sample_type>"
        print "please choose sample type: "
        print "1: cochran"
        print "2: chi-squared test"
    else:
        data = OrderedDict()
        if args[1] == "1":
            data["CandidateA"] = [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            data["CandidateB"] = [1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
            data["CandidateC"] = [1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0]
            multiple_comparison.test(data, test="cochran")
        elif args[1] == "2":
            data["A"] = [12, 10, 8]
            data["B"] = [5, 7, 20]
            data["C"] = [7, 6, 7] 
            data["D"] = [1, 3, 4]
            multiple_comparison.test(data, test="chi-squared")
