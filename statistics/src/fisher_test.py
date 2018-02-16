#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from scipy import stats
import math

class FisherTest:   
   def test(self, data):
      """
                     Yes   No   Total
      -------------------------------
      Condition1     a     b    a+b
      Condition2     c     d    c+d
      -------------------------------
      Total         a+c   b+d   n (= a+b+c+d)
      
      data[(data.keys())[0]][0] = a
      data[(data.keys())[0]][1] = c
      data[(data.keys())[1]][0] = b
      data[(data.keys())[1]][1] = d
      """
      # check data length is 2
      if len(data.keys()) != 2 and len(data[(data.keys())[0]]) != 2 and len(data[(data.keys())[1]]) != 2:
         print "Please check the components of your data."
         print "length of data should be four"
         sys.exit()

      else:
         a = data[(data.keys())[0]][0]
         c = data[(data.keys())[0]][1]
         b = data[(data.keys())[1]][0]
         d = data[(data.keys())[1]][1]
         a_plus_b = a + b
         b_plus_d = b + d
         n = a+b+c+d

         if a+b > 999 or b+c > 999 or a+c > 999 or a+d > 999 or n > 999:
            print "In python, it seems that we can't calculate fact(> 999)."
            sys.exit()
         else:
            #bunshi = kai(a+b) * kai(c+d) * kai(a+c) * kai(b+d)
            #bunbo = kai(n) * kai(a) * kai(b) * kai(c) * kai(d)
            #p =  bunshi / bunbo            
            p = 0.0
            for i in range(0, a+1):
               # adding p value when i=0, 1, ..., a
               b = a_plus_b - i
               d = b_plus_d - b
               c = n - i - b - d

               kai_a_b = math.factorial(i+b)
               kai_c_d = math.factorial(c+d)
               kai_a_c = math.factorial(i+c)
               kai_b_d = math.factorial(b+d)
               kai_a = math.factorial(i)
               kai_b = math.factorial(b)
               kai_c = math.factorial(c)
               kai_d = math.factorial(d)
               kai_n = math.factorial(n)

               # kai(c+d) / (kai(c) * kai(d))
               tmp1 = (kai_c_d / float(kai_c)) / kai_d
               # kai(a+b) / (kai(a) * kai(b))
               tmp2 = (kai_a_b / float(kai_a)) / kai_b
               # kai(a+c) * kai(b+d) / kai(n)
               tmp3 = (kai_a_c / float(kai_n)) * kai_b_d
               p += tmp1 * tmp2 * tmp3
            
            

            print "p value: " + str(p)
            return p
