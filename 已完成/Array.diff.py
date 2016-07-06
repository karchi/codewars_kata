#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目地址：
https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
'''

import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
    def test2(self):self.assertEqual(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
    def test3(self):self.assertEqual(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
    def test4(self):self.assertEqual(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
    def test5(self):self.assertEqual(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")
    # def test6(self):self.assertEqual(find_nb(1), 1)

def array_diff(a, b):
    return [i for i in a if (i not in b)]
        

if __name__ == '__main__':
    unittest.main()


    
'''
参考解法：

'''