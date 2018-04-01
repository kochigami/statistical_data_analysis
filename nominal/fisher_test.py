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
      if len(data.keys()) != 2:
         print "Please check the components of your data. The number of types should be two."
         sys.exit()

      elif len(data[(data.keys())[0]]) == 2 and len(data[(data.keys())[1]]) == 2:
         a = data[(data.keys())[0]][0]
         b = data[(data.keys())[0]][1]
         c = data[(data.keys())[1]][0]
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

      elif len(data[(data.keys())[0]]) == 3 and len(data[(data.keys())[1]]) == 3:
         a = data[(data.keys())[0]][0]
         b = data[(data.keys())[0]][1]
         c = data[(data.keys())[0]][2]
         d = data[(data.keys())[1]][0]
         e = data[(data.keys())[1]][1]
         f = data[(data.keys())[1]][2]
         a_b_c = a + b + c
         b_e = b + e
         a_d = a + d
         n = a+b+c+d+e+f

         if a+d > 999 or b+e > 999 or c+f > 999 or a+b+c > 999 or d+e+f > 999 or n > 999:
            print "In python, it seems that we can't calculate fact(> 999)."
            sys.exit()
         else:
            p = 0.0
            if a_b_c - a < b_e:
               max_b = a_b_c - a
            else:
               max_b = b_e
            for i in range(0, a+1):
               # adding p value when i=0, 1, ..., a
               for j in range(0, max_b+1):
                  c = a_b_c - i - j
                  e = b_e - j
                  d = a_d - i
                  f = n - i - j - c - d - e
                  
                  kai_a_b_c = math.factorial(a_b_c)
                  kai_d_e_f = math.factorial(n - a_b_c)
                  kai_a_d = math.factorial(a_d)
                  kai_b_e = math.factorial(b_e)
                  kai_c_f = math.factorial(n - a_d - b_e)
                  kai_a = math.factorial(i)
                  kai_b = math.factorial(j)
                  kai_c = math.factorial(c)
                  kai_d = math.factorial(d)
                  kai_e = math.factorial(e)
                  kai_f = math.factorial(f)
                  kai_n = math.factorial(n)

                  tmp1 = kai_a_b_c * kai_d_e_f * kai_a_d * kai_b_e * kai_c_f 
                  tmp2 = kai_a * kai_b * kai_c * kai_d * kai_e * kai_f * kai_n
                  p += tmp1 / float(tmp2)
            
            print "p value: " + str(p)
            return p

      else:
         print "If the number of components per each condition is more than three (= 4, 5,...), please calculate p value by yourself."
         sys.exit()