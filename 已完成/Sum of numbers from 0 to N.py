#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Sum of numbers from 0 to N题目地址：https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(show_sequence(6),"0+1+2+3+4+5+6 = 21")
    def test2(self):self.assertEqual(show_sequence(7),"0+1+2+3+4+5+6+7 = 28")
    def test3(self):self.assertEqual(show_sequence(0),"0=0")
    def test4(self):self.assertEqual(show_sequence(-1),"-1<0")


def show_sequence(n):
    if n > 0:
        res = "+".join([str(i) for i in range(n+1)]) + " = " + str(sum([i for i in range(n+1)]))
    elif n == 0:
        res = "0=0"
    else:
        res = str(n) + "<0"
    return res
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：

'''