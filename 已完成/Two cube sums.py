#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目地址：
https://www.codewars.com/kata/55fd4919ce2a1d7c0d0000f3/train/python
'''

import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(has_two_cube_sums(1729),True)
    def test2(self):self.assertEqual(has_two_cube_sums(42),False)
    def test3(self):self.assertEqual(has_two_cube_sums(1), False)
    def test4(self):self.assertEqual(has_two_cube_sums(4104), True)
    def test5(self):self.assertEqual(has_two_cube_sums(4105), False)


def has_two_cube_sums(n):
    count = 0
    for a in range(1,int(n**0.5)):
        for b in range(a,int(n**0.5)):
            if a**3 + b**3 == n:
                count += 1
            elif a**3 + b**3 > n:
                break
    if count >= 2:
        result = True
    else:
        result = False
    return result

if __name__ == '__main__':
    unittest.main()


    



    
    
'''
参考解法：
求立方根：n ** (1/3.0)
'''