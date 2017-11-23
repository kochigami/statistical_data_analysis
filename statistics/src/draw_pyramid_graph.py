#!/usr/bin/env python
# -*- coding: utf-8 -*-
# reference this link: http://coreblog.org/ats/stuff/minpy_support/samplecodes04/samplecodes/Chapter12/12-04.html
import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np

class DrawPyramidGraph:
    def draw_graph(self, year, arr1, arr2, ymin, ymax, ydim=1):
        # 人口ピラミッドを表示する
        # 表示する人口のインデックスを得る ターゲットの行
        idx = int((year - ymin) / ydim)
        # 人口ピラミッドのグリッドを生成
        gs = gridspec.GridSpec(1, 2)
        # グラフの配置を決める
        ax = [plt.subplot(gs[0, 0]), plt.subplot(gs[0, 1])]
        # 男性の人口ピラミッドを描く
        # https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.barh
        # print arr1[idx]
        # [ 5719.  4826.  4401.  4318.  3836.  2822.  2360.  2376.  2199.  2019.
        #   1719.  1379.  1110.   796.   540.   268.    96.    29.     0.     0.
        #   0.]
        # print range(0, 101, 5)
        # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
        ax[0].barh(range(0, 101, 5), arr1[idx], height=3, label="male", color="b")
        ax[0].set(ylim=(0, 100), xlim=(0, 6000))
        ax[0].invert_xaxis()
        ax[0].yaxis.tick_right()
        # 女性の人口ピラミッドを描く
        ax[1].barh(range(0, 101, 5), arr2[idx], height=3, label="female", color="g")
        ax[1].tick_params(labelleft='off')
        ax[1].set(ylim=(0, 100), xlim=(0, 6000))

        # TODO:凡例を表示
        # TODO: title

        plt.show()
        

if __name__ == '__main__':
    draw_graph = DrawPyramidGraph()
    # 1944年から2014年までの5歳階級別の人口を男女別に読み込む
    # use 1-22 (,0 – 4, 5 – 9, 10 – 14, 15 – 19, 20 – 24, 25 – 29, 30 – 34, 35 – 39, 40 – 44, 45 – 49, 50 – 54, 55 – 59, 60 – 64, 65 – 69, 70 – 74, 75 – 79, 80 – 84, 85 – 89, 90 – 94, 95 – 99, 100-,) 
    # and skip first line (line1: just show ,0 – 4, 5 – 9, 10 – 14, ...) 
    p_male = np.loadtxt('male_1944_2014.csv', delimiter=",",
                        skiprows=1, usecols=range(1, 22))
    p_female = np.loadtxt('female_1944_2014.csv', delimiter=",",
                          skiprows=1, usecols=range(1, 22))

    # 関数を呼び出して人口ピラミッドを描く
    draw_graph.draw_graph(1950, p_male, p_female, 1944, 2014)
