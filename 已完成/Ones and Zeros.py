#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Ones and Zeros题目地址：https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test2(self):self.assertEqual(binary_array_to_number([0,0,0,1]), 1)
    def test3(self):self.assertEqual(binary_array_to_number([0,0,1,0]), 2)
    def test4(self):self.assertEqual(binary_array_to_number([1,1,1,1]), 15)
    def test5(self):self.assertEqual(binary_array_to_number([0,1,1,0]), 6)


    
def binary_array_to_number(arr):
    base, res = 0, 0
    while arr:
        res += arr.pop() * (2 ** base)
        base += 1
    return res
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def binary_array_to_number(arr):
  return int("".join(map(str, arr)), 2)
'''