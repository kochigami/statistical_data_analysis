#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from draw_graph import DrawGraph

if __name__ == '__main__':
    args = sys.argv
    if len(args) is not 2:
        print "input which case you want to try: unpaired-ttest, paired-ttest"
    else:
        d = DrawGraph()
        if args[1] == "unpaired-ttest":
            # for welch's test
            # followed this website for sample: http://www.geisya.or.jp/~mwm48961/statistics/ttest_question2.htm
            # data = {'HamburgerA':  [15.3, 14.9, 14.5, 14.4, 14.0, 13.9, 14.1, 14.7, 15.3, 14.6],
            #         'HamburgerB' : [13.9, 14.2, 14.1, 14.3, 14.1, 13.7, 14.7, 13.9, 14.1, 13.8, 14.3]}
            
            # for student's test
            # followed this website for sample: http://kogolab.chillout.jp/elearn/hamburger/chap4/sec1.html
            data = {'HamburgerA':  [70, 75, 70, 85, 90, 70, 80, 75],
                    'HamburgerB' : [85, 80, 95, 70, 80, 75, 80, 90]}
            d.draw_graph(data, "test", "x", "y", tight_layout=True, mode="unpaired-ttest")

        elif args[1] == "paired-ttest":
            # # followed this website for sample: http://kogolab.chillout.jp/elearn/hamburger/chap5/sec1.html
            # data = {'HamburgerA':  [90, 75, 75, 75, 80, 65, 75, 80],
            #         'HamburgerB' : [95, 80, 80, 80, 75, 75, 80, 85]}

            # # children
            data = {'Talking to the robot': [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                    'Touching the robot':   [0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]}
            d.draw_graph(data, "The number of children \nwho spontaneously interacted with the robot", "Action Type", "Number", tight_layout=True)

            # adult
            # data = {'Talking to the robot': [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0],
            #         'Touching the robot':   [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0]}
            # d.draw_graph(data, "The number of adults \nwho spontaneously interacted with the robot", "Action Type", "Number", tight_layout=True)
