#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Prefill an Array题目地址：http://www.codewars.com/kata/54129112fb7c188740000162/train/python
'''

import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(prefill(3,1), [1,1,1])
    def test2(self):self.assertEqual(prefill(2,'abc'), ['abc','abc'])
    def test3(self):self.assertEqual(prefill('1',1), [1])
    def test4(self):self.assertEqual(prefill(3, prefill(2,'2d')), [['2d','2d'],['2d','2d'],['2d','2d']])

def prefill(n,v = None):
    try:
        n = int(n)
        return [v] * n      
    except Exception as TypeError:
        value = str(n) + " is invalid"

    
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def prefill(n=0,v=None):
    try:
        return [v] * int(n)
    except:
        raise TypeError(str(n) + ' is invalid')
'''