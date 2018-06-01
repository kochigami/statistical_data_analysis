#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

class DrawBoxGraph:
    def draw_graph(self, data, title, xlabel, ylabel):
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

        '''
        plot number of sample for each condition as text
        '''
        # calculate medians for getting y position
        medians = []
        for i in range(len(tmp_data)):
            medians.append(np.median(tmp_data[i]))
        # set plotting text (number of sample for each condition)
        nobs = []
        for i in range(len(tmp_data)):
            nobs.append(len(tmp_data[i]))
        nobs = ["n: " + str(i) for i in nobs]
        # plot nobs (x position is 1, 2, 3,...)
        pos = range(len(nobs))
        for tick in pos:
            # x position of the text, y position of the text, text, other options
            plt.text(pos[tick]+1, medians[tick] * 1.01, nobs[tick], horizontalalignment='center', size='medium', color='black', weight='semibold')

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
