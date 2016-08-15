#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Grasshopper - Summation题目地址：http://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(summation(1), 1)
    def test2(self):self.assertEqual(summation(8), 36)


def summation(num):
    return sum([i for i in range(1, num + 1)])
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def summation(num):
    return (1+num) * num / 2
'''