#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目地址：
https://www.codewars.com/kata/56747fd5cb988479af000028/train/python
'''

import time
import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(get_middle("test"),"es")
    def test2(self):self.assertEqual(get_middle("testing"),"t")
    def test3(self):self.assertEqual(get_middle("middle"),"dd")
    def test4(self):self.assertEqual(get_middle("A"),"A")
    def test5(self):self.assertEqual(get_middle("of"),"of")


def get_middle(s):
    while len(s) > 2:
        s = s[1:-1]
    return s

    
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
def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]
   
def get_middle(s):
    i = (len(s) - 1) // 2
    return s[i:-i] or s
'''