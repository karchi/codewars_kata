#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Basic Mathematical Operations题目地址：http://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
        
    def test1(self):self.assertEqual(basic_op('+', 4, 7), 11)
    def test2(self):self.assertEqual(basic_op('-', 15, 18), -3)
    def test3(self):self.assertEqual(basic_op('*', 5, 5), 25)
    def test4(self):self.assertEqual(basic_op('/', 49, 7), 7)
    
    
def basic_op(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))
   

    
if __name__ == '__main__':
    unittest.main()
   

    
    
    



    
'''
参考解法：
def basic_op(operator, value1, value2):
    if operator=='+':
        return value1+value2
    if operator=='-':
        return value1-value2
    if operator=='/':
        return value1/value2
    if operator=='*':
        return value1*value2
'''