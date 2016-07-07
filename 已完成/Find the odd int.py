#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目地址：
https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
'''

import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
    # def test2(self):self.assertEqual(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
    # def test3(self):self.assertEqual(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
    # def test4(self):self.assertEqual(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
    # def test5(self):self.assertEqual(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")
    # def test6(self):self.assertEqual(find_nb(1), 1)

def find_it(seq):
    seq2 = list(set(seq))
    for x in seq2:
        if seq.count(x) % 2 == 1:
            return x

if __name__ == '__main__':
    unittest.main()


    
'''
参考解法：

'''