#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Count of positives / sum of negatives题目地址：http://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]),[10,-65])
    def test2(self):self.assertEqual(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]),[8,-50])
    def test3(self):self.assertEqual(count_positives_sum_negatives([1]),[1,0])
    def test4(self):self.assertEqual(count_positives_sum_negatives([-1]),[0,-1])
    def test5(self):self.assertEqual(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]),[0,0])

def count_positives_sum_negatives(arr):
    res = []
    if arr != []:
        res.append(len([i for i in arr if i > 0]))
        res.append(sum([i for i in arr if i <= 0]))
    return res
            
        
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def count_positives_sum_negatives(arr):
    return [ sum(1 for x in arr if x > 0) , sum(x for x in arr if x < 0) ]
'''