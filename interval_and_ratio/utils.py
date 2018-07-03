#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Utils():
    def condition_num(self, condition):
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
            for j in range(len(data[(data.keys()[i])])):
                G += (data[(data.keys()[i])])[j]
        return G
        
    def WC_dof(self, p, q, n):
        return p * q * (n - 1.0)

    def X(self, G, p, q, n):
        return  pow(G, 2.0) / (n * p * q)

    def condition_sum(self, data, label_A):
        condition_sum = []
        condition_sum_tmp = 0.0
        for i in range(len(label_A)):
            for j in range(len(data.keys())):
                if label_A[i] in (data.keys())[j]:
                    condition_sum_tmp += sum(data[(data.keys())[j]])
            condition_sum.append(condition_sum_tmp)
            condition_sum_tmp = 0.0
        return condition_sum
