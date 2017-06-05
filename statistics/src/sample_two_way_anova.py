#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import DataFrame
import numpy as np
from two_way_anova import TwoWayAnova
import sys

def sample_2x2():
    data = {'Crispy-hot':  [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
            'Crispy-mild': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
            'Normal-hot' : [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
            'Normal-mild' : [70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]}
    
    df = DataFrame(data, index = [str(i+1)  for i  in np.arange(15)])
    
    data_factor1 = {'Crispy': [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90, 65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
                    'Normal': [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75, 70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]}
    
    data_factor2 = {'hot': [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90, 70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75], 
                    'mild': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75, 70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]}

    df_factor1 = DataFrame(data_factor1, index = [str(i+1)  for i  in np.arange(30)])
    df_factor2 = DataFrame(data_factor2, index = [str(i+1)  for i  in np.arange(30)])
    
    data_all = {'all': [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90, 65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75, 70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75, 70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]}
    
    df_all = DataFrame(data_all, index = [str(i+1) for i in np.arange(60)])
    
    two_way_anova = TwoWayAnova()
    two_way_anova.calc_two_way_anova(df, ['Crispy-hot', 'Crispy-mild', 'Normal-hot', 'Normal-mild'], df_factor1, ['Crispy', 'Normal'], df_factor2, ['hot', 'mild'], df_all, ['all'])

def sample_2x3():
    data = {'Crispy-hot':  [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
            'Crispy-normal': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
            'Crispy-mild': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
            'Normal-hot' : [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
            'Normal-normal' : [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
            'Normal-mild' : [70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]
        }

    df = DataFrame(data, index = [str(i+1)  for i  in np.arange(15)])
    
    data_factor1 = {'Crispy': [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90, 65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75, 65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
                    'Normal': [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75, 70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75, 70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]}

    data_factor2 = {'hot': [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90, 70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
                    'normal': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75, 70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
                    'mild': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75, 70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]}

    df_factor1 = DataFrame(data_factor1, index = [str(i+1)  for i  in np.arange(45)])
    df_factor2 = DataFrame(data_factor2, index = [str(i+1)  for i  in np.arange(30)])

    data_all = {'all': [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90, 65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75, 65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75, 70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75, 70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75, 70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]
            }

    df_all = DataFrame(data_all, index = [str(i+1) for i in np.arange(90)])

    two_way_anova = TwoWayAnova()
    two_way_anova.calc_two_way_anova(df, ['Crispy-hot', 'Crispy-normal', 'Crispy-mild', 'Normal-hot', 'Normal-normal', 'Normal-mild'], df_factor1, ['Crispy', 'Normal'], df_factor2, ['hot', 'normal', 'mild'], df_all, ['all'])

def sample_2x3_nao():
    data = {'first-vision' : [2.03678, 1.870811, 2.860442, 3.23255, 2.26, 1.686727],
            'first-sound' : [7.67, 2.721273, 1.5, 2.586297, 3.43, 2.685902],
            'first-vision+sound' : [1.42923, 1.54, 1.89001, 2.021806, 2.33, 1.06],
            'second-vision':  [2.148006, 2.198387, 2.009008, 2.033217, 2.148546, 1.64081],
            'second-sound': [1.597316, 1.6, 2.398989, 2.418485, 2.306829, 1.579134],
            'second-vision+sound': [1.442516, 1.873331, 1.755275, 2.190506, 3.176726, 2.009838]
        }

    df = DataFrame(data, index = [str(i+1)  for i  in np.arange(6)])
    
    data_factor1 = {'first': [2.03678, 1.870811, 2.860442, 3.23255, 2.26, 1.686727, 7.67, 2.721273, 1.5, 2.586297, 3.43, 2.685902, 1.42923, 1.54, 1.89001, 2.021806, 2.33, 1.06],
                    'second': [2.148006, 2.198387, 2.009008, 2.033217, 2.148546, 1.64081, 1.597316, 1.6, 2.398989, 2.418485, 2.306829, 1.579134, 1.442516, 1.873331, 1.755275, 2.190506, 3.176726, 2.009838]}

    data_factor2 = {'vision': [2.03678, 1.870811, 2.860442, 3.23255, 2.26, 1.686727, 2.148006, 2.198387, 2.009008, 2.033217, 2.148546, 1.64081],
                    'sound': [7.67, 2.721273, 1.5, 2.586297, 3.43, 2.685902, 1.597316, 1.6, 2.398989, 2.418485, 2.306829, 1.579134],
                    'vision+sound': [1.42923, 1.54, 1.89001, 2.021806, 2.33, 1.06, 1.442516, 1.873331, 1.755275, 2.190506, 3.176726, 2.009838]}

    df_factor1 = DataFrame(data_factor1, index = [str(i+1)  for i  in np.arange(18)])
    df_factor2 = DataFrame(data_factor2, index = [str(i+1)  for i  in np.arange(12)])

    data_all = {'all': [2.03678, 1.870811, 2.860442, 3.23255, 2.26, 1.686727, 7.67, 2.721273, 1.5, 2.586297, 3.43, 2.685902, 1.42923, 1.54, 1.89001, 2.021806, 2.33, 1.06, 2.148006, 2.198387, 2.009008, 2.033217, 2.148546, 1.64081, 1.597316, 1.6, 2.398989, 2.418485, 2.306829, 1.579134, 1.442516, 1.873331, 1.755275, 2.190506, 3.176726, 2.009838]
            }

    df_all = DataFrame(data_all, index = [str(i+1) for i in np.arange(36)])

    two_way_anova = TwoWayAnova()
    two_way_anova.calc_two_way_anova(df, ['first-vision', 'first-sound', 'first-vision+sound', 'second-vision', 'second-sound', 'second-vision+sound'], df_factor1, ['first', 'second'], df_factor2, ['vision', 'sound', 'vision+sound'], df_all, ['all'])


if __name__ == '__main__':
    args = sys.argv
    if args[1] == "2x2":
        sample_2x2()
    elif args[1] == "2x3":
        sample_2x3()
    elif args[1] == "2x3_nao":
        sample_2x3_nao()    

