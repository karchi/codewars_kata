#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目地址：
https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
'''

import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)


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