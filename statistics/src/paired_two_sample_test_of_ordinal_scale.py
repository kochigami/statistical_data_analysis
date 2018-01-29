#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scipy import stats
import sys
import itertools
import math

'''
signed rank sum test
signes test
'''

class PairedTwoSampleTestOfOrdinalScale:
    def calc_ave(self, order, count, i):
        tmp_sum = 0.0
        for j in range(count):
            tmp_sum += i+1+j
        for j in range(count):
            order.append(tmp_sum / float(count))

    def test(self, data, mode="signed_rank_sum_test"):
        '''
        signed rank sum test
        '''
        """
        data = {'Product_A': [25, 62, 58, 26, 42, 18, 11, 33, 50, 34]
                'Product_B': [26, 31, 35, 24, 47, 13, 11, 21, 42, 18]}
        """
        if mode == "signed_rank_sum_test":
            x = data[(data.keys())[0]]
            y = data[(data.keys())[1]]
            # note: nx == ny
            nx = len(data[(data.keys())[0]])
            if len(x) != len(y):
                print "Please check the contents of your data."
                print "The number of data type should be two."
                sys.exit()
            else:
                diff = []
                for i in range(nx):
                    if x[i] - y[i] != 0.0:
                        diff.append(x[i] - y[i])

                for i in range(len(diff)):
                    for j in range(i+1, len(diff)):
                        if abs(diff[i]) > abs(diff[j]):
                            tmp = diff[i]
                            diff[i] = diff[j]
                            diff[j] = tmp

                order = []
                tmp = []
                if abs(diff[0]) == abs(diff[1]):
                    tmp.append(1)
                else:
                    tmp.append(0)

                for i in range(1, len(diff)-1):
                    if abs(diff[i]) == abs(diff[i+1]) or abs(diff[i-1]) == abs(diff[i]):
                        tmp.append(1)
                    else:
                        tmp.append(0)

                if abs(diff[len(diff) -1]) == abs(diff[len(diff) -2]):
                    tmp.append(1)
                else:
                    tmp.append(0)

                # tmp
                # [0, 0, 1, 1, 0, 0, 0, 0, 0]
                count = 1
                for i in range(len(tmp)-1):
                    if tmp[i+count-1] == 1:
                        count = 1
                        for j in range(i+count-1, len(tmp)-1):
                            if tmp[j] == tmp[j+1]:
                                count += 1
                            else:
                                self.calc_ave(order, count, i)
                                break
                    else:
                        order.append(i+count-1.0+1.0)
                    
                t_plus = 0.0
                t_minus = 0.0
                for i in range(len(diff)):
                    if diff[i] < 0.0:
                        t_minus += order[i]
                    else:
                        t_plus += order[i]
            
                if t_minus < t_plus:
                    t = t_minus
                else:
                    t = t_plus
            
                print "t: " + str(t)
                print "n: " + str(len(diff))
                print "If t is smaller than T_threshold at n = " + str(len(diff)) + ", you can reject null hypothesis."
                return True

        elif mode == "signed_test":
            '''
            signed test
            '''
            """
            data = {'Cusine_A': [5, 3, 4, 4, 3, 4, 4, 1, 3, 3, 5, 3]
            'Cusine_B': [3, 5, 3, 3, 5, 2, 2, 1, 4, 2, 2, 3]}
            # https://kusuri-jouhou.com/statistics/fugou.html
            """
            x = data[(data.keys())[0]]
            y = data[(data.keys())[1]]
            # note: nx == ny
            nx = len(data[(data.keys())[0]])
            if len(x) != len(y):
                print "Please check the contents of your data."
                print "The number of data type should be two."
                sys.exit()
            else:
                diff = []
                for i in range(nx):
                    diff.append(x[i] - y[i])
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
                print "p value: " + str(p)
                return p

        else:
            print "Please choose mode: 'signed_test' or 'signed_rank_test'"
