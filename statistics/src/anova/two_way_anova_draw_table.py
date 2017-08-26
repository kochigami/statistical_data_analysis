#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
import matplotlib.pyplot as plt
from two_way_anova import TwoWayAnova


class DrawTable:
    '''
    draw_table: function for draw Analysis variance of table by matplotlib.
    data_list:
    mode: string. between or within. choose one based on your test.
    '''
    def draw_table(self, data_list, label_1, label_2, mode="between"):
        # set column
        columns = ("Sum of Squares", "Dof", "Mean Square", "F") 
        # set row based on your test type
        if mode == "between":
            rows = ["Factor1", "Factor2", "Interaction", "Others", "Total"]
        elif mode == "within":
            rows = ["Subject", "Factor1", "Subject x Factor1", "Factor2", "Subject x Factor2", "Interaction", "Subject x Interaction", "Total"]
        else:
            print "Please choose mode 'between' or 'within'."
            return False

        # initialization for draw table
        fig, ax = plt.subplots()

        # FIXME: calculate anova
        two_way_anova_class = TwoWayAnova()
        if mode == "between":
            data_list = two_way_anova_class.two_way_anova(data_list, label_1, label_2)
        elif mode == "within":
            data_list = two_way_anova_class.two_way_anova(data_list, label_1, label_2, mode="within")

        # set information for table
        # cellText: data text inside each cell
        # cellLoc: data text location inside each cell
        # rowLabels: string list. table row label
        # colLabels: string list. table column label
        # bbox: float list. [left, bottom, width, height]. adjustment to fit table inside plot area
        # % left: right is +, left is -. bottom: up is +, down is -, width/ height: size ratio 
        # loc: table location relative to plot area
        table = ax.table(cellText=data_list,
                         cellLoc='center',
                         rowLabels=rows,
                         colLabels=columns,
                         bbox=[0.11, 0.0, 1.0, 0.7],
                         loc="center left")
        # set x, y axis display off 
        ax.axis("off")
        # show a table
        plt.show()

if __name__ == '__main__':
    draw_table = DrawTable()
    args = sys.argv
    if len(args) is not 2:
        print "input which case you want to try: between, within"

    else:
        # followed this website for sample: http://kogolab.chillout.jp/elearn/hamburger/chap7/sec2.html
        if args[1] == "between":
            data = {'NAO-Adult':       [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
                    'NAO-Children':    [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
                    'Pepper-Adult':    [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
                    'Pepper-Children': [70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]}
            label_a = ["NAO", "Pepper"]
            label_b = ["Adult", "Children"]

            draw_table.draw_table(data, label_a, label_b, mode="between")
        
        elif args[1] == "within":
            # followed this website for sample: http://mcn-www.jwu.ac.jp/~kuto/kogo_lab/psi-home/stat2000/DATA/08/START.HTM
            data = {'Box-Tsukurioki':  [65, 75, 70, 75, 90, 80, 65, 50, 55, 80, 90, 70, 75, 80, 75],
                    'Box-Order': [70, 80, 75, 75, 95, 80, 75, 55, 50, 85, 80, 70, 75, 80, 60],
                    'Paper-Tsukurioki' : [50, 55, 70, 75, 80, 85, 65, 55, 55, 75, 80, 75, 70, 65, 55],
                    'Paper-Order' : [60, 65, 75, 80, 90, 80, 80, 55, 60, 82, 80, 70, 90, 70, 60]}
            label_a = ["Box", "Paper"]
            label_b = ["Tsukurioki", "Order"]

            draw_table.draw_table(data, label_a, label_b, mode="within")

        else:
            print "please input between or within"
