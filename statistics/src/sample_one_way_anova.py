#!/usr/bin/env python
# -*- coding: utf-8 -*-
from one_way_anova_draw_table import DrawTable

if __name__ == '__main__':
    draw_table = DrawTable()
    # followed this website for sample: http://kogolab.chillout.jp/elearn/hamburger/chap6/sec0.html
    data = {'HamburgerA':  [80, 75, 80, 90, 95, 80, 80, 85, 85, 80, 90, 80, 75, 90, 85, 85, 90, 90, 85, 80],
            'HamburgerB':  [75, 70, 80, 85, 90, 75, 85, 80, 80, 75, 80, 75, 70, 85, 80, 75, 80, 80, 90, 80],
            'HamburgerC' : [80, 80, 80, 90, 95, 85, 95, 90, 85, 90, 95, 85, 98, 95, 85, 85, 90, 90, 85, 85]}    
    draw_table.draw_table(data)
