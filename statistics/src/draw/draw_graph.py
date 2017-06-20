#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import math
import numpy as np

class DrawGraph:
    def draw_graph(self, df, label, title, xlabel, ylabel, p=None, mode="paired-ttest"):
        """
        fig: make figure instance
        """
        fig = plt.figure()
        """
        y_data: calculate sample_data_average as list [ave_0, ave_1, ave_2]
        max_y_data: max y value for scale
        """
        y_data = []
        for i in range(len(label)):
            y_data.append(df[label[i]].mean())
        max_y_data = math.ceil(max(y_data))
        """
        y_error: calculate sample_error as list [err_0, err_1]
        left: list of x value for each bar, now it is just empty
        """
        y_error = []
        for i in range(len(label)):
            y_error.append(df[label[i]].std(ddof=False))
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
        plt.tick_params(labelsize=12)
        """
        add y_value in each bar
        """
        ax = plt.gca()
        w = 0.4
        for i in range(len(y_data)):
            ann = ax.annotate(str((round (y_data[i] * 100.0)) * 0.01), xy=(left[i] - w * 0.5, y_data[i] / 2.0), fontsize=28)
        """
        add x_value in each bar
        """
        plt.xticks(left, label)
        """
        add title, label
        """
        if mode == "anova":
            new_title = title + "\n(N = " + str(len(df[label[0]])) + " for each type)"
        elif mode == "paired-ttest":
            new_title = title + "\n(N = " + str(len(df[label[0]])) + " for each type, * p < 0.1, ** p < 0.05)"
        elif mode == "unpaired-ttest":
            new_title = title + "\n(N = " + str(len(df[label[0]]) * len(label)) + " for total, * p < 0.1, ** p < 0.05)"
        plt.title(new_title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        
        if (mode == "paired-ttest" or mode == "unpaired-ttest") and p is not None:
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
            plt.text(1.0, max_y_data * 0.85, "|---------------------------|")
        
        """
        show grid
        """
        plt.grid(True)
        """
        make graph small in order not to overlap each label
        memo: especially in t-test, which sentences are very long, 
        graph is made very small in order not to overlap.
        That's why I comment in this line. If necessary, please comment out it.
        """
        # fig.tight_layout()
        """
        show graph
        """
        plt.show()

