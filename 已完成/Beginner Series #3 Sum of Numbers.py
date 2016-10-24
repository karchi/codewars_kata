#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Beginner Series #3 Sum of Numbers题目地址：https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(get_sum(0,1),1)
    def test2(self):self.assertEqual(get_sum(0,-1),-1)
    def test3(self):self.assertEqual(get_sum(1,0),1)
    def test4(self):self.assertEqual(get_sum(1, 1),1)
    def test5(self):self.assertEqual(get_sum(-1, 0),-1)
    def test6(self):self.assertEqual(get_sum(-1, 2),2)
    def test7(self):self.assertEqual(get_sum(3, 3),3)


    
def get_sum(a,b):
    if b < a:
        return get_sum(b, a)
    else:
        return sum([i for i in range(a, b+1)])
        
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) // 2
    
解法2：
def get_sum(a,b):
    return sum(range(min(a,b), max(a,b)+1))
    
解法3：
get_sum=lambda a,b: get_sum(b,a) if b<a else (b-a+1)*(a+b)/2
'''