#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import math
import numpy as np
from t_test import TTEST

class DrawGraph:
    """
       if mode is paired-ttest or unpaired-ttest, data is like this.
       data = {'Crispy':  [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
               'Normal' : [70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]}
              Be sure that string list is like ([category1, category2]).

       if mode is anova, data is like this.
       data = {'Crispy-hot':  [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
               'Crispy-mild': [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
               'Normal-hot' : [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
               'Normal-mild' : [70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]}

       title: string.
       xlabel: string.
       ylabel: string.
       tight_layout: bool. if execute tight_layout, set True.
       mode: string. paired-ttest, unpaired-ttest, anova
       p: float. if mode is paired-ttest or unpaired-ttest, it is required.
    """
    def draw_graph(self, data, title, xlabel, ylabel, tight_layout=False, mode="paired-ttest", p=None):
        """
        fig: make figure instance
        """
        fig = plt.figure()
        """
        y_data: calculate sample_data_average as list [ave_0, ave_1, ave_2]
        max_y_data: max y value for scale
        """
        y_data = []
        tmp=0
        for i in range(len(data.keys())):
            tmp=0
            for j in range(len(data[(data.keys())[i]])):
                print "test: "
                print data[(data.keys())[i]][j]
                #print data[((data.keys())[i])[j]]
                if data[(data.keys())[i]][j] == 1:
                    tmp += 1
            print tmp
            y_data.append(tmp)
            #y_data.append(np.mean(data[(data.keys())[i]]))
        tmp_list = []    
        for i in range(len(data.keys())):
            tmp_list.append(len((data.keys())[i]))
        #max_y_data = math.ceil(max(len(data.keys())))
        max_y_data = math.ceil(max(tmp_list))
        """
        y_error: calculate sample_error as list [err_0, err_1]
        left: list of x value for each bar, now it is just empty
        ddof=False means calculating Sample standard deviation
        not Unbiased standard deviation (ddof=True)
        """
        y_error = []
        for i in range(len(data.keys())):
            #y_error.append(np.std(data[(data.keys())[i]], ddof=False))
            y_error.append((len((data.keys())[i]) * np.std(data[(data.keys())[i]], ddof=False)))
        print "y_error: "
        print y_error
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
        """
        plt.bar(left, y_data, color="cyan", yerr=y_error, align="center", ecolor="blue", capsize=60)
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
        for i in range(len(y_data)):
            ann = ax.annotate(str((round (y_data[i] * 100.0)) * 0.01), xy=(left[i] - 0.15, y_data[i] / 2.0), fontsize=28)
        """
        add x_value in each bar
        """
        plt.xticks(left, data.keys())
        """
        add title, label
        """
        if mode == "anova":
            new_title = title + "\n(N = " + str(len(data[(data.keys())[0]])) + " for each type)"
        elif mode == "paired-ttest":
            new_title = title + "\n(N = " + str(len(data[(data.keys())[0]])) + " for each type, * p < 0.1, ** p < 0.05)"
        elif mode == "unpaired-ttest":
            new_title = title + "\n(N = " + str(len(data[(data.keys())[0]]) + len(data[(data.keys())[1]]))  + " for total (" + str((data.keys())[0]) + ": " +  str(len(data[(data.keys())[0]])) + ", " + str((data.keys())[1]) + ": " + str(len(data[(data.keys())[1]])) + "),\n * p < 0.1, ** p < 0.05)"
        plt.title(new_title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        
        if (mode == "paired-ttest" or mode == "unpaired-ttest") and p is None:
            t_test = TTEST()
            if mode == "paired-ttest":
                p = t_test.paired_ttest(data)
            else:
                p = t_test.unpaired_ttest(data)
        if p:
            """
            add p value and mark
            """
            if p < 0.05:
                #input_word = "**" + " (p = " + str(round (p * 1000.0) * 0.001) + " )"
                print p
                input_word = "**" + " (p = " + str(round (p * 100000.0) * 0.00001) + " )"
                plt.text(1.3, max_y_data * 0.75, input_word)
            elif p < 0.1:
                input_word = "*" + " (p = " + str(round (p * 1000.0) * 0.001) + " )"
                plt.text(1.3, max_y_data * 0.75, input_word)
            else:
                input_word = " p = " + str(round (p * 1000.0) * 0.001)
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

if __name__ == '__main__':
    pass
