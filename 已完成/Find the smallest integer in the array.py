#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Find the smallest integer in the array题目地址：https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(findSmallestInt([78,56,232,12,11,43]), 11)
    def test2(self):self.assertEqual(findSmallestInt([78,56,-2,12,8,-33]), -33)


def findSmallestInt(arr):
    return min(arr)
    
if __name__ == '__main__':
    unittest.main()

    

    



    
'''
参考解法：
findSmallestInt=min   
'''