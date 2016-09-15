#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Sort the odd题目地址：https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
'''

import time
import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
    def test2(self):self.assertEqual(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
    def test3(self):self.assertEqual(sort_array([]),[])

'''
# 比较慢的写法
def sort_array(source_array):
    odd_list = sorted([item for item in source_array if item % 2 == 1])
    for i in range(len(source_array)):
        if source_array[i] % 2 == 1:
            source_array[i] = odd_list.pop(0)
    return source_array
'''

def sort_array(source_array):
    index_list = []
    odd_list = []
    for i in range(len(source_array)):
        if source_array[i] % 2 == 1:
            index_list.append(i)
            odd_list.append(source_array[i])
    odd_list.sort()
    for index in index_list:
        source_array[index] = odd_list.pop(0)
    return source_array    

    
if __name__ == '__main__':
    # unittest.main()
    # 测试时间：
    start = time.clock()
    for i in range(100000):
        a = sort_array([5, 3, 2, 8, 1, 4])
    end = time.clock()
    print(end - start) 

    



    
'''
参考解法：
def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]
'''