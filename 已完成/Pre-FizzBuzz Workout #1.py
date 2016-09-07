#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Pre-FizzBuzz Workout #1题目地址：https://www.codewars.com/kata/569e09850a8e371ab200000b/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(pre_fizz(1), [1])
    def test2(self):self.assertEqual(pre_fizz(2), [1,2])
    def test3(self):self.assertEqual(pre_fizz(3), [1,2,3])
    def test4(self):self.assertEqual(pre_fizz(4), [1,2,3,4])
    def test5(self):self.assertEqual(pre_fizz(5), [1,2,3,4,5])


def pre_fizz(n):
    return [i for i in range(1, n + 1)]
    
if __name__ == '__main__':
    unittest.main()

    
    



    
'''
参考解法：

'''