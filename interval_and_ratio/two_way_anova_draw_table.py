#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from two_way_anova import TwoWayAnova


class TwoWayAnovaDrawTable:
    '''
    draw_table: function for draw Analysis variance of table by matplotlib.
    data_list:
    mode: string. CRFpq, SPFpq, RBFpq. choose one based on your test.
    '''
    def draw_table(self, data_list, label_1, label_2, mode="CRFpq"):
        # set column
        columns = ("Sum of Squares", "Dof", "Mean Square", "F", "P") 
        # set row based on your test type
        if mode == "CRFpq":
            rows = ["Factor1", "Factor2", "Factor1 x Factor2", "Others", "Total"]
        elif mode == "SPFpq":
            rows = ["Factor1", "Subject(Factor1)", "Factor2", "Factor1 x Factor2", "Factor2 x Subject(Factor1)", "Total"]
        elif mode == "RBFpq":
            rows = ["Subject", "Factor1", "Factor1 x Subject", "Factor2", "Factor2 x Subject", "Factor1 x Factor2", "Factor1 x Factor2 x Subject", "Total"]
        else:
            print "Please choose mode."
            return False

        # initialization for draw table
        fig, ax = plt.subplots()

        # FIXME: calculate anova
        two_way_anova_class = TwoWayAnova()
        if mode == "CRFpq":
            data_list = two_way_anova_class.two_way_anova(data_list, label_1, label_2, mode="CRFpq")
        elif mode == "SPFpq":
            data_list = two_way_anova_class.two_way_anova(data_list, label_1, label_2, mode="SPFpq")
        elif mode == "RBFpq":
            data_list = two_way_anova_class.two_way_anova(data_list, label_1, label_2, mode="RBFpq")

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
    pass
