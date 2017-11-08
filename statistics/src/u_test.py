#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import sys
import itertools
import math

class UTEST:
    def paired_utest(self, data):
        """
        data = {'Cusine_A': [5, 3, 4, 4, 3, 4, 4, 1, 3, 3, 5, 3]
                'Cusine_B': [3, 5, 3, 3, 5, 2, 2, 1, 4, 2, 2, 3]}
        # https://kusuri-jouhou.com/statistics/fugou.html
       """
        if len(data[(data.keys())[0]]) != len(data[(data.keys())[1]]):
            print "Please check the contents of your data."
            print "The number of data type should be two."
            sys.exit()
        else:
            diff = []
            for i in range(len(data[(data.keys())[0]])):
                diff.append(data[(data.keys())[0]][i] - data[(data.keys())[1]][i])         
            count_plus = 0
            count_minus = 0
            for i in range(len(diff)):
                if diff[i] > 0.0:
                    count_plus += 1
                if diff[i] < 0.0:
                    count_minus += 1
            # choose smallest one among count_plus and count_minus
            if count_plus < count_minus or count_plus == count_minus:
                r = count_plus
            else:
                r = count_minus
            # emit the pair if diff == 0
            n = count_plus + count_minus

            # if 5 < n < 25 or n == 25, execute below
            if n < 6:
                print "n should be more than 5."
                sys.exit()
            elif n > 5 and (n < 25 or n == 25):
                p = 0.0
                # hypothesis: there is no difference between condition A & B
                #            = the probability that smallest one (r) appeared is 1/2
                # so caluculate the probability that the value appears which is smaller than r 
                # for loop from 0 to r
                for i in range(0, r+1):
                    # [0] * 5 = [0, 0, 0, 0, 0]
                    # one of the initializing list
                    # list(itertools.combinations(['a', 'b', 'c', 'd', 'e'], 3))
                    # >> [('a', 'b', 'c'),
                    #     ('a', 'b', 'd'),
                    #     ('a', 'b', 'e'),
                    #     ('a', 'c', 'd'),
                    #     ('a', 'c', 'e'),
                    #     ('a', 'd', 'e'),
                    #     ('b', 'c', 'd'),
                    #     ('b', 'c', 'e'),
                    #     ('b', 'd', 'e'),
                    #     ('c', 'd', 'e')]
                    # len(list(itertools.combinations(['a', 'b', 'c', 'd', 'e'], 3)))
                    # >> 10
                    p += len(list(itertools.combinations([0] * n, i))) * pow(0.5, n)
                    # for two-side test, p value should be doubled
                    p = p * 2.0
            # else (n > 25): calculate z
            elif n > 25:
            # followed algorithm described in this link:
            # https://kusuri-jouhou.com/statistics/fugou.html
                u = n * 0.5
                theta = math.sqrt(n) * 0.5
                if r < u:
                    z = ((r + 0.5) - u) / theta
                else:
                    z = ((r - 0.5) - u) / theta

                # calculate p value from z value
                # multiply 2.0 for two-side test
                p = stats.norm.sf(abs(z)) * 2.0
            return p

    def unpaired_utest(self, data):
        """
        data = {'Children':  [20, 18, 15, 13, 10, 6],
                'Adults': [17, 16, 12, 9, 8, 6, 4, 2]}
        # https://kusuri-jouhou.com/statistics/mann.html
        # use mannwhitneyu() from scipy
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html
        # however, alternative keyword cannnot be used
        # TypeError: mannwhitneyu() got an unexpected keyword argument 'alternative'
        """
        if len(data.keys()) != 2:
            print "Please check the contents of your data."
            print "The number of data type should be two."
            sys.exit()
        result = stats.mannwhitneyu(data[(data.keys())[0]], data[(data.keys())[1]], use_continuity=True)
        # return pvalue
        return result[1]
