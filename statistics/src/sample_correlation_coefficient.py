#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from pearsons_product_moment_correlation_coefficient import PearsonsProductMomentCorrelationCoefficient
from spearmans_rank_correlation_coefficient import SpearmansRankCorrelationCoefficient

if __name__ == '__main__':
        args = sys.argv
        if len(args) is not 2:
                print "python sample_correlation_coefficient.py <sample_type>"
                print "please choose sample type: "
                print "1: pearson's product-moment correlation coefficient"
                print "2: spearman's rank correlation coefficient"
        else:
                if args[1] == "1":
                        data = [[3,1], [2,4], [0,1], [2,3], [3,6], [5,5], [4,3], [6,5], [3,5], [1,2]]    
                        pearsons_product_moment_correlation_coefficient = PearsonsProductMomentCorrelationCoefficient()
                        pearsons_product_moment_correlation_coefficient.test(data)
                elif args[1] == "2":
                        data = [[4.3,3.9], [2.1,0.8], [1.4,0.9], [0.9,1.5], [0.5,0.5]]
                        spearmans_rank_correlation_coefficient = SpearmansRankCorrelationCoefficient()
                        spearmans_rank_correlation_coefficient.test(data)
                else:
                        print "python sample_correlation_coefficient.py <sample_type>"
                        print "please choose sample type: "
                        print "1: pearson's product-moment correlation coefficient"
                        print "2: spearman's rank correlation coefficient"
