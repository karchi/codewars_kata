#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Fibonacci, Tribonacci and friends题目地址：https://www.codewars.com/kata/556e0fccc392c527f20000c5/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test2(self):self.assertEqual(Xbonacci([0,1],10),[0,1,1,2,3,5,8,13,21,34])
    def test3(self):self.assertEqual(Xbonacci([1,1],10),[1,1,2,3,5,8,13,21,34,55])
    def test4(self):self.assertEqual(Xbonacci([0,0,0,0,1],10),[0,0,0,0,1,1,2,4,8,16])
    def test5(self):self.assertEqual(Xbonacci([1,0,0,0,0,0,1],10),[1,0,0,0,0,0,1,2,3,6])
    def test6(self):self.assertEqual(Xbonacci([1,0,0,0,0,0,0,0,0,0],20),[1,0,0,0,0,0,0,0,0,0,1,1,2,4,8,16,32,64,128,256])
    def test7(self):self.assertEqual(Xbonacci([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],9),[1, 2, 3, 4, 5, 6, 7, 8, 9])
    
def Xbonacci(signature,n):
    res = signature[:]
    x = len(signature)
    while len(res) < n:
        res.append(sum(res[-x:]))
    return res[:n]
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：

'''