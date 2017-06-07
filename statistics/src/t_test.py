#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import DataFrame
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import math

class TTEST:
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
        df = DataFrame(data, index = ["sample" + str(i+1)  for i  in np.arange(len(data.values()[0]))])
        fig = plt.figure()
    
        # calculate t & p value
        t, p = stats.ttest_rel(df[label[0]], df[label[1]])
        print( "p値 = %(p)s" %locals() )
        
        # calculate sample_data_average [ave_x, ave_y]
        y_data = [ df[label[0]].mean(), df[label[1]].mean()]
        max_y_data = math.ceil(max(y_data))
   
        # calculate sample_error [err_x, err_y]
        y_error = [ df[label[0]].std(ddof=False), df[label[1]].std(ddof=False)]

        left = np.array([])
    
        for i in range(len(label)):
            left = np.append(left, i+1)
        plt.bar(left, y_data, color="#FF5B70", yerr=y_error, align="center", ecolor="blue", capsize=60)
        plt.rcParams["font.size"] = 28
        plt.tick_params(labelsize=28)
        ax = plt.gca()
        w = 0.4
        for j in range(len(y_data)):
            ann = ax.annotate(str((round (y_data[j] * 100.0)) * 0.01), xy=(left[j] - w * 0.5, y_data[j] / 2.0), fontsize=28)
        plt.xticks(left, label)
        new_title = title + "\n(N = " + str(len(df['Japanese'])) + ", * p < 0.1, ** p < 0.05)"
        plt.title(new_title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

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
        plt.grid(True)
        fig.tight_layout()

        plt.show()

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
        df = DataFrame(data, index = ["sample" + str(i+1)  for i  in np.arange(len(data.values()[0]))])
        fig = plt.figure()
    
        # calculate f
        if np.var(df[label[0]]) > np.var(df[label[1]]):
            f = np.var(df[label[0]]) / np.var(df[label[1]])
        else:
            f = np.var(df[label[1]]) / np.var(df[label[0]])
        dfx = len(df[label[0]]) - 1
        dfy = len(df[label[1]]) - 1
        p_value = stats.f.cdf(f, dfx, dfy)

        # calculate t & p value
        if p_value < 0.05:
            t, p = stats.ttest_ind(df[label[0]], df[label[1]], equal_var = False)
            print( "p値 = %(p)s" %locals() )
        else:
            t, p = stats.ttest_ind(df[label[0]], df[label[1]], equal_var = True)
            print( "p値 = %(p)s" %locals() )

        # calculate sample_data_average [ave_x, ave_y]
        y_data = [ df[label[0]].mean(), df[label[1]].mean()]
        max_y_data = math.ceil(max(y_data))
   
        # calculate sample_error [err_x, err_y]
        y_error = [ df[label[0]].std(ddof=False), df[label[1]].std(ddof=False)]

        left = np.array([])
    
        for i in range(len(label)):
            left = np.append(left, i+1)
        plt.bar(left, y_data, color="#FF5B70", yerr=y_error, align="center", ecolor="blue", capsize=60)
        plt.rcParams["font.size"] = 28
        plt.tick_params(labelsize=28)
        ax = plt.gca()
        w = 0.4
        for j in range(len(y_data)):
            ann = ax.annotate(str((round (y_data[j] * 100.0)) * 0.01), xy=(left[j] - w * 0.5, y_data[j] / 2.0), fontsize=28)
        plt.xticks(left, label)
        new_title = title + "\n(N = " + str(len(df['Japanese'])) + ", * p < 0.1, ** p < 0.05)"
        plt.title(new_title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

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
        plt.grid(True)
        fig.tight_layout()

        plt.show()
