#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import math

class OneWayAnova:
    '''
    data = {'Japanese': [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
            'English':  [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
            'French' :  [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75]}
    mode: string. between or within.
    '''
    def one_way_anova(self, data, mode="between"):
        if mode == "between":
            # calculate total average
            total_average = 0.0
            total_sample_num = 0.0
            for i in range(len(data.keys())):
                total_sample_num += len(data[(data.keys())[i]])
                for j in range(len(data[(data.keys())[i]])):
                    total_average += (data[(data.keys())[i]])[j]
            total_average = total_average / total_sample_num

            # calculate average per category
            average_per_group = []
            for i in range(len(data.keys())):
                average_per_group.append(np.mean(data[(data.keys())[i]]))

            # calculate sum of squares
            ss_total = 0.0
            for i in range(len(data.keys())):
                for j in range(len(data[(data.keys())[i]])):
                    ss_total += pow(((data[(data.keys())[i]])[j] - total_average), 2.0)

            ss_between = 0.0
            for i in range(len(data.keys())):
                ss_between += pow((average_per_group[i] - total_average), 2.0) * len(data[(data.keys())[i]])

            ss_within = ss_total - ss_between

            # calculate dof (group type & sample number of each type)
            between_dof = len(data.keys()) - 1
            total_dof = total_sample_num - 1
            within_dof = total_dof - between_dof

            # calculate mean square
            mean_square_between = ss_between / float(between_dof)
            mean_square_within = ss_within / float(within_dof)

            # calculate F
            F = mean_square_between / mean_square_within

            #answer_list = [[0 for col in range(4)] for row in range(3)]
            answer_list = [[math.ceil(ss_between * 100.0) * 0.01, int(between_dof), math.ceil(mean_square_between * 100.0) * 0.01, math.ceil(F * 100.0) * 0.01],
                           [math.ceil(ss_within * 100.0) * 0.01, int(within_dof), math.ceil(mean_square_within * 100.0) * 0.01, '--'], 
                           [math.ceil((ss_between + ss_within) * 100.0) * 0.01, int(between_dof + within_dof),'--', '--']]
            return answer_list

        # elif mode == "within":
        #     # preparation
        #     ss_total_data = 0.0
        #      for i in range(len(label_of_each_group)):
        #          for j in range(len(df_of_each_group[label_of_each_group[0]])):
        #              ss_total_data += pow((df_of_each_group[label_of_each_group[i]])[j], 2.0)

        #     ss_between_data = 0.0
        #     for i in range(len(label_of_each_group)):
        #         ss_between_data += pow(df_of_each_group[label_of_each_group[i]].sum(), 2.0) / len(df_of_each_group[label_of_each_group[i]])

        #     ss_subject_data = 0.0
        #     for i in range(len(df_of_each_group[label_of_each_group[0]])):
        #         tmp = 0.0
        #         for j in range(len(label_of_each_group)):
        #             tmp += df_of_each_group[label_of_each_group[j]][i]
        #         ss_subject_data += pow(tmp, 2.0) / len(label_of_each_group)

        #     # calculate X (correction term)
        #     x = pow(df_of_all_samples[label_of_all_samples].sum(), 2.0) / (len(label_of_each_group) * len(df_of_each_group[label_of_each_group[0]]))

        #     # calculate sum of squares
        #     ss_total = ss_total_data - x
        #     ss_between = ss_between_data - x
        #     ss_subject = ss_subject_data - x
        #     ss_error = ss_total - ss_between - ss_subject

        #     # calculate dof (group type & sample number of each type)
        #     between_dof = self.analysis_of_variance.calc_dof(len(label_of_each_group))
        #     subject_dof = self.analysis_of_variance.calc_dof(len(df_of_each_group[label_of_each_group[0]]))
        #     error_dof = len(df_of_all_samples[label_of_all_samples]) - 1 - between_dof - subject_dof

        #     # calculate mean square
        #     between_mean_square = self.analysis_of_variance.calc_mean_square(ss_between, between_dof)
        #     subject_mean_square = self.analysis_of_variance.calc_mean_square(ss_subject, subject_dof)
        #     error_mean_square = self.analysis_of_variance.calc_mean_square(ss_error, error_dof)

        #     # calculate F
        #     F = self.analysis_of_variance.calc_F(between_mean_square, error_mean_square)

        #     # preparation for table
        #     sum_of_squares = {"Between Groups": ss_between,
        #                       "Subject": ss_subject,
        #                       "Error": ss_error,
        #                       "Total": ss_total}

        #     dof = {"Between Groups": between_dof,
        #            "Subject": subject_dof,
        #            "Error": error_dof,
        #            "Total": between_dof + subject_dof + error_dof}

        #     mean_squares = {"Between Groups": between_mean_square,
        #                     "Subject": subject_mean_square,
        #                     "Error": error_mean_square}

        #     # show table
        #     self.analysis_of_variance.show_table(sum_of_squares, dof, mean_squares, F, analysis_type="one-way-within")

        #     show_table_df = self.analysis_of_variance.make_df_of_one_way_anova_for_matplotlib_table("within", F, ss_between, between_dof, between_mean_square, ss_subject, subject_dof, subject_mean_square, ss_error, error_dof, error_mean_square)
        #     self.analysis_of_variance.matplotlib_table(show_table_df)

if __name__ == '__main__':
    pass
