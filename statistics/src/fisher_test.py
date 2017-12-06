#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math

def recur_factorial(n):
   """
   Function to return the factorial
   of a number using recursion
   """
   if n == 1:
      return n
   else:
      return n * recur_factorial(n-1)

class FisherTest:   
   def test(self, data):
      """
                     Yes   No   Total
      -------------------------------
      Condition1     a     b    a+b
      Condition2     c     d    c+d
      -------------------------------
      Total         a+c   b+d   n (= a+b+c+d)
      
      data[0][0] = a
      data[0][1] = b
      data[1][0] = c
      data[1][1] = d
      """
      # check data length is 2
      if len(data) != 2 and len(data[0]) != 2 and len(data[1]) != 2:
         print "Please check the components of your data."
         print "length of data should be four"
         sys.exit()

      else:
         a = data[0][0]
         b = data[0][1]
         c = data[1][0]
         d = data[1][1]
         n = a+b+c+d

         if a+b > 999 or b+c > 999 or a+c > 999 or a+d > 999 or n > 999:
            print "In python, it seems that we can't calculate fact(> 999)."
            sys.exit()
         else:
            #bunshi = kai(a+b) * kai(c+d) * kai(a+c) * kai(b+d)
            #bunbo = kai(n) * kai(a) * kai(b) * kai(c) * kai(d)
            #p =  bunshi / bunbo

            kai_a_b = recur_factorial(a+b)
            kai_c_d = recur_factorial(c+d)
            kai_a_c = recur_factorial(a+c)
            kai_b_d = recur_factorial(b+d)
            kai_a = recur_factorial(a)
            kai_b = recur_factorial(b)
            kai_c = recur_factorial(c)
            kai_d = recur_factorial(d)
            kai_n = recur_factorial(n)
            
            tmp1 = (kai_c_d / float(kai_c)) / kai_d
            tmp2 = (kai_a_b / float(kai_a)) / kai_b
            tmp3 = (kai_a_c / float(kai_n)) * kai_b_d
            p = tmp1 * tmp2 * tmp3            
            return p
