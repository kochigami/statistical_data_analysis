#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import DataFrame
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import math

class TTEST:
    def make_df(self, data):
        df = DataFrame(data, index = ["sample" + str(i+1)  for i  in np.arange(len(data.values()[0]))])
        return df

    def draw_graph(self, df, label, xlabel, ylabel, title, p):
        """
        fig: make figure instance
        """
        fig = plt.figure()
        """
        y_data: calculate sample_data_average as list [ave_0, ave_1]
        max_y_data: max y value for scale
        """
        y_data = [ df[label[0]].mean(), df[label[1]].mean()]
        max_y_data = math.ceil(max(y_data))
        """
        y_error: calculate sample_error as list [err_0, err_1]
        left: list of x value for each bar, now it is just empty
        """
        y_error = [ df[label[0]].std(ddof=False), df[label[1]].std(ddof=False)]
        left = np.array([])
        """
        left: list of x value (the number of order) for each bar
        """
        for i in range(len(label)):
            left = np.append(left, i+1)
        """
        make bar:
        left: list of x value (the number of order)
        y_data: list of y value
        (width: the width of bar, default is 0.8)
        color: bar color
        yerr: error list of y value
        align: position to x bar (default is "edge")
        ecolor: color of yerror
        capsize: umbrella size of yerror
        """
        plt.bar(left, y_data, color="#FF5B70", yerr=y_error, align="center", ecolor="blue", capsize=60)
        """
        plt.rcParams["font.size"]: modify character size in a graph
        plt.tick_params(labelsize=28): modify character size in x, ylabel
        """
        plt.rcParams["font.size"] = 28
        plt.tick_params(labelsize=28)
        """
        add y_value in each bar
        """
        ax = plt.gca()
        w = 0.4
        for j in range(len(y_data)):
            ann = ax.annotate(str((round (y_data[j] * 100.0)) * 0.01), xy=(left[j] - w * 0.5, y_data[j] / 2.0), fontsize=28)
        """
        add x_value in each bar
        """
        plt.xticks(left, label)
        """
        add title, label
        """
        new_title = title + "\n(N = " + str(len(df['Japanese'])) + ", * p < 0.1, ** p < 0.05)"
        plt.title(new_title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        """
        add p value and mark
        """
        if p < 0.05:
            input_word = "**" + " (p = " + str(round (p * 1000.0) * 0.001) + " )"
            plt.text(1.0, max_y_data * 0.95, input_word)
        elif p < 0.1:
            input_word = "*" + " (p = " + str(round (p * 1000.0) * 0.001) + " )"
            plt.text(1.0, max_y_data * 0.95, input_word)
        else:
            input_word = " p = " + str(round (p * 1000.0) * 0.001)
            plt.text(1.0, max_y_data * 0.95, input_word)
        plt.text(1.0, max_y_data * 0.85, "|----------------|")
        """
        show grid
        """
        plt.grid(True)
        """
        make graph small in order not to overlap each label
        """
        fig.tight_layout()
        """
        show graph
        """
        plt.show()

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
        self.draw_graph(df, label, xlabel, ylabel, title, p)

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
        self.draw_graph(df, label, xlabel, ylabel, title, p)
