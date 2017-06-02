#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import DataFrame
import numpy as np
from one_way_anova import OneWayAnova

def sample1():
     data = {'Japanese':  [68, 75, 80, 71, 73, 79, 69, 65],
             'Mathematics': [86, 83, 76, 81, 75, 82, 87, 75],
             'Science' : [85, 69, 77, 77, 75, 74, 87, 69],
             'English': [80, 76, 84, 93, 76, 80, 79, 84]}
     data_all = {'all': [68, 75, 80, 71, 73, 79, 69, 65, 86, 83, 76, 81, 75, 82, 87, 75, 85, 69, 77, 77, 75, 74, 87, 69, 80, 76, 84, 93, 76, 80, 79, 84]}

     df = DataFrame(data, index = [str(i+1)  for i  in np.arange(8)]) # must change the length of array
     df_all = DataFrame(data_all, index = [str(i+1)  for i  in np.arange(32)])
     
     one_way_anova = OneWayAnova()
     one_way_anova.calc_one_way_anova(df, ['Japanese', 'Mathematics', 'Science', 'English'], df_all, ['all'])

def sample2():
     data = {'Japanese':  [80, 75, 80, 90, 95, 80, 80, 85, 85, 80, 90, 80, 75, 90, 85, 85, 90, 90, 85, 80],
             'Mathematics': [75, 70, 80, 85, 90, 75, 85, 80, 80, 75, 80, 75, 70, 85, 80, 75, 80, 80, 90, 80],
             'Science' : [80, 80, 80, 90, 95, 85, 95, 90, 85, 90, 95, 85, 98, 95, 85, 85, 90, 90, 85, 85]}
     data_all = {'all': [80, 75, 80, 90, 95, 80, 80, 85, 85, 80, 90, 80, 75, 90, 85, 85, 90, 90, 85, 80, 75, 70, 80, 85, 90, 75, 85, 80, 80, 75, 80, 75, 70, 85, 80, 75, 80, 80, 90, 80, 80, 80, 80, 90, 95, 85, 95, 90, 85, 90, 95, 85, 98, 95, 85, 85, 90, 90, 85, 85]}

     df = DataFrame(data, index = [str(i+1)  for i  in np.arange(20)]) # must change the length of array
     df_all = DataFrame(data_all, index = [str(i+1)  for i  in np.arange(60)])

     one_way_anova = OneWayAnova()
     one_way_anova.calc_one_way_anova(df, ['Japanese', 'Mathematics', 'Science'], df_all, ['all'])

def sample3():
     data = {'vision':  [2.148006, 2.198387, 2.009008, 2.033217, 2.148546, 1.64081],
             'sound': [1.597316, 1.6, 2.398989, 2.418485, 2.306829, 1.579134],
             'vision + sound' : [1.442516, 1.873331, 1.755275, 2.190506, 3.176726, 2.009838]}
     data_all = {'all': [2.148006, 2.198387, 2.009008, 2.033217, 2.148546, 1.64081, 1.597316, 1.6, 2.398989, 2.418485, 2.306829, 1.579134, 1.442516, 1.873331, 1.755275, 2.190506, 3.176726, 2.009838]}
     
     df = DataFrame(data, index = [str(i+1)  for i  in np.arange(6)]) # must change the length of array
     df_all = DataFrame(data_all, index = [str(i+1)  for i  in np.arange(18)])
     
     one_way_anova = OneWayAnova()
     one_way_anova.calc_one_way_anova(df, ['vision', 'sound', 'vision + sound'], df_all, ['all'])

if __name__ == '__main__':
     #sample1()
     #sample2()
     sample3()
