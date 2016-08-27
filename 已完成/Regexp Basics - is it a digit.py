#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Regexp Basics - is it a digit题目地址：http://www.codewars.com/kata/567bf4f7ee34510f69000032/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):pass
    def test1(self):self.assertEqual(is_digit(""), False)
    def test2(self):self.assertEqual(is_digit("7"), True)
    def test3(self):self.assertEqual(is_digit(" "), False)
    def test4(self):self.assertEqual(is_digit("a"), False)
    def test5(self):self.assertEqual(is_digit("a5"), False)

    
def is_digit(n):
    return n.isdigit() if len(n) == 1 else False
    
if __name__ == '__main__':
    unittest.main()

    

    


    
'''
参考解法：
def is_digit(n):
    return n.isdigit() and len(n)==1
    
解法2：
import re
def is_digit(n):
    return bool(re.match("\d\Z", n))
'''