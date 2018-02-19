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
        print "1: chi-squared test"
        print "2: mcnemar test"
        print "3: mann-whitney test"
        print "4: signed test"
    else:
        data = OrderedDict()
        if args[1] == "1":
            data["A"] = [12, 10, 8]
            data["B"] = [5, 7, 20]
            data["C"] = [7, 6, 7] 
            data["D"] = [1, 3, 4]
            multiple_comparison.test(data, test="chi-squared")
        elif args[1] == "2":
            data["CandidateA"] = [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            data["CandidateB"] = [1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
            data["CandidateC"] = [1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0]
            multiple_comparison.test(data, test="mcnemar")
        elif args[1] == "3":
            data["A"] = [3.88,4.60,6.30,2.15,4.80,5.20]
            data["B"] = [2.86,9.02,4.27,9.86,3.66,5.48] 
            data["C"] = [1.82,4.21,3.10,1.99,2.75,2.18]            
            multiple_comparison.test(data, test="mann-whitney")
        elif args[1] == "4":
            data["A"] = [1,5,1,5,5,4,5]
            data["B"] = [2,1,2,1,4,2,4]
            data["C"] = [3,3,3,4,2,1,2]
            data["D"] = [5,2,4,2,3,3,3]            
            data["E"] = [4,4,5,3,1,5,1]
            multiple_comparison.test(data, test="signed-test")
        else:
            print "python sample_comparison.py <sample_type>"
            print "please choose sample type: "
            print "1: cochran test"
            print "2: chi-squared test"
            print "3: mann-whitney test"
            print "4: signed test"
