#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Formatting decimal places #0题目地址：https://www.codewars.com/kata/5641a03210e973055a00000d/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(two_decimal_places(4.659725356), 4.66, "didn't work for 4.659725356")
    def test2(self):self.assertEqual(two_decimal_places(173735326.3783732637948948), 173735326.38, "didn't work for 173735326.3783732637948948")
    def test3(self):self.assertEqual(two_decimal_places(4.653725356), 4.65, "didn't work for 4.653725356")
    def test4(self):self.assertEqual(two_decimal_places(2.675), 2.68, "worked for 2.675")


def two_decimal_places(n):
    return round(n, 2)
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：

'''