#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Best travel题目地址：http://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
        
    def test1(self):self.assertEqual(choose_best_sum(230, 4, self.xs), 230)
    def test2(self):self.assertEqual(choose_best_sum(430, 5, self.xs), 430)
    def test3(self):self.assertEqual(choose_best_sum(430, 8, self.xs), None)
    
def choose_best_sum(t, k, ls):
    from itertools import combinations
    res = None
    temp = 0
    for i in combinations(ls, k):
        if temp <= sum(i) <= t:
            temp = sum(i)
            res = temp
    return res

    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
import itertools
def choose_best_sum(t, k, ls):
    try: 
        return max(sum(i) for i in itertools.combinations(ls,k) if sum(i)<=t)
    except:
        return None
'''