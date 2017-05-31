#!/usr/bin/env python
# -*- coding: utf-8 -*-
from texttable import Texttable
import pandas.tools.plotting as plotting
import matplotlib.pyplot as plt

class AnalysisOfVariance:
    def calc_sample_num(self, df, label, output_list):
        for i in range(len(label)):
            output_list.append(float(len(df[label[i]])))
        return output_list

    def calc_sum_of_squares(self, variance, sample_num):
        return float(variance * sample_num)

    def calc_dof(self, sample_num):
        return sample_num - 1.0

    def calc_mean_square(self, sum_of_squares, dof):
        return float(sum_of_squares / dof)

    def calc_F(self, between_mean_square, within_mean_square):
        return float(between_mean_square / within_mean_square)

    def show_table(self, sum_of_squares, dof, mean_squares, F, analysis_type="one-way"):
        ### draw a table ###
        table = Texttable()
        table.set_cols_align(["c", "c", "c", "c", "c"])
        table.set_cols_valign(["m", "m", "m", "m", "m"])
        
        if analysis_type == "one-way":
            table.add_rows([ ["Factor", "Sum of Squares", "Dof", "Mean Square", "F"], 
                             ["Between Groups", str(float(sum_of_squares["Between Groups"])), str(float(dof["Between Groups"])), str(float(mean_squares["Between Groups"])), str(float(F))],
                             ["Within Groups", str(float(sum_of_squares["Within Groups"])), str(float(dof["Within Groups"])), str(float(mean_squares["Within Groups"])), ""],
                             ["Total", str(float(sum_of_squares["Total"])), str(float(dof["Total"])), "", ""]])
        else:
            table.add_rows([["Factor", "Sum of Squares", "Dof", "Mean Square", "F"], 
                            ["Factor1", str(float(sum_of_squares["Factor1"])), str(float(dof["Factor1"])), str(float(mean_squares["Factor1"])), float(F["Factor1"])],
                            ["Factor2", str(float(sum_of_squares["Factor2"])), str(float(dof["Factor2"])), str(float(mean_squares["Factor2"])), float(F["Factor2"])],
                            ["Interaction", str(float(sum_of_squares["Interaction"])), str(float(dof["Interaction"])), str(float(mean_squares["Interaction"])), float(F["Interaction"])],
                            ["Others", str(float(sum_of_squares["Others"])), str(float(dof["Others"])), str(float(mean_squares["Others"])), ""],
                            ["Total", str(float(sum_of_squares["Total"])), str(float(dof["Total"])), "", ""]])
        print table.draw()

    def matplotlib_table(self, df):
        fig, ax = plt.subplots(1, 1)
        plotting.table(ax, df, loc='center')
        ax.axis('off')
        plt.show()
        
