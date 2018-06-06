#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from scipy import stats
import math

class FisherTest:   
   def test(self, data):
      # check data length is 2
      if len(data.keys()) != 2:
         print "Please check the components of your data."
         print "Number of types should be two."
         sys.exit()

      elif len(data[(data.keys())[0]]) == 2 and len(data[(data.keys())[1]]) == 2:
         """
                    Yes   No   Total
      -------------------------------
      Condition1     a     b    a+b
      Condition2     c     d    c+d
      -------------------------------
      Total         a+c   b+d   n (= a+b+c+d)

      data[(data.keys())[0]][0] = a
      data[(data.keys())[0]][1] = b
      data[(data.keys())[1]][0] = c
      data[(data.keys())[1]][1] = d
         """

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
            p = 0.0
            # adding p value when i=0, 1, ..., a
            for i in range(0, a+1):
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
               '''
               bunshi = kai(a+b) * kai(c+d) * kai(a+c) * kai(b+d)
               bunbo = kai(n) * kai(a) * kai(b) * kai(c) * kai(d)
               p =  bunshi / bunbo
               '''
               p += tmp1 * tmp2 * tmp3

            print "p value: " + str(p)
            return p

      elif len(data[(data.keys())[0]]) == 3 and len(data[(data.keys())[1]]) == 3:
         """
                       Yes   No  Yes/No  Total
         -------------------------------------
         Condition1     a     b    c     a+b+c
         Condition2     d     e    f     d+e+f
         ------------------------------------
         Total         a+d   b+e   c+f   n (= a+b+c+d+e+f)

         data[(data.keys())[0]][0] = a
         data[(data.keys())[0]][1] = b
         data[(data.keys())[0]][2] = c
         data[(data.keys())[1]][0] = d
         data[(data.keys())[1]][1] = e
         data[(data.keys())[1]][2] = f
         """

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
            # 0 =< d, e =< n - a_b_c (d+e+f)
            # f = n - a_b_c (= d+e+f) - d - e
            # a = a_d - d
            # b = b_e - e
            # c = a_b_c - a - b
            
            for i in range(0, n - a_b_c + 1):
               for j in range(0, n - a_b_c- i + 1):
                  f_tmp = n - a_b_c - i - j
                  a_tmp = a_d - i
                  b_tmp = b_e - j
                  c_tmp = a_b_c - a_tmp - b_tmp
                  if a_tmp > 0 and b_tmp > 0 and c_tmp > 0 and f_tmp > 0 and a_tmp < a and b_tmp < b:
                     kai_a_b_c = math.factorial(a_b_c)
                     kai_d_e_f = math.factorial(n - a_b_c)
                     kai_a_d = math.factorial(a_d)
                     kai_b_e = math.factorial(b_e)
                     kai_c_f = math.factorial(n - a_d - b_e)
                     kai_a = math.factorial(a_tmp)
                     kai_b = math.factorial(b_tmp)
                     kai_c = math.factorial(c_tmp)
                     kai_d = math.factorial(i)
                     kai_e = math.factorial(j)
                     kai_f = math.factorial(f_tmp)
                     kai_n = math.factorial(n)

                     tmp1 = kai_a_b_c * kai_d_e_f * kai_a_d * kai_b_e * kai_c_f 
                     tmp2 = kai_a * kai_b * kai_c * kai_d * kai_e * kai_f * kai_n
                     print "{} {} {}".format(a_tmp,b_tmp,c_tmp)
                     print "{} {} {}\n".format(i,j,f_tmp)
                     print "{}".format(tmp1/float(tmp2))
                     print "\n"
                     p += tmp1 / float(tmp2)
            
            print "p value: " + str(p)
            return p
      else:
         print "If the number of components per each condition is more than three (= 4, 5,...), please calculate p value by yourself."
         sys.exit()
