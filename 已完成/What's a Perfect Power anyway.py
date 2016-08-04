#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# What's a Perfect Power anyway?题目地址：http://www.codewars.com/kata/whats-a-perfect-power-anyway
'''

import time
import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(isPP(4), [2,2], "4 = 2^2")
    def test2(self):self.assertEqual(isPP(9), [3,2], "9 = 3^2")
    def test3(self):self.assertEqual(isPP(5), None, "5 isn't a perfect power")
    def test4(self):self.assertEqual(isPP(8), [2,3])

def isPP(n):
    for i in range(n % 2, int(n ** 0.5)+1, 2):
        for j in range(n % 2, int(n ** 0.5)+2):
            if i ** j == n:
                return [i, j]
            elif i ** j > n:
                break
    return None
    
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def isPP(n):
    for i in range(2, int(n**.5) + 1):
        number = n
        times = 0
        while number % i == 0:
            number /= i
            times += 1
            if number == 1:
                return [i, times]
    return None
    
解法2：
def isPP(n):
    for m in range(2, int(n**0.5) + 1):
        k = int(round(log(n, m)))
        if m ** k == n:
            return [m, k]
    return None
'''