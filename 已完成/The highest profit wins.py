#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# The highest profit wins题目地址：https://www.codewars.com/kata/559590633066759614000063/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(min_max([1,2,3,4,5]), [1,5])
    def test2(self):self.assertEqual(min_max([2334454,5]), [5, 2334454])
    def test2(self):self.assertEqual(min_max([1]), [1, 1])


def min_max(lst):
    return [min(lst), max(lst)]
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：

'''