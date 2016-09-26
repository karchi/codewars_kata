#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Double Char题目地址：https://www.codewars.com/kata/56b1f01c247c01db92000076/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(double_char("String"),"SSttrriinngg")
    def test2(self):self.assertEqual(double_char("Hello World"),"HHeelllloo  WWoorrlldd")
    def test3(self):self.assertEqual(double_char("1234!_ "),"11223344!!__  ")


def double_char(s):
    return "".join([i * 2 for i in s])
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：

'''