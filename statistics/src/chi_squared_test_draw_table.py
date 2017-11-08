#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from chi_squared_test import ChiSquaredTest

# referenced the table design below
# See: http://www.f.kpu-m.ac.jp/c/kouza/joho/kiso/topics/kentei/top.html#fig
class ChiSquaredTestDrawTable:
    '''
    draw_table: function for draw Analysis variance of table by matplotlib.
    data_list:
    mode: string. between or within. choose one based on your test.
    '''
    def draw_table(self, data, condition_list, title):
        chi_squared_test = ChiSquaredTest()
        p = chi_squared_test.test(data)
        
        # set column
        columns = ("Yes", "No", "Chi-squared test") 
        # set row based on your test type
        rows = [condition_list[0], condition_list[1]]
        if p < 0.01:
            data_list = [[data[0][0], data[0][1], str("** (" + str((round(p * 100.0)) * 0.01) + ")")],
                    [data[1][0], data[1][1], "-"]]
        elif p < 0.05:
            data_list = [[data[0][0], data[0][1], str("* (" + str((round(p * 100.0)) * 0.01) + ")")],
                    [data[1][0], data[1][1], "-"]]
        else:
            data_list = [[data[0][0], data[0][1], str("n.s. (" + str((round(p * 100.0)) * 0.01) + ")")],
                    [data[1][0], data[1][1], "-"]]
        # initialization for draw table
        fig, ax = plt.subplots()

        # set information for table
        # cellText: data text inside each cell
        # cellLoc: data text location inside each cell
        # rowLabels: string list. table row label
        # colLabels: string list. table column label
        # bbox: float list. [left, bottom, width, height]. adjustment to fit table inside plot area
        # % left: right is +, left is -. bottom: up is +, down is -, width/ height: size ratio 
        # loc: table location relative to plot area
        ax.table(cellText=data_list,
                 cellLoc='center',
                 rowLabels=rows,
                 colLabels=columns,
                 bbox=[0.11, 0.0, 1.0, 0.7],
                 loc="center left")
        # set x, y axis display off 
        ax.axis("off")
        # set title
        title = title + "\n n.s.: not significant, *:p<0.05, **:p<0.01"
        plt.title(title)
        # show a table
        plt.show()

if __name__ == '__main__':
    pass
