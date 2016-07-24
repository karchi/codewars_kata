#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Even or Odd题目地址：https://www.codewars.com/kata/even-or-odd
'''

import time
import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(even_or_odd(2), "Even")
    def test2(self):self.assertEqual(even_or_odd(0), "Even")
    def test3(self):self.assertEqual(even_or_odd(7), "Odd")
    def test4(self):self.assertEqual(even_or_odd(1), "Odd")


def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

    
if __name__ == '__main__':
    unittest.main()
    
    # 测试时间：
    # start = time.clock()
    # for i in range(100000):
        # a = sum_pairs([20, -13, 40], -7)
        # b = sum_pairs([20, -13, 40, 23, 122, 492, 324, -245, 58, -132, -49, 942], -7)
    # end = time.clock()
    # print(end - start)

    



    
'''
参考解法：

'''