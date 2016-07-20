#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目地址：
https://www.codewars.com/kata/sum-of-pairs
'''

import time
import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(sum_pairs([1, 4, 8, 7, 3, 15], 8),[1, 7])
    def test2(self):self.assertEqual(sum_pairs([1, -2, 3, 0, -6, 1], -6), [0, -6])
    def test3(self):self.assertEqual(sum_pairs([20, -13, 40], -7), None)
    def test4(self):self.assertEqual(sum_pairs([1, 2, 3, 4, 1, 0], 2), [1, 1])
    def test5(self):self.assertEqual(sum_pairs([10, 5, 2, 3, 7, 5], 10), [3, 7])
    def test6(self):self.assertEqual(sum_pairs([4, -2, 3, 3, 4], 8), [4, 4])
    def test7(self):self.assertEqual(sum_pairs([0, 2, 0], 0), [0, 0])
    def test8(self):self.assertEqual(sum_pairs([5, 9, 13, -3], 10), [13, -3])

'''
# 太慢了
from itertools import combinations
def sum_pairs(ints, s):
    last = len(ints) + 1
    result = None
    for pickNumbers in combinations(ints, 2):
        if sum(pickNumbers) == s:
            temp = list(pickNumbers)
            if ints.index(temp[1], ints.index(temp[0]) + 1) <= last:
                result = temp[:]
                last = ints.index(temp[1], ints.index(temp[0]) + 1)
    return result
'''


#太慢了
def sum_pairs(ints, s):
    result = None
    sub_ints = []
    for number in ints:
        if not number in sub_ints:
            sub_ints.append(s - number)
        else:
            result = [s - number, number]
            break
    return result


'''
#太慢了
def sum_pairs(ints, s):
    result = None
    sub_ints = {}
    for number in ints:
        if not number in sub_ints.keys():
            sub_ints[s - number] = number
        else:
            result = [s - number, number]
            break
    return result
'''
    
'''
def sum_pairs(ints, s):
    result = None
    while len(ints) > 1: 
        if s - ints[0] in ints[1:]:
            result = [ints[0], s - ints[0]]
            ints = ints[1:ints[1:].index(result[1])+1]
        else:
            ints.pop(0)
    return result
'''

if __name__ == '__main__':
    unittest.main()
    # print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
    # for i in range(10,1,-1):
        # print(i)
    
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