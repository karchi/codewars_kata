#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Is this a triangle题目地址：https://www.codewars.com/kata/56606694ec01347ce800001b/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(is_triangle(1, 2, 2), True, "didn't work when sides were 1, 2, 2")
    def test2(self):self.assertEqual(is_triangle(7, 2, 2), False, "didn't work when sides were 7, 2, 2")
    def test3(self):self.assertEqual(is_triangle(1, 2, 3), False, "didn't work when sides were 1, 2, 3")
    def test4(self):self.assertEqual(is_triangle(1, 3, 2), False, "didn't work when sides were 1, 3, 2")
    def test5(self):self.assertEqual(is_triangle(3, 1, 2), False, "didn't work when sides were 3, 1, 2")
    def test6(self):self.assertEqual(is_triangle(4, 2, 3), True, "didn't work when sides were 4, 2, 3")
    def test7(self):self.assertEqual(is_triangle(2, 2, 2), True, "didn't work when sides were 2, 2, 2")
    def test8(self):self.assertEqual(is_triangle(0, 2, 3), False, "didn't work when sides were 0, 2, 3")
    def test9(self):self.assertEqual(is_triangle(1, 2, -3), False, "didn't work when sides were 1, 2, -3")

def is_triangle(a, b, c):
    triangle = sorted([a,b,c])
    return triangle[0] > 0 and sum(triangle[:2]) > triangle[-1]
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)
    
解法2：
def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c
'''