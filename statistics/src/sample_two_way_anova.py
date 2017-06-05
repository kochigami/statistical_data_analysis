#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import DataFrame
import numpy as np
from two_way_anova import TwoWayAnova
from analysis_of_variance import AnalysisOfVariance
import sys

if __name__ == '__main__':
    args = sys.argv

    analysis_of_variance = AnalysisOfVariance()

    if args[1] == "2x2":
        data = {'Crispy-hot':  [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
                'Crispy-mild': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
                'Normal-hot' : [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
                'Normal-mild' : [70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]}
        df_factor1 = analysis_of_variance.create_df(data, ["Crispy", "Normal"])
        df_factor2 = analysis_of_variance.create_df(data, ["hot", "mild"])

    elif args[1] == "2x3":
        data = {'Crispy-hot':  [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
                'Crispy-normal': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
                'Crispy-mild': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
                'Normal-hot' : [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
                'Normal-normal' : [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
                'Normal-mild' : [70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]}
        df_factor1 = analysis_of_variance.create_df(data, ["Crispy", "Normal"])
        df_factor2 = analysis_of_variance.create_df(data, ["hot", "normal", "mild"])

    elif args[1] == "2x3_nao":
        data = {'first-vision' : [2.03678, 1.870811, 2.860442, 3.23255, 2.26, 1.686727],
                'first-sound' : [7.67, 2.721273, 1.5, 2.586297, 3.43, 2.685902],
                'first-both' : [1.42923, 1.54, 1.89001, 2.021806, 2.33, 1.06],
                'second-vision':  [2.148006, 2.198387, 2.009008, 2.033217, 2.148546, 1.64081],
                'second-sound': [1.597316, 1.6, 2.398989, 2.418485, 2.306829, 1.579134],
                'second-both': [1.442516, 1.873331, 1.755275, 2.190506, 3.176726, 2.009838]}
        df_factor1 = analysis_of_variance.create_df(data, ["first", "second"])
        df_factor2 = analysis_of_variance.create_df(data, ["vision", "sound", "both"])

    df = analysis_of_variance.create_df(data)
    df_label = analysis_of_variance.create_label(df)
    df_factor1_label = analysis_of_variance.create_label(df_factor1)
    df_factor2_label = analysis_of_variance.create_label(df_factor2)
    df_all = analysis_of_variance.create_df(data, "all")
    df_all_label = analysis_of_variance.create_label(df_all)
    two_way_anova = TwoWayAnova()
    two_way_anova.calc_two_way_anova(df, df_label, df_factor1, df_factor1_label, df_factor2, df_factor2_label, df_all, df_all_label)
