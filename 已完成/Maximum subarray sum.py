#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目地址：
https://www.codewars.com/kata/maximum-subarray-sum
'''

import unittest
import time   
   
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(maxSequence([]), 0)
    def test2(self):self.assertEqual(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)


       
def maxSequence(arr):
    result = 0
    sum_arr = []
    if len(arr) == 0:
        return result
    for i in range(len(arr)):
        sum_arr.append(sum(arr[:i]))
    max_sum = max(sum_arr)
    min_sum = min(sum_arr[:sum_arr.index(max_sum)])
    if min_sum >= 0:
        result = max_sum
    else:
        result = max_sum - min_sum
    return result


if __name__ == '__main__':
    unittest.main()
    
    # 测试时间：
    # start = time.clock()
    # for i in range(5):
        # a = dbl_linear(20000)
    # end = time.clock()
    # print(end - start)

    



    
'''
参考解法：
def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max

另一种解法：
def maxSequence(arr):
  lowest = ans = total = 0
  for i in arr:
    total += i
    lowest = min(lowest, total)
    ans = max(ans, total - lowest)
  return ans
'''