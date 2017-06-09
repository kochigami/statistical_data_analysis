#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import DataFrame
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import math
from draw_graph import DrawGraph

class TTEST:
    def make_df(self, data):
        df = DataFrame(data, index = ["sample" + str(i+1)  for i  in np.arange(len(data.values()[0]))])
        return df

    def paired_ttest(self, data, title, label, xlabel, ylabel):
        """
        data = {'Japanese':  [68, 75, 80, 71, 73, 79, 69, 65],
        'Mathematics': [86, 83, 76, 81, 75, 82, 87, 75],
        'Science' : [85, 69, 77, 77, 75, 74, 87, 69],
        'English': [80, 76, 84, 93, 76, 80, 79, 84]}
        title: "Test"
        label: ["Japanese", "English"]
        xlabel: "type"
        ylabel: "average"
        """
        """
        make df
        """
        df = self.make_df(data)
        """
        If samples are paired,
        we use paired t-test
        """
        # calculate t & p value
        t, p = stats.ttest_rel(df[label[0]], df[label[1]])
        print( "p value = %(p)s" %locals() )
        """
        draw gragh
        """
        draw_graph = DrawGraph()
        draw_graph.draw_graph(df, label, title, xlabel, ylabel, p, mode="paired-ttest")

    def unpaired_ttest(self, data, title, label, xlabel, ylabel):
        """
        data = {'Japanese':  [68, 75, 80, 71, 73, 79, 69, 65],
        'Mathematics': [86, 83, 76, 81, 75, 82, 87, 75],
        'Science' : [85, 69, 77, 77, 75, 74, 87, 69],
        'English': [80, 76, 84, 93, 76, 80, 79, 84]}
        title: "Test"
        label: ["Japanese", "English"] 
        xlabel: "type"
        ylabel: "average"
        """
        """
        make df
        """
        df = self.make_df(data)
        """
        If samples are not paired,
        we use unpaired t-test.
        We have to investigate whether the distribution is equall (tou bunsan) 
        by calculating f.
        We have to choose larger one as numerator (bunshi)
        """
        if np.var(df[label[0]]) > np.var(df[label[1]]):
            f = np.var(df[label[0]]) / np.var(df[label[1]])
        else:
            f = np.var(df[label[1]]) / np.var(df[label[0]])
        dfx = len(df[label[0]]) - 1
        dfy = len(df[label[1]]) - 1
        p_value = stats.f.cdf(f, dfx, dfy)

        """
        After obtaining p value, 
        we can check whether the distribution of samples is equal or not.
        If p < 0.05, we use t-test with not equal variance
        otherwise, we use t-test with equal variance
        """
        # calculate t & p value
        if p_value < 0.05:
            t, p = stats.ttest_ind(df[label[0]], df[label[1]], equal_var = False)
            ### heteroscedasticity: hi tou bunsan
            print ("t-test with heteroscedasticity")
        else:
            t, p = stats.ttest_ind(df[label[0]], df[label[1]], equal_var = True)
            ### homoscedasticity: tou bunsan
            print ("t-test with homoscedasticity")

        print( "p value = %(p)s" %locals() )

        """
        draw gragh
        """
        draw_graph = DrawGraph()
        draw_graph.draw_graph(df, label, title, xlabel, ylabel, p, mode="unpaired-ttest")
