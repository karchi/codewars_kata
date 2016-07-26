#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Equal Sides Of An Array题目地址：https://www.codewars.com/kata/equal-sides-of-an-array
'''

import time
import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(find_even_index([20,10,30,10,10,15,35]),3)
    def test2(self):self.assertEqual(find_even_index([20,10,-80,10,10,15,35]),0)
    def test3(self):self.assertEqual(find_even_index([10,-80,10,10,15,35,20]),6)
    def test4(self):self.assertEqual(find_even_index(range(1,100)),-1)
    def test5(self):self.assertEqual(find_even_index([0,0,0,0,0]),0)
    def test6(self):self.assertEqual(find_even_index([-1,-2,-3,-4,-3,-2,-1]),3)
    def test7(self):self.assertEqual(find_even_index(range(-100,-1)),-1)

def find_even_index(arr):
    result = -1
    for i in range(len(arr)):
        if sum(arr[:i+1]) == sum(arr[i:]):
            result = i
            break
    return result
    
if __name__ == '__main__':
    unittest.main()
    # a = "a"
    # print(sum([]))
    
    # 测试时间：
    # start = time.clock()
    # for i in range(100000):
        # a = sum_pairs([20, -13, 40], -7)
        # b = sum_pairs([20, -13, 40, 23, 122, 492, 324, -245, 58, -132, -49, 942], -7)
    # end = time.clock()
    # print(end - start)

    



    
'''
参考解法：
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1
'''