#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Utils():

    def condition_type_num(self, condition):
        return len(condition)
    
    def ABS(self, data):
        ABS = 0.0
        for i in data.keys():
            for j in range(len(data[i])):
                ABS += pow((data[i])[j], 2.0)
        return ABS
        
    def AB(self, data):
        AB = 0.0
        for i in data.keys():
            AB += pow(sum(data[i]), 2.0) / len(data[i])
        return AB

    def G(self, data):
        G = 0.0
        for i in range(len(data.keys())):
            G += sum(data[(data.keys())[i]])
        return G
        
    def WC_dof(self, p, q, n):
        return p * q * (n - 1.0)

    def X(self, G, p, q, n):
        return  pow(G, 2.0) / (n * p * q)

    def condition_sum(self, data, label):
        condition_sum = []
        condition_sum_tmp = 0.0
        for i in range(len(label)):
            for j in range(len(data.keys())):
                if label[i] in (data.keys())[j]:
                    condition_sum_tmp += sum(data[(data.keys())[j]])
            condition_sum.append(condition_sum_tmp)
            condition_sum_tmp = 0.0
        return condition_sum

    def condition_num(self, data, label):
        num_list = []
        for j in range(len(label)):
            for i in range(len(data.keys())):
                if label[j] in (data.keys())[i]:
                    num_list.append(len(data[(data.keys())[i]]))
                    break
        return num_list

    # used when num of sample data per condition is different
    def condition_sum_of_unweighted_mean(self, data, label, unweighted_mean):
            condition_sum_tmp = 0.0
            condition_num_tmp = 0.0
            condition_sum = []
            for j in range(len(label)):
                for i in range(len(data.keys())):
                    if label[j] in (data.keys())[i]:
                        condition_sum_tmp += unweighted_mean[i]
                        condition_num_tmp += 1.0
                condition_sum_tmp = condition_sum_tmp / condition_num_tmp
                condition_sum.append(condition_sum_tmp)
                condition_sum_tmp = 0.0
                condition_num_tmp = 0.0
            return condition_sum

    def Sij(self, data, num_list, label):
        Sij = []
        tmp = [[] for i in range(len(num_list))]
        for i in range(len(label)):
            tmp[i] = [0 for s in range(num_list[i])]
            # tmp = [[0 0 0 0 0], [0 0 0 0]] 
            for j in range(num_list[i]):
                for k in range(len(data.keys())):
                    if label[i] in (data.keys())[k]:
                        tmp[i][j] += data[(data.keys())[k]][j]
                Sij.append(tmp[i][j])
        return Sij
