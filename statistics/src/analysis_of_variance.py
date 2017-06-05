#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import DataFrame
import numpy as np
from texttable import Texttable
import pandas.tools.plotting as plotting
import matplotlib.pyplot as plt

class AnalysisOfVariance:
    def create_df(self, data, keyword=None):
        """
        data: dictionary of each data
        keyword
        """
        connected_data = []
        if keyword is None: 
            keyword = "each"
            return DataFrame(data, index = [str(i+1)  for i  in np.arange(len(data.values()[0]))])

        elif keyword == "all" or keyword == "All":
            for i in range(len(data.keys())):
                connected_data += data[data.keys()[i]]
        else:
            for i in range(len(data.keys())):
                if keyword in data.keys()[i]:
                    connected_data += data[data.keys()[i]]
        new_dict = {keyword: connected_data}
        return DataFrame(new_dict, index = [str(i+1)  for i  in np.arange(len(new_dict.values()[0]))])

    def create_label(self, df):
        label = []
        for i in range(len(df.keys())):
            label.append(df.keys()[i])
        return label

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

    def make_df_of_one_way_anova_for_matplotlib_table(self, between_sum_of_squares, within_sum_of_squares, between_dof, within_dof, between_mean_square, within_mean_square, F):
        show_table_df = DataFrame (index=list("123"), columns=[])
        show_table_df['Sum of Squares'] = [float(between_sum_of_squares), float(within_sum_of_squares), float(within_sum_of_squares) + float(between_sum_of_squares)]
        show_table_df['DOF'] = [float(between_dof), float(within_dof), float(within_dof) + float(between_dof)]
        show_table_df['Mean Square'] = [float(between_mean_square), float(within_mean_square), ""]
        show_table_df['F'] = [float(F), "", ""]
        show_table_df.index = ['Between', 'Within', 'Total']
        return show_table_df
        
    def make_df_of_two_way_anova_for_matplotlib_table(self, sum_of_squares_of_factor1, sum_of_squares_of_factor2, sum_of_squares_of_interaction, sum_of_squares_of_others, dof_of_factor1, dof_of_factor2, dof_of_interaction, dof_of_others, dof_of_all, mean_square_of_factor1, mean_square_of_factor2, mean_square_of_interaction, mean_square_of_others, F_of_factor1, F_of_factor2, F_of_interaction):
        show_table_df = DataFrame (index=list("12345"), columns=[])
        show_table_df['Sum of Squares'] = [sum_of_squares_of_factor1, sum_of_squares_of_factor2, sum_of_squares_of_interaction, sum_of_squares_of_others, sum_of_squares_of_factor1 + sum_of_squares_of_factor2 + sum_of_squares_of_interaction + sum_of_squares_of_others]
        show_table_df['DOF'] = [dof_of_factor1, dof_of_factor2, dof_of_interaction, dof_of_others, dof_of_all]
        show_table_df['Mean Square'] = [mean_square_of_factor1, mean_square_of_factor2, mean_square_of_interaction, mean_square_of_others, ""]
        show_table_df['F'] = [F_of_factor1, F_of_factor2, F_of_interaction, "", ""]
        show_table_df.index = ['Factor1', 'Factor2', 'Interaction', 'Others', 'Total']
        return show_table_df

    def matplotlib_table(self, df):
        fig, ax = plt.subplots(1, 1)
        plotting.table(ax, df, loc='center')
        ax.axis('off')
        plt.show()
