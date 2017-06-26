#!/usr/bin/env python
# -*- coding: utf-8 -*-

#このファイルの絶対パス
#print os.path.abspath(os.path.dirname(__file__))

#このファイルの1つ上のディレクトリの絶対パス
#print os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/anova')
from anova import ANOVA

if __name__ == '__main__':
     args = sys.argv
     if len(args) < 2:
          print "input which sample case you want to try: 1-4"

     else:
          if args[1] == "1":
               data = {'Japanese':  [68, 75, 80, 71, 73, 79, 69, 65],
                       'Mathematics': [86, 83, 76, 81, 75, 82, 87, 75],
                       'Science' : [85, 69, 77, 77, 75, 74, 87, 69],
                       'English': [80, 76, 84, 93, 76, 80, 79, 84]}
          elif args[1] == "2":
               data = {'Japanese':  [80, 75, 80, 90, 95, 80, 80, 85, 85, 80, 90, 80, 75, 90, 85, 85, 90, 90, 85, 80],
                       'Mathematics': [75, 70, 80, 85, 90, 75, 85, 80, 80, 75, 80, 75, 70, 85, 80, 75, 80, 80, 90, 80],
                       'Science' : [80, 80, 80, 90, 95, 85, 95, 90, 85, 90, 95, 85, 98, 95, 85, 85, 90, 90, 85, 85]}
          elif args[1] == "3":
               ### first ###
               data = {'vision':  [2.03678, 1.870811, 2.860442, 3.23255, 2.26, 1.686727],
                       'sound': [7.67, 2.721273, 1.5, 2.586297, 3.43, 2.685902],
                       'vision + sound' : [1.42923, 1.54, 1.89001, 2.021806, 2.33, 1.06]}
          elif args[1] == "4":
               ### second ###
               data = {'vision':  [2.148006, 2.198387, 2.009008, 2.033217, 2.148546, 1.64081],
                       'sound': [1.597316, 1.6, 2.398989, 2.418485, 2.306829, 1.579134],
                       'vision + sound' : [1.442516, 1.873331, 1.755275, 2.190506, 3.176726, 2.009838]}

          if len(args) == 3:
               test_mode = args[2]

          else:
               test_mode = "between"

          anova = ANOVA()
          anova.one_way_anova(data, test_mode)
          anova.draw_graph(data, "Average of each type", "type", "average value")
