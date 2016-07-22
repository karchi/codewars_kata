#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目地址：
https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python
'''

import time
import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(dig_pow(89, 1), 1)
    def test2(self):self.assertEqual(dig_pow(92, 1), -1)
    def test3(self):self.assertEqual(dig_pow(46288, 3), 51)



def dig_pow(n, p):
    strn = str(n)
    powresult = 0
    for i in range(p, p + len(strn)):
        powresult += (int(strn[i - p]) ** i)
    if powresult % n == 0:
        result = powresult / n
    else:
        result = -1
    return result
    
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
def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1
  
另一种解法：
def dig_pow(n, p):
    summ = 0
    for digit in str(n):
        summ += int(digit)**int(p)
        p += 1
    if summ % int(n) == 0:
        return summ/int(n)
    return -1
'''