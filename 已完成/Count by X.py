#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Count by X题目地址：http://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(list(count_by(1, 5)), [1, 2, 3, 4, 5])
    def test2(self):self.assertEqual(list(count_by(2, 5)), [2, 4, 6, 8, 10])
    def test3(self):self.assertEqual(list(count_by(3, 5)), [3, 6, 9, 12, 15])
    def test4(self):self.assertEqual(list(count_by(50, 5)), [50, 100, 150, 200, 250])
    def test5(self):self.assertEqual(list(count_by(100, 5)), [100, 200, 300, 400, 500])


def count_by(x, n):
    return [i * x for i in range(1, n+1)]
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return range(x, x * n + 1, x)
'''