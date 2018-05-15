#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

class DrawBoxGraph:
    def draw_graph(self, data, title, xlabel, ylabel):
        # # 数学の点数
        # math = [74, 65, 40, 62, 85, 67, 82, 71, 60, 99]
        # # 国語の点数
        # literature = [81, 62, 32, 67, 41, 50, 85, 70, 67, 97]
        # # 点数のタプル
        # data = (math, literature)

        # 箱ひげ図
        fig, ax = plt.subplots()
        
        tmp_data = []
        for i in data.values():
            tmp_data.append(i)
            
        bp = ax.boxplot(tmp_data)
        
        tmp_label = []
        for i in data.keys():
            tmp_label.append(i)
        ax.set_xticklabels(tmp_label)

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        # Y軸のメモリのrange
        tmp_max = tmp_data[0][0]
        for i in range(len(tmp_data)):
            for j in range(len(tmp_data[i])):
                if tmp_max < tmp_data[i][j]:
                    tmp_max = tmp_data[i][j]

        plt.ylim([0,tmp_max*1.1])
        plt.grid()
        
        # 描画
        plt.show()

if __name__ == '__main__':
    pass
