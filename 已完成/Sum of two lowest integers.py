#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Sum of two lowest integers题目地址：http://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
    def test2(self):self.assertEqual(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
    def test3(self):self.assertEqual(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)
    def test4(self):self.assertEqual(sum_two_smallest_numbers([1, 8, 12, 18, -1]), 0)
    def test5(self):self.assertEqual(sum_two_smallest_numbers([-1, -1]), -2)

def sum_two_smallest_numbers(numbers):    
    return sum(sorted(numbers)[:2])
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：

'''