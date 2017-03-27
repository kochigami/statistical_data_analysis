#!/usr/bin/env python
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats

# functions for calculating t value (% Now we don't use it. We use stats.ttest_rel(l1, l2) because it returns p value.)
def difference_average (l1, l2):
    difference_average = 0.0
    for i in range(len(l1)):
        difference_average += l1[i] - l2[i]
    difference_average = difference_average / (len(l1))
    return difference_average

def difference_variance (l1, l2):
    difference_variance = 0.0
    diff_average = difference_average(l1, l2)
    for i in range(len(l1)):
        difference_variance += (l1[i] - l2[i] - diff_average) * (l1[i] - l2[i] - diff_average)
    difference_variance = difference_variance / (len(l1))
    return difference_variance

def difference_error (l1, l2):
    difference_error = 0.0
    diff_variance = difference_variance(l1, l2)
    difference_error = math.sqrt (diff_variance / (len(l1) - 1))
    return difference_error

def t_value (l1, l2):
    t = 0.0
    diff_average = difference_average(l1, l2)
    diff_error = difference_error(l1, l2)
    t = diff_average / diff_error
    return t

# functions for drawing a graph
def create_nested_list (l1, l2):
    # create a nested list [[x1, x2, x3, x4], [y1, y2, y3, y4]]
    inner_list = []
    outer_list = []
    for i in range(len(l1)):
        inner_list.append(l1[i])
    outer_list.append(inner_list)
    
    inner_list = []
    for i in range(len(l2)):
        inner_list.append(l2[i])
    outer_list.append(inner_list)
    
    return outer_list

def sample_data_average (l1):
    ave = 0.0
    for i in range(len(l1)):
        ave = ave + l1[i]
    ave = ave / (len(l1))
    return ave

def sample_data_average_list (l1):
    average_list = [] 
    for i in range(len(l1)):
        average = sample_data_average(l1[i])
        average_list.append(average)
    return average_list

def sample_variance (l1):
    sample_variance = 0.0
    ave = sample_data_average(l1)
    for i in range(len(l1)):
        sample_variance += (l1[i] - ave) * (l1[i] - ave)
    sample_variance = sample_variance / (len(l1))
    return sample_variance

def sample_error (l1):
    sample_error = math.sqrt (sample_variance(l1))
    return sample_error
    
def sample_error_list (l1):
    error_list = []
    for i in range(len(l1)):
        error = sample_error(l1[i])
        error_list.append(error)
    return error_list

def draw_graph(title, label, xlabel, ylabel, l1, l2):
    # calculate t & p value
    t, p = stats.ttest_rel(l1, l2)

    # create a nested list [[x1, x2, x3, x4], [y1, y2, y3, y4]]
    nested_list=[]
    nested_list = create_nested_list(l1, l2)

    # calculate sample_data_average [ave_x, ave_y]
    y_data = sample_data_average_list (nested_list)
    max_y_data = math.ceil(max(y_data))
    min_y_data = math.floor(min(y_data))
   
    # calculate sample_error [err_x, err_y]
    y_error = sample_error_list (nested_list)

    left = np.array([])
    
    for i in range(len(label)):
        left = np.append(left, i+1)
    plt.bar(left, y_data, color="#FF5B70", yerr=y_error, align="center", ecolor="blue", capsize=60)
    plt.rcParams["font.size"] = 28
    plt.tick_params(labelsize=28)
    ax = plt.gca()
    w = 0.4
    for j in range(len(y_data)):
        ann = ax.annotate(str((round (y_data[j] * 100.0)) * 0.01), xy=(left[j] - w * 0.5 * 0.5, y_data[j] / 2.0), fontsize=28)
    plt.xticks(left, label)
    new_title = title + "  (N = " + str(len(l1)) + ", * p < 0.1, ** p < 0.05)"
    plt.title(new_title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if p < 0.05:
        input_word = "**" + " (p = " + str(p) + " )"
        plt.text(1.0, max_y_data * 0.95, input_word)
    elif p < 0.1:
        input_word = "*" + " (p = " + str(p) + " )"
        plt.text(1.0, max_y_data * 0.95, input_word)
    else:
        input_word = " p = " + str(p)
        plt.text(1.0, max_y_data * 0.95, input_word)

    plt.text(0.90, max_y_data * 0.9, "|--------------------------------------------|")
    plt.grid(True)
    plt.tight_layout()

    #plt.savefig("graph.pdf") # TODO path
    plt.show()

def main():
    # a = [225.48972,
    #      236.54971]
    # b = [169.1854,
    #      163.793112679]
    # a = [255.56605,
    #      267.48198]
    # b = [135.141159,
    #      84.659183899]
    a = [0, 1, 3, 1, 3, 3, 4, 2, 4, 1, 3, 3, 0, 2, 1]
    b = [1, 3, 2, 4, 3, 4, 2, 1, 5, 2, 3, 4, 5, 1, 1]
    # paired t-value: -1.46759877141, degree of freedom: 14
    #b = [1, 3, 2, 4, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    # paired t-value: -4.92800147686, degree of freedom: 14
    #a = [90, 75, 75, 75, 80, 65, 75, 80]
    #b = [95, 94, 92, 95, 95, 95, 90, 95]

    # calculate t value
    # TODO: calculate p value
    #t = t_value(a, b)
    #print "paired t-value: " + str(t) + ", degree of freedom: " + str((len(a) - 1))

    # draw a graph
    draw_graph("Test", ["a", "b"], "type", "average", a, b)

if __name__ == '__main__':
    main()
