#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Build Tower题目地址：https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(tower_builder(1), ['*', ])
    def test2(self):self.assertEqual(tower_builder(2), [' * ', '***'])
    def test3(self):self.assertEqual(tower_builder(3), ['  *  ', ' *** ', '*****'])


def tower_builder(n_floors):
    res = []
    for n in range(1, n_floors + 1):
        res.append(" " * (n_floors - n) + "*" * (2 * n - 1) + " " * (n_floors - n))
    return res
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
'''