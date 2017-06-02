#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import DataFrame
import numpy as np
from two_way_anova import TwoWayAnova

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


if __name__ == '__main__':
    sample_2x2()
    #sample_2x3()
    

