#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from two_way_anova_draw_table import DrawTable

if __name__ == '__main__':
    draw_table = DrawTable()
    args = sys.argv
    if len(args) is not 2:
        print "input which case you want to try: between, within"

    else:
        # followed this website for sample: http://kogolab.chillout.jp/elearn/hamburger/chap7/sec2.html
        if args[1] == "between":
            data = {'NAO-Adult':       [65, 85, 75, 85, 75, 80, 90, 75, 85, 65, 75, 85, 80, 85, 90],
                    'NAO-Children':    [65, 70, 80, 75, 70, 60, 65, 70, 85, 60, 65, 75, 70, 80, 75],
                    'Pepper-Adult':    [70, 65, 85, 80, 75, 65, 75, 60, 85, 65, 75, 70, 65, 80, 75],
                    'Pepper-Children': [70, 70, 85, 80, 65, 75, 65, 85, 80, 60, 70, 75, 70, 80, 85]}
            label_a = ["NAO", "Pepper"]
            label_b = ["Adult", "Children"]

            draw_table.draw_table(data, label_a, label_b, mode="between")
        
        elif args[1] == "within":
            # followed this website for sample: http://mcn-www.jwu.ac.jp/~kuto/kogo_lab/psi-home/stat2000/DATA/08/START.HTM
            data = {'Box-Tsukurioki':  [65, 75, 70, 75, 90, 80, 65, 50, 55, 80, 90, 70, 75, 80, 75],
                    'Box-Order': [70, 80, 75, 75, 95, 80, 75, 55, 50, 85, 80, 70, 75, 80, 60],
                    'Paper-Tsukurioki' : [50, 55, 70, 75, 80, 85, 65, 55, 55, 75, 80, 75, 70, 65, 55],
                    'Paper-Order' : [60, 65, 75, 80, 90, 80, 80, 55, 60, 82, 80, 70, 90, 70, 60]}
            label_a = ["Box", "Paper"]
            label_b = ["Tsukurioki", "Order"]

            draw_table.draw_table(data, label_a, label_b, mode="within")

        else:
            print "please input between or within"
