#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import DataFrame
import numpy as np
from analysis_of_variance import AnalysisOfVariance

import sys
import os
sys.path.append( os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/basic')
from calculate_average import CalculateAverage
from calculate_variance import CalculateVariance

class OneWayAnova:
    def __init__(self):
        self.calculate_average = CalculateAverage()
        self.calculate_variance = CalculateVariance()
        self.analysis_of_variance = AnalysisOfVariance()

    def calc_one_way_anova(self, df_of_each_group, label_of_each_group, df_of_all_samples, label_of_all_samples, test_mode="between"):
        if test_mode == "between":
            # calculate average of whole samples
            average_of_all = self.calculate_average.calc_average(df_of_all_samples, label_of_all_samples)

            # calculate average of each group
            within_average = []
            for i in range(len(label_of_each_group)):
                within_average.append(self.calculate_average.calc_average(df_of_each_group, label_of_each_group[i]))

            # calculate sum of squares
            ss_total = 0.0
            for i in range(len(label_of_each_group)):
                for j in range(len(df_of_each_group[label_of_each_group[0]])):
                    ss_total += pow((df_of_each_group[label_of_each_group[i]])[j] - average_of_all, 2.0)

            ss_between = 0.0
            for i in range(len(label_of_each_group)):
                ss_between += pow(within_average[i] - average_of_all, 2.0) * len(df_of_each_group[label_of_each_group[i]])

            ss_within = ss_total - ss_between

            # calculate dof (group type & sample number of each type)
            between_dof = self.analysis_of_variance.calc_dof(len(label_of_each_group))
            within_dof = 0.0
            for i in range(len(label_of_each_group)):
                within_dof += self.analysis_of_variance.calc_dof(len(df_of_each_group[label_of_each_group[i]]))

            # calculate mean square
            between_mean_square = self.analysis_of_variance.calc_mean_square(ss_between, between_dof)
            within_mean_square = self.analysis_of_variance.calc_mean_square(ss_within, (len(label_of_each_group) * within_dof))

            # calculate F
            F = self.analysis_of_variance.calc_F(between_mean_square, within_mean_square)

            # table
            sum_of_squares = {"Within Groups": ss_within,
                              "Between Groups": ss_between,
                              "Total": ss_total}

            dof = {"Within Groups": within_dof,
                   "Between Groups": between_dof,
                   "Total": within_dof + between_dof}

            mean_squares = {"Within Groups": within_mean_square,
                            "Between Groups": between_mean_square}

            self.analysis_of_variance.show_table(sum_of_squares, dof, mean_squares, F, analysis_type="one-way-between")

            # show table
            show_table_df = self.analysis_of_variance.make_df_of_one_way_anova_for_matplotlib_table("between", F, ss_between, between_dof, between_mean_square, ss_within,  within_dof,  within_mean_square)
            self.analysis_of_variance.matplotlib_table(show_table_df)

        elif test_mode == "within":
            # preparation
            ss_total_data = 0.0
            for i in range(len(label_of_each_group)):
                for j in range(len(df_of_each_group[label_of_each_group[0]])):
                    ss_total_data += pow((df_of_each_group[label_of_each_group[i]])[j], 2.0)

            ss_between_data = 0.0
            for i in range(len(label_of_each_group)):
                ss_between_data += pow(df_of_each_group[label_of_each_group[i]].sum(), 2.0) / len(df_of_each_group[label_of_each_group[i]])

            ss_subject_data = 0.0
            for i in range(len(df_of_each_group[label_of_each_group[0]])):
                tmp = 0.0
                for j in range(len(label_of_each_group)):
                    tmp += df_of_each_group[label_of_each_group[j]][i]
                ss_subject_data += pow(tmp, 2.0) / len(label_of_each_group)

            # calculate X (correction term)
            x = pow(df_of_all_samples[label_of_all_samples].sum(), 2.0) / (len(label_of_each_group) * len(df_of_each_group[label_of_each_group[0]]))

            # calculate sum of squares
            ss_total = ss_total_data - x
            ss_between = ss_between_data - x
            ss_subject = ss_subject_data - x
            ss_error = ss_total - ss_between - ss_subject

            # calculate dof (group type & sample number of each type)
            between_dof = self.analysis_of_variance.calc_dof(len(label_of_each_group))
            subject_dof = self.analysis_of_variance.calc_dof(len(df_of_each_group[label_of_each_group[0]]))
            error_dof = len(df_of_all_samples[label_of_all_samples]) - 1 - between_dof - subject_dof

            # calculate mean square
            between_mean_square = self.analysis_of_variance.calc_mean_square(ss_between, between_dof)
            subject_mean_square = self.analysis_of_variance.calc_mean_square(ss_subject, subject_dof)
            error_mean_square = self.analysis_of_variance.calc_mean_square(ss_error, error_dof)

            # calculate F
            F = self.analysis_of_variance.calc_F(between_mean_square, error_mean_square)

            # preparation for table
            sum_of_squares = {"Between Groups": ss_between,
                              "Subject": ss_subject,
                              "Error": ss_error,
                              "Total": ss_total}

            dof = {"Between Groups": between_dof,
                   "Subject": subject_dof,
                   "Error": error_dof,
                   "Total": between_dof + subject_dof + error_dof}

            mean_squares = {"Between Groups": between_mean_square,
                            "Subject": subject_mean_square,
                            "Error": error_mean_square}

            # show table
            self.analysis_of_variance.show_table(sum_of_squares, dof, mean_squares, F, analysis_type="one-way-within")

            show_table_df = self.analysis_of_variance.make_df_of_one_way_anova_for_matplotlib_table("within", F, ss_between, between_dof, between_mean_square, ss_subject, subject_dof, subject_mean_square, ss_error, error_dof, error_mean_square)
            self.analysis_of_variance.matplotlib_table(show_table_df)

if __name__ == '__main__':
    pass
