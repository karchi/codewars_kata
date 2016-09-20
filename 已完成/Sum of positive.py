#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Sum of positive题目地址：https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(positive_sum([1,2,3,4,5]),15)
    def test2(self):self.assertEqual(positive_sum([1,-2,3,4,5]),13)
    def test3(self):self.assertEqual(positive_sum([-1,2,3,4,-5]),9)
    def test4(self):self.assertEqual(positive_sum([]),0)
    def test5(self):self.assertEqual(positive_sum([-1,-2,-3,-4,-5]),0)


def positive_sum(arr):
    return sum([i for i in arr if i > 0])
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：

'''