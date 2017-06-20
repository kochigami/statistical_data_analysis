#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import DataFrame
from scipy import stats
import numpy as np
import math

class CalculateAverage:
    def __init__(self):
        self.sample_sum_of_each_category_average = []
        self.sample_num_of_each_category = []
        
    def reset_list(self):
        self.sample_sum_of_each_category_average = []
        self.sample_num_of_each_category = []

    def add_list(self, list_name, value):
        list_name.append(value)
        return list_name

    def calc_average(self, df, label):
        '''
        Calculate average of each label.
        Args: df (DataFrame): dataframe of samples.
              label (string): label of each group of samples.
        Return: average (float)
        '''
        return float(df[label].mean())

    # def calc_average_of_each_sample(self, df, label):
    #     # average: each sample #
    #     self.reset_list()
    #     for i in range(len(label)):
    #         self.add_list(self.sample_sum_of_each_category_average, df[label[i]].mean())
    #         self.add_list(self.sample_num_of_each_category, len(df[label[i]]))
    #     return self.sample_sum_of_each_category_average, self.sample_num_of_each_category

    # def calc_average_of_factor1(self, df, label, condition_number_of_factor1):
    #     # average: factor1 #
    #     self.reset_list()
    #     tmp_sum = 0.0
    #     tmp_num = 0.0
    #     tmp_sum = [0.0 for i in range(condition_number_of_factor1)]
    #     tmp_num = [0.0 for i in range(condition_number_of_factor1)]
    #     tmp_list = []
    #     tmp_list = [(df[label].values.flatten())[i:i + (len(label) / condition_number_of_factor1)] for i in range(0, len(df[label]) * len(label), (len(label) / condition_number_of_factor1))]
    #     for i in range(0, ((len(df[label]) * len(label)) / (len(label) / condition_number_of_factor1))):
    #         a, b = divmod(i, condition_number_of_factor1)
    #         tmp_sum[b] += sum(tmp_list[i])
    #         tmp_num[b] += len(tmp_list[i])
      
    #     for i in range(condition_number_of_factor1):
    #         self.add_list(self.sample_sum_of_each_category_average, tmp_sum[i] / tmp_num[i])
    #         self.add_list(self.sample_num_of_each_category, tmp_num[i])

    #     return self.sample_sum_of_each_category_average, self.sample_num_of_each_category

    # def calc_average_of_factor2(self, df, label, condition_number_of_factor1):
    #     # average: factor2 #
    #     self.reset_list()
    #     tmp_sum = 0.0
    #     tmp_num = 0.0
    #     for i in range(0, len(label), (len(label) / condition_number_of_factor1)): #2
    #         tmp_sum += df[label[i]].sum()
    #         tmp_num += len(df[label[i]])
    #     self.add_list(self.sample_sum_of_each_category_average, tmp_sum / tmp_num)
    #     self.add_list(self.sample_num_of_each_category, tmp_num)

    #     tmp_sum = 0.0
    #     tmp_num = 0.0
    #     for i in range(1, len(label), (len(label) / condition_number_of_factor1)): #2
    #         tmp_sum += df[label[i]].sum()
    #         tmp_num += len(df[label[i]])
    #     self.add_list(self.sample_sum_of_each_category_average, tmp_sum / tmp_num)
    #     self.add_list(self.sample_num_of_each_category, tmp_num)

    #     return self.sample_sum_of_each_category_average, self.sample_num_of_each_category

    # def calc_average_of_total(self, df, label):
    #     # average: total #
    #     self.reset_list()
    #     tmp_sum = 0.0
    #     tmp_num = 0.0
    #     for i in range(len(label)):
    #         tmp_sum += df[label[i]].sum()
    #         tmp_num += len(df[label[i]])
    #     self.add_list(self.sample_sum_of_each_category_average, tmp_sum / tmp_num)
    #     self.add_list(self.sample_num_of_each_category, tmp_num)

    #     return self.sample_sum_of_each_category_average, self.sample_num_of_each_category

    # def calc_average(self, df, label, condition_number_of_factor1):
    #     # average: each sample #
    #     #self.reset_list()
    #     self.sample_sum_of_each_category_average, self.sample_num_of_each_category = self.calc_average_of_each_sample(df, label)

    #     # average: factor1 #
    #     self.sample_sum_of_each_category_average, self.sample_num_of_each_category = self.calc_average_of_factor1(df, label, condition_number_of_factor1)

    #     # average: factor2 #
    #     self.sample_sum_of_each_category_average, self.sample_num_of_each_category = self.calc_average_of_factor2(df, label, condition_number_of_factor1)

    #     # average: total #
    #     self.sample_sum_of_each_category_average, self.sample_num_of_each_category = self.calc_average_of_total(df, label, condition_number_of_factor1)

    #     return self.sample_sum_of_each_category_average, self.sample_num_of_each_category
