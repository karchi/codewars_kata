#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目地址：
https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python
'''

import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(find_nb(4183059834009), 2022)
    def test2(self):self.assertEqual(find_nb(24723578342962), -1)
    def test3(self):self.assertEqual(find_nb(135440716410000), 4824)
    def test4(self):self.assertEqual(find_nb(40539911473216), 3568)
    def test5(self):self.assertEqual(find_nb(26825883955641), 3218)
    def test6(self):self.assertEqual(find_nb(1), 1)

def find_nb(m):
    n = 1
    while m > n**3:
        m -= n**3
        n +=1
    if m == n**3:
        return n
    else: return -1

if __name__ == '__main__':
    unittest.main()


    
    
    
'''
参考解法：

'''