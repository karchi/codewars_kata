#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# What's the real floor?题目地址：https://www.codewars.com/kata/574b3b1599d8f897470018f6/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(get_real_floor(1), 0)
    def test2(self):self.assertEqual(get_real_floor(5), 4)
    def test3(self):self.assertEqual(get_real_floor(15), 13)
    def test4(self):self.assertEqual(get_real_floor(-3), -3)
    def test5(self):self.assertEqual(get_real_floor(0), 0)

def get_real_floor(n):
    res = 0
    if n <= 0:
        res = n
    elif n <=13:
        res = n - 1
    else:
        res = n -2
    return res
    
    
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：

'''