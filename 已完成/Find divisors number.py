#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Find divisors number题目地址：https://www.codewars.com/kata/542c0f198e077084c0000c2e/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(divisors(4), 3)
    def test2(self):self.assertEqual(divisors(5), 2)
    def test3(self):self.assertEqual(divisors(12), 6)
    def test4(self):self.assertEqual(divisors(30), 8)

def divisors(n):
    return len([i for i in range(1, n+1) if n % i == 0])
    
    
if __name__ == '__main__':
    unittest.main()

    



    
'''
参考解法：

'''