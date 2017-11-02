#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
# os.pardir: ".."
# os.path.dirname(__file__): abs path to enquette_vas.py 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from draw_graph import DrawGraph
from collections import OrderedDict
from one_way_anova_draw_table import DrawTable

if __name__ == '__main__':
    args = sys.argv
    if len(args) is not 2:
        print "python enquette_vas.py <sample_type>"
        print "please choose sample type: "
        print "paired-ttest: paired-ttest"
        print "unpaired-ttest: unpaired-ttest"
        print "w-one-way-anova: within-one-way-anova"
        print "b-one-way-anova: between-one-way-anova"
    else:
        draw_graph = DrawGraph()
        draw_table = DrawTable()
        data = OrderedDict()
        if args[1] == "paired-ttest":
            data['Sound']   = [65.3, 84.6, 79.9, 80.4, 52.2, 70.7, 64.2, 22.9, 30.8, 3.90]
            data['Gesture'] = [39.5, 26.8, 83.9, 54.1, 84.0, 36.6, 13.1, 46.6, 69.8, 83.1]
            draw_graph.draw_graph(data, "test", "condition", "vas value", tight_layout=True, test_mode="paired-ttest")

        elif args[1] == "unpaired-ttest":
            data['Sound']   = [65.3, 84.6, 79.9, 80.4, 52.2, 70.7, 64.2, 22.9, 30.8, 3.90]
            data['Gesture'] = [39.5, 26.8, 83.9, 54.1, 84.0, 36.6, 13.1, 46.6, 69.8, 83.1]
            draw_graph.draw_graph(data, "test", "condition", "vas value", tight_layout=True, test_mode="unpaired-ttest")
        
        elif args[1] == "w-one-way-anova":
            data['Sound']   = [6.53, 84.6, 79.9, 80.4, 52.2, 70.7, 64.2, 22.9, 30.8, 3.9]
            data['Gesture'] = [39.5, 26.8, 83.9, 54.1, 84.0, 36.6, 13.1, 46.6, 69.8, 83.1]
            data['Writing'] = [15.4, 86.0, 90.7, 55.9, 66.3, 33.1, 62.1, 54.7, 83.8, 39.6]
            draw_table.draw_table(data, mode="within")
            draw_graph.draw_graph(data, "test", "condition", "vas value", tight_layout=True, test_mode="within-anova")

        elif args[1] == "b-one-way-anova":
            data['Sound']   = [6.53, 84.6, 79.9, 80.4, 52.2, 70.7, 64.2, 22.9, 30.8, 3.9]
            data['Gesture'] = [39.5, 26.8, 83.9, 54.1, 84.0, 36.6, 13.1, 46.6, 69.8, 83.1]
            data['Writing'] = [15.4, 86.0, 90.7, 55.9, 66.3, 33.1, 62.1, 54.7, 83.8, 39.6]
            draw_table.draw_table(data)
            draw_graph.draw_graph(data, "test", "condition", "vas value", tight_layout=True, test_mode="between-anova")
        
        else:
            print "Please select test type."
            print "paired-ttest: paired-ttest"
            print "unpaired-ttest: unpaired-ttest"
            print "w-one-way-anova: within-one-way-anova"
            print "b-one-way-anova: between-one-way-anova"
