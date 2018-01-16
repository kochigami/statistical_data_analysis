#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
from chi_squared_test_draw_graph import ChiSquaredTestDrawGraph

# TODO
# draw graph and table
# See: http://www.f.kpu-m.ac.jp/c/kouza/joho/kiso/topics/kentei/top.html#fig

if __name__ == '__main__':
    args = sys.argv
    if len(args) is not 1:
        print "python sample_chi_squared_test.py"
    else:
        d = ChiSquaredTestDrawGraph()
        # Q2 children
        #data = np.array([[43, 28],[19, 52]])
        # Q2 adults
        # data = np.array([[8, 12],[11, 9]])

        # enquette
        # q1. adults (29), children (27)
        #data = np.array([[20, 9],[18, 9]])
        # q1. female (30), male (26)
        #data = np.array([[21, 9],[17, 9]])

        # q2. adults (29), children (27)
        #data = np.array([[7, 22],[16, 11]])
        # q2. female (30), male (26)
        #data = np.array([[15, 15],[8, 18]])

        # q3. adults (29), children (27)
        #data = np.array([[16, 13],[12, 15]])
        # q3. female (30), male (26)        
        #data = np.array([[16, 14],[12, 14]])

        # q4. adults (29), children (27)
        #data = np.array([[9, 20],[15, 12]])
        # q4. female (30), male (26)        
        data = np.array([[13, 17],[11, 15]])

        # q1. adults-children
        # d.draw_graph(data, ["Adults", "Children"], "The ratio of people who want to use a robot which helps doing household chores", "condition", "percentage", tight_layout=True, mode="unpaired")
        # q1. female-male
        # d.draw_graph(data, ["Female", "Male"], "The ratio of people who want to use a robot which helps doing household chores", "condition", "percentage", tight_layout=True, mode="unpaired")

        # q2. adults-children
        #d.draw_graph(data, ["Adults", "Children"], "The ratio of people who want to use a robot which can be a companion for its user", "condition", "percentage", tight_layout=True, mode="unpaired")
        # q2. female-male
        # d.draw_graph(data, ["Female", "Male"], "The ratio of people who want to use a robot which can be a companion for its user", "condition", "percentage", tight_layout=True, mode="unpaired")

        # q3. adults-children
        # d.draw_graph(data, ["Adults", "Children"], "The ratio of people who want to use a robot which takes care of its user's health", "condition", "percentage", tight_layout=True, mode="unpaired")
        # q3. female-male
        # d.draw_graph(data, ["Female", "Male"], "The ratio of people who want to use a robot which takes care of its user's health", "condition", "percentage", tight_layout=True, mode="unpaired")

        # q4. adults-children
        # d.draw_graph(data, ["Adults", "Children"], "The ratio of people who want to use a robot which its user can raise it", "condition", "percentage", tight_layout=True, mode="unpaired")
        # q4. female-male
        # d.draw_graph(data, ["Female", "Male"], "The ratio of people who want to use a robot which its user can raise it", "condition", "percentage", tight_layout=True, mode="unpaired")

        d.draw_graph(data, ["Touch", "Speak"], "The ratio of children who touched or spoke to the robot \n on their own accord", "condition", "percentage", tight_layout=True, mode="paired")
        # d.draw_graph(data, ["Touch", "Speak"], "The ratio of adults who touched or spoke to the robot \n on their own accord", "condition", "percentage", tight_layout=True, mode="paired")
        # TODO
        # draw table        
