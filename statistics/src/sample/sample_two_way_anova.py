#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append( os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/anova')
from anova import ANOVA

"""
Be careful for names of each factor.
Each name shouldn't include other.
For example, "vision", "sound", "vision+sound" is bad because thrid one (vision+sound) includes first (vision) and second one (sound).
In this case, "vision", "sound", "both" is good.  
"""

if __name__ == '__main__':
    args = sys.argv

    if len(args) is not 2:
        print "input which sample case you want to try: 2x2, 2x3, 2x3_nao"

    else:
        if args[1] == "2x2":
            data = {'Crispy-hot':  [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
                    'Crispy-mild': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
                    'Normal-hot' : [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
                    'Normal-mild' : [70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]}
            factor1_label = ["Crispy", "Normal"]
            factor2_label = ["hot", "mild"]

        elif args[1] == "2x3":
            data = {'Crispy-hot':  [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
                    'Crispy-normal': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
                    'Crispy-mild': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
                    'Normal-hot' : [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
                    'Normal-normal' : [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
                    'Normal-mild' : [70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]}
            factor1_label = ["Crispy", "Normal"]
            factor2_label = ["hot", "normal", "mild"]

        elif args[1] == "2x3_nao":
            data = {'first-vision' : [2.03678, 1.870811, 2.860442, 3.23255, 2.26, 1.686727],
                    'first-sound' : [7.67, 2.721273, 1.5, 2.586297, 3.43, 2.685902],
                    'first-both' : [1.42923, 1.54, 1.89001, 2.021806, 2.33, 1.06],
                    'second-vision':  [2.148006, 2.198387, 2.009008, 2.033217, 2.148546, 1.64081],
                    'second-sound': [1.597316, 1.6, 2.398989, 2.418485, 2.306829, 1.579134],
                    'second-both': [1.442516, 1.873331, 1.755275, 2.190506, 3.176726, 2.009838]}
            factor1_label = ["first", "second"]
            factor2_label = ["vision", "sound", "both"]
        
        anova = ANOVA()
        anova.two_way_anova(data, factor1_label, factor2_label)
        anova.draw_graph(data, "Experiment Result", "type", "value")
