#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import DataFrame
from scipy import stats
import numpy as np
import math

class CalculateVariance:
    def __init__(self):
        self.sample_sum_of_each_category_variance = []

    def reset_list(self):
        self.sample_sum_of_each_category_variance = []
        
    def add_list(self, list_name, value):
        list_name.append(value)
        return list_name

    def calc_variance_of_total(self, df, label):
        # variance: total #
        self.reset_list()
        self.sample_sum_of_each_category_variance = np.var(df[label].values.flatten())
        return self.sample_sum_of_each_category_variance

    def calculate_variance_of_each(self, df, label):
        # variance: total #
        for i in range(len(label)):
            self.add_list(self.sample_sum_of_each_category_variance, df[label[i]].var(ddof=False))
        return self.sample_sum_of_each_category_variance
        
    def calculate_variance_of_each_condition(self, df, label, condition_number_of_factor1):
        # variance: each condition #
        condition1 = []
        condition2 = []
        condition3 = []
        condition4 = []
        sample = len (label) / condition_number_of_factor1
        for i in range(0, sample):
            for j in range(len(df[label[i]])):
                condition1.append(df[label[i]][j])
    
        for i in range(sample, len(label)):
            for j in range(len(df[label[i]])):
                condition2.append(df[label[i]][j])

        for i in range(0, len(label), (len(label) / condition_number_of_factor1)):
            for j in range(len(df[label[i]])):
                condition3.append(df[label[i]][j])

        for i in range(1, len(label), (len(label) / condition_number_of_factor1)):
            for j in range(len(df[label[i]])):
                condition4.append(df[label[i]][j])

        self.add_list(self.sample_sum_of_each_category_variance, np.var(condition1))
        self.add_list(self.sample_sum_of_each_category_variance, np.var(condition2))
        self.add_list(self.sample_sum_of_each_category_variance, np.var(condition3))
        self.add_list(self.sample_sum_of_each_category_variance, np.var(condition4))
        self.add_list(self.sample_sum_of_each_category_variance, np.var(df[label].values.flatten()))
        
        return self.sample_sum_of_each_category_variance

    def calc_variance(self, df, label, condition_number_of_factor1):
        ### calculate total variance ###
        self.sample_sum_of_each_category_variance = self.calculate_total_variance(df, label)
    
        ### calculate variance of each condition ###
        self.sample_sum_of_each_category_variance = self.calculate_variance_of_each_condition(df, label, condition_number_of_factor1)
        
        return self.sample_sum_of_each_category_variance
