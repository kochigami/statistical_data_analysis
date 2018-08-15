#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

class DrawBoxGraph:
    def draw_graph(self, data, title, xlabel, ylabel, text=True):
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

        # print SD
        for i in range(len(tmp_data)):
            print "std {}: {}".format(tmp_label[i], np.std(tmp_data[i]))

        if text:
            '''
            plot number of sample for each condition as text
            '''
            # calculate medians for getting y position
            nobs = []
            medians = []
            scoreatpercentile_25 = []
            scoreatpercentile_75 = []
            min_data = []
            max_data = []
            for i in range(len(tmp_data)):
                nobs.append(len(tmp_data[i]))
                medians.append(np.median(tmp_data[i]))
                scoreatpercentile_25.append(stats.scoreatpercentile(tmp_data[i], 25))
                scoreatpercentile_75.append(stats.scoreatpercentile(tmp_data[i], 75))
                min_data.append(min(tmp_data[i]))
                max_data.append(max(tmp_data[i]))

            # plot text (x position is 1, 2, 3,...)
            for tick in range(len(nobs)):
                # x position of the text, y position of the text, text, other options
                plt.text(tick+1, medians[tick] * 1.02, "median: " + str(round(medians[tick], 2)), horizontalalignment='center', size='small', color='black', weight='semibold') # (median = scoreatpercentile_50)
                plt.text(tick+1, scoreatpercentile_25[tick] * 1.02, "1st quartiles: " + str(round(scoreatpercentile_25[tick], 2)), horizontalalignment='center', size='small', color='black', weight='semibold')
                plt.text(tick+1, scoreatpercentile_75[tick] * 1.02, "3rd quartiles: " + str(round(scoreatpercentile_75[tick], 2)), horizontalalignment='center', size='small', color='black', weight='semibold')
                plt.text(tick+1, min_data[tick] * 1.02, "min: " + str(round(min_data[tick], 2)), horizontalalignment='center', size='small', color='black', weight='semibold')
                plt.text(tick+1, max_data[tick] * 1.02, "max: " + str(round(max_data[tick], 2)), horizontalalignment='center', size='small', color='black', weight='semibold')
                plt.text(tick+1, max_data[tick] * 1.07, "n: " + str(nobs[tick]), horizontalalignment='center', size='small', color='black', weight='semibold')

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        # Y軸の目盛りのrange
        tmp_max = tmp_data[0][0]
        for i in range(len(tmp_data)):
            if tmp_max < max(tmp_data[i]):
                    tmp_max = max(tmp_data[i])
        plt.ylim([0,tmp_max*1.1])
        plt.grid()
        
        # 描画
        plt.show()

if __name__ == '__main__':
    pass
