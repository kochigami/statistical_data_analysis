#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import math
import numpy as np

class DrawGraph:
    """
    displaying bar graph which contains average data per sample group
    
    if test_mode is paired, data is like this.
    data = {'Crispy':  [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
    'Normal' : [70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]}
    Be sure that string list is like ([category1, category2]).
    
    title: string.
    xlabel: string.
    ylabel: string.
    tight_layout: bool. if execute tight_layout, set True.
    sample_type: string. paired, unpaired
    p: float. if conducted test is two sample test, it is required.
    """
    def draw_graph(self, data, title, xlabel, ylabel, p=None, tight_layout=False, sample_type="paired", is_scale_nominal=False):
        """
        fig: make figure instance
        """
        fig = plt.figure()
        """
        y_data: if nominal scale is not used: calculate sample_data_average as list [ave_0, ave_1, ave_2]
                if nominal scale is used    : calculate sample_data_total_num as list [total_0, total_1, total_2]
        max_y_data: max y value for scale
        """
        y_data = []
        if is_scale_nominal == False:
            for i in range(len(data.keys())):
                y_data.append(np.mean(data[(data.keys())[i]]))
        else:
            for i in range(len(data.keys())):
                y_data.append(sum(data[(data.keys())[i]]))

        print "y_data: " + str(y_data)
        """
        y_error: calculate sample_error as list [err_0, err_1]
        is scale is nominal: it is not calculated
        left: list of x value for each bar, now it is just empty
        ddof=False means calculating Sample standard deviation
        not Unbiased standard deviation (ddof=True)
        """
        y_error = []
        if is_scale_nominal == False:
            for i in range(len(data.keys())):
                y_error.append(np.std(data[(data.keys())[i]], ddof=False))
            print "y_error: " + str(y_error)
            max_y_data = math.ceil(max(y_data) + max(y_error))
        else:
            max_y_data = math.ceil(max(y_data))

        left = np.array([])
        """
        left: list of x value (the number of order) for each bar
        """
        for i in range(len(data.keys())):
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

        If scale is nominal, yerr doesn't exist.
        """
        if is_scale_nominal == False:
            plt.bar(left, y_data, color="cyan", yerr=y_error, align="center", ecolor="blue", capsize=60)
        else:
            plt.bar(left, y_data, color="cyan", align="center", ecolor="blue", capsize=60)
        """
        plt.rcParams["font.size"]: modify character size in a graph
        plt.tick_params(labelsize=28): modify character size in x, ylabel
        """
        plt.rcParams["font.size"] = 16
        plt.tick_params(labelsize=12)
        """
        add y_value in each bar
        w = 0.4 (bar width from bar center line is 0.4)
        """
        ax = plt.gca()

        """
        set y range
        """
        ax.set_ylim([0.0, max_y_data + 1.0])
        for i in range(len(y_data)):
            ann = ax.annotate(str((round (y_data[i] * 100.0)) * 0.01), xy=(left[i] - 0.15, y_data[i] / 2.0), fontsize=28)
        """
        add x_value in each bar
        """
        plt.xticks(left, data.keys())
        """
        add title, label
        """
        if sample_type == "paired":
            new_title = title + "\n(N = " + str(len(data[(data.keys())[0]])) + " for each type, * p < 0.05, ** p < 0.01)"
        else:
            new_title = title + "\n(N = " + str(len(data[(data.keys())[0]]))
            for i in range(1, len(data.keys())):
                new_title += ", " + str(len(data[(data.keys())[i]])) 
            new_title += " respectively, * p < 0.05, ** p < 0.01)"
        plt.title(new_title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        if p and len(data.keys()) == 2:
            """
            add p value and mark
            """
            if p < 0.01:
                input_word = "**" + " (p = " + str(round (p * 100000.0) * 0.00001) + " )"
                plt.text(1.3, max_y_data * 0.75, input_word)
            elif p < 0.05:
                input_word = "*" + " (p = " + str(round (p * 100000.0) * 0.00001) + " )"
                plt.text(1.3, max_y_data * 0.75, input_word)
            else:
                input_word = " p = " + str(round (p * 100000.0) * 0.00001)
                plt.text(1.3, max_y_data * 0.75, input_word)
            plt.text(1.0, max_y_data * 0.65, "|--------------------------------------------|")
        
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
        if tight_layout:
            fig.tight_layout()
        """
        show graph
        """
        plt.show()
        return y_data, y_error

if __name__ == '__main__':
    pass
