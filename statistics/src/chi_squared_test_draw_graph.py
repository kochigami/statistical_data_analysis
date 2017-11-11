#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import math
import numpy as np
from chi_squared_test import ChiSquaredTest

class ChiSquaredTestDrawGraph:
    """
    title: string.
    label: string list.
    xlabel: string.
    ylabel: string.
    tight_layout: bool. if execute tight_layout, set True.
    mode: string. paried or unpaired
    p: float.
    """
    def draw_graph(self, data, label, title, xlabel, ylabel, tight_layout=False, mode="paired", p=None):
        """
        fig: make figure instance
        """
        fig = plt.figure()
        """
        y_data: calculate sample_data_average as list [ave_0, ave_1, ave_2]
        max_y_data: max y value for scale
        """
        y_data1 = np.array([(data[0][0] / float(data[0][0] + data[0][1])) * 100.0, (data[1][0] / float(data[1][0] + data[1][1])) * 100.0])
        y_data2 = np.array([(data[0][1] / float(data[0][0] + data[0][1])) * 100.0, (data[1][1] / float(data[1][0] + data[1][1])) * 100.0])
        
        max_y_data = 100

        left = np.array([])
        """
        left: list of x value (the number of order) for each bar
        """
        for i in range(len(data[0])):
            left = np.append(left, i+1)
        """
        make bar:
        left: list of x value (the number of order)
        y_data: list of y value
        (width: the width of bar, default is 0.8)
        color: bar color
        align: position to x bar (default is "edge")
        reference: http://pythondatascience.plavox.info/matplotlib/%E6%A3%92%E3%82%B0%E3%83%A9%E3%83%95
        """
        p1 = plt.bar(left, y_data1, color="cyan", align="center")
        p2 = plt.bar(left, y_data2, bottom=y_data1, color="green", align="center")
        plt.legend((p1[0], p2[0]), ("Yes", "No"))
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
        for i in range(len(y_data1)):
            # x, y, displaying y value, width position, height position (va="top": bottom of (x, y))
            plt.text(left[i] - 0.02, y_data1[i] / 2.0, str(str((round (y_data1[i] * 100.0)) * 0.01) + " ("+ str(data[0][i]) +")"), ha='center', va='top', fontsize=28)

        plt.text(left[0] - 0.02, y_data1[0] + (y_data2[0] / 2.0), str(str((round (y_data2[0] * 100.0)) * 0.01) + " ("+ str(data[1][0]) +")"), ha='center', va='top', fontsize=28)
        if y_data1[1] + y_data2[1] * 0.5 > 80.0:
            # avoid overlapping with legend
            plt.text(left[1] - 0.1, y_data1[1] + (y_data2[1] / 2.0), str(str((round (y_data2[1] * 100.0)) * 0.01) + " ("+ str(data[1][1]) +")"), ha='center', va='top', fontsize=28)
        else:
            plt.text(left[1] - 0.02, y_data1[1] + (y_data2[1] / 2.0), str(str((round (y_data2[1] * 100.0)) * 0.01) + " ("+ str(data[1][1]) +")"), ha='center', va='top', fontsize=28)
        """
        add x label in each bar
        """
        plt.xticks(left, label)
        """
        add title, label
        """
        if mode == "unpaired":
            new_title = title + "\n(N = " + str(data[0][0] + data[0][1] + data[1][0] + data[1][1]) + " for total (" + str(label[0]) + ": " +  str(data[0][0] + data[0][1]) + ", " + str(label[1]) + ": " + str(data[1][0] + data[1][1]) + "),\n * p < 0.05, ** p < 0.01)"
        elif mode == "paired":
            new_title = title + "\n(N = " + str(data[0][0] + data[0][1]) + " for each type, * p < 0.05, ** p < 0.01)"
        plt.title(new_title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        
        """
        calculate p value
        """
        chi_squared_test = ChiSquaredTest()
        p = chi_squared_test.test(data)
        
        if p:
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

if __name__ == '__main__':
    pass
