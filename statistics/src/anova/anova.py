#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import math
import numpy as np
from analysis_of_variance import AnalysisOfVariance
from one_way_anova import OneWayAnova
from two_way_anova import TwoWayAnova

import sys
import os
sys.path.append( os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/draw')
from draw_graph import DrawGraph

class ANOVA:
    def __init__(self):
        pass

    def one_way_anova(self, data, test_mode="between"): ### temporary
        """
        Args:
        data = {'Japanese':  [68, 75, 80, 71, 73, 79, 69, 65],
        'Mathematics': [86, 83, 76, 81, 75, 82, 87, 75],
        'Science' : [85, 69, 77, 77, 75, 74, 87, 69],
        'English': [80, 76, 84, 93, 76, 80, 79, 84]}
        """
        analysis_of_variance = AnalysisOfVariance()
        df = analysis_of_variance.create_df(data)
        df_label = analysis_of_variance.create_label(df)
        df_all = analysis_of_variance.create_df(data, "all")
        df_all_label = analysis_of_variance.create_label(df_all)
        one_way_anova = OneWayAnova()
        one_way_anova.calc_one_way_anova(df, df_label, df_all, df_all_label, test_mode)

    def two_way_anova(self, data, factor1_label, factor2_label, test_mode):
        """
        Args:
        data = {'Crispy-hot':  [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
        'Crispy-mild': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
        'Normal-hot' : [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
        'Normal-mild' : [70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]}
        factor1_label: ["Crispy", "Normal"]
        factor2_label: ["hot", "mild"]
        
        %Be careful for names of each factor.
        Each name shouldn't include other.
        For example, "vision", "sound", "vision+sound" is bad because thrid one (vision+sound) includes first (vision) and second one (sound).
        In this case, "vision", "sound", "both" is good.  
        
        """

        analysis_of_variance = AnalysisOfVariance()
        
        df_factor1 = analysis_of_variance.create_df(data, factor1_label)
        df_factor2 = analysis_of_variance.create_df(data, factor2_label)
        
        df = analysis_of_variance.create_df(data)
        df_label = analysis_of_variance.create_label(df)
        df_factor1_label = analysis_of_variance.create_label(df_factor1)
        df_factor2_label = analysis_of_variance.create_label(df_factor2)
        df_all = analysis_of_variance.create_df(data, "all")
        df_all_label = analysis_of_variance.create_label(df_all)
        two_way_anova = TwoWayAnova()
        two_way_anova.calc_two_way_anova(df, df_label, df_factor1, df_factor1_label, df_factor2, df_factor2_label, df_all, df_all_label, test_mode)

    def draw_graph(self, data, title, xlabel, ylabel):
        """
        make df
        """
        analysis_of_variance = AnalysisOfVariance()
        df = analysis_of_variance.create_df(data)
        label = analysis_of_variance.create_label(df)

        draw_graph = DrawGraph()
        draw_graph.draw_graph(df, label, title, xlabel, ylabel, mode="anova")

if __name__ == '__main__':
    pass
