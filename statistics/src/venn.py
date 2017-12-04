#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib_venn import venn2
from matplotlib_venn import venn3
import matplotlib.pyplot as plt


#A=3,B=2,AB=1
venn2(subsets=(3, 2, 1), set_labels=('A', 'B'))
plt.show()

#A=5, B=2,C=3,AB=5,AC=2,BC=3,ABC=2
venn3(subsets={'100': 5, '010': 2, '001': 3,
               '110': 5, '101': 2, '011': 3,
               '111': 2}, set_labels=('A', 'B', 'C'))
plt.show()
