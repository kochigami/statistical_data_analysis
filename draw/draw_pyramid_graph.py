#!/usr/bin/env python
# -*- coding: utf-8 -*-
# reference this link: http://coreblog.org/ats/stuff/minpy_support/samplecodes04/samplecodes/Chapter12/12-04.html
import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np

class DrawPyramidGraph:
    def draw_graph(self, arr1, arr2, x_max, title="test"):
        # ピラミッドのグリッドを生成
        gs = gridspec.GridSpec(1, 2)
        # グラフの配置を決める
        ax = [plt.subplot(gs[0, 0]), plt.subplot(gs[0, 1])]
        
        if x_max % 2 == 1:
            x_max += 1
        
        # hypothesis: age range is 0-9, 10-19, 20-29, 30-39, 40-49, 50-59, 60-
        y_ticks=[5, 15, 25, 35, 45, 55, 65]
        # reference: https://stackoverflow.com/questions/19626530/python-xticks-in-subplots
        plt.setp(ax, yticks=y_ticks, yticklabels=["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-"], xticks=range(0, x_max, 2))
        # https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.barh
        ax[0].barh(y_ticks, arr1, height=3, label="male", color="b")
        
        # memo:
        #ax[0].set_yticks(y_ticks)
        #ax[0].set_yticklabels(y_ticks, ["0-9","10-19","20-29", "30-39", "40-49", "50-59", "60-"])
        #ax[1].set_yticks(y_ticks)
        #ax[1].set_yticklabels(y_ticks, ["0-9","10-19","20-29", "30-39", "40-49", "50-59", "60-"])
        # displays just "5,15,25,35,45,55,65" for y axis

        ax[0].set(ylim=(0, 70), xlim=(0, x_max))
        ax[0].invert_xaxis()
        ax[0].yaxis.tick_right()

        ax[1].barh(y_ticks, arr2, height=3, label="female", color="g")
        ax[1].tick_params(labelleft='off')
        ax[1].set(ylim=(0, 70), xlim=(0, x_max))

        # TODO:凡例を表示
        plt.suptitle(title)
        plt.show()
        

if __name__ == '__main__':
    draw_graph = DrawPyramidGraph()
    p_male = np.loadtxt('openlab2017_s_male.csv', delimiter=",",
                        skiprows=1, usecols=range(0, 7))
    p_female = np.loadtxt('openlab2017_s_female.csv', delimiter=",",
                          skiprows=1, usecols=range(0, 7))

    draw_graph.draw_graph(p_male, p_female, 12)
