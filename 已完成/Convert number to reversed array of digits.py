#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Convert number to reversed array of digits题目地址：https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python
'''

import time
import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(digitize(35231),[1,3,2,5,3])


'''
# 稍慢   
def digitize(n):
    return [int(i) for i in list(str(n)[::-1])]
'''

def digitize(n):    
    res = []
    while n:
        res.append(n % 10)
        n = n // 10
    return res
    
if __name__ == '__main__':
    unittest.main()
    # 测试时间：
    # start = time.clock()
    # for i in range(10000):
        # b = (digitize(4232142))
    # end = time.clock()
    # print(end - start) #0.14-0.19

    



    
'''
参考解法：
def digitize(n):
    return map(int, str(n)[::-1])
'''