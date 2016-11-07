#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Head, Tail, Init and Last题目地址：https://www.codewars.com/kata/54592a5052756d5c5d0009c3/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test2(self):self.assertEqual(head([5,1]), 5);
    def test3(self):self.assertEqual(tail([1]), []);
    def test4(self):self.assertEqual(init([1,5,7,9]), [1,5,7]);
    def test5(self):self.assertEqual(last([7,2]),2);
    def test6(self):self.assertEqual(tail([1,2,3,4,5]),[2,3,4,5])

    
def head(x):
    return x[0]
    
def tail(x):
    res = []
    if len(x) >= 2:
        res = x[1:]
    return res

def init(x):
    return x[:-1]

def last(x):
    return x[-1]
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：

'''