#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目地址：
https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
'''

import time
import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214")
    def test2(self):self.assertEqual(high_and_low("1 -1"), "1 -1")
    def test3(self):self.assertEqual(high_and_low("1 1"), "1 1")
    def test4(self):self.assertEqual(high_and_low("-1 -1"), "-1 -1")
    def test5(self):self.assertEqual(high_and_low("1 -1 0"), "1 -1")
    def test6(self):self.assertEqual(high_and_low("1 1 0"), "1 0")
    def test7(self):self.assertEqual(high_and_low("-1 -1 0"), "0 -1")
    def test8(self):self.assertEqual(high_and_low("42"), "42 42")
    def test9(self):self.assertEqual(high_and_low("24 3 18"), "24 3")


def high_and_low(strings):
    numbers = strings.split(" ")
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    result = " ".join([str(max(numbers)), str(min(numbers))])
    return result
    
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
def high_and_low(numbers):
  n = map(int, numbers.split(' '))
  return str(max(n)) + ' ' + str(min(n))
  
解法2：
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
'''