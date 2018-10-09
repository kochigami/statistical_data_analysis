#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

'''
craete txt file per line from one csv file
'''

# Please modify path
READ_FILE_PATH="/home/nao/Downloads/openlab2018_adult.csv"
# Please create folder if it has not existed yet. (ex. adults in this case)
WRITE_FILE_PATH="/home/nao/Downloads/adults/"

i = 0
csvfile = open(READ_FILE_PATH, "r")
f = csv.reader(csvfile)

for line in f:
    i += 1
    if len(line) > 0:
        # create path including file name
        tmp = WRITE_FILE_PATH + "%02.f"%(i) + ".txt"
        with open(tmp, mode="w") as w:
            w.write(line[0])
    
