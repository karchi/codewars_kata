#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Compare within margin题目地址：https://www.codewars.com/kata/56453a12fcee9a6c4700009c/train/python
'''

import time
import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(close_compare(1.99, 5, 3), -1)        
    def test2(self):self.assertEqual(close_compare(4, 5), -1)
    def test3(self):self.assertEqual(close_compare(5, 5), 0)
    def test4(self):self.assertEqual(close_compare(6, 5), 1)
    def test5(self):self.assertEqual(close_compare(2, 5, 3), 0)
    def test6(self):self.assertEqual(close_compare(5, 5, 3), 0)
    def test7(self):self.assertEqual(close_compare(8, 5, 3), 0)
    def test8(self):self.assertEqual(close_compare(8.1, 5, 3), 1)

    
def close_compare(a, b, margin = 0):
    if abs(a - b) <= margin:
        res = 0
    else:
        res = 1 if a > b else -1
    return res
    
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def close_compare(a, b, margin = 0):
    return 0 if abs(a - b) <= margin else -1 if b > a else 1
'''