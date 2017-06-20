#!/usr/bin/env python
import sys
import os
sys.path.append( os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/t_test')
from t_test import TTEST 

if __name__ == '__main__':
    data = {'Japanese':  [68, 75, 80, 71, 73, 79, 69, 65],
            'Mathematics': [86, 83, 76, 81, 75, 82, 87, 75],
            'Science' : [85, 69, 77, 77, 75, 74, 87, 69],
            'English': [80, 76, 84, 93, 76, 80, 79, 84]}

    t_test = TTEST()

    args = sys.argv
    if args[1] == "unpaired":
    ### unpaired-t-test ###
        t_test.unpaired_ttest(data, "Test", ["Japanese", "English"], "type", "average")
    elif args[1] == "paired":
    ### unpaired-t-test ###
        t_test.paired_ttest(data, "Test", ["Japanese", "English"], "type", "average")
    else:
        print "please check argument"
