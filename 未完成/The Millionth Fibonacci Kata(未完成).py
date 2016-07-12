#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import sys
# import os
#print(os.times())

import time,datetime
# print(time.localtime())

# 查看对象类别：type(obj)，查看对象内存地址：id(obj)， 查看对象属性：dir(obj)

'''
# 题目地址：
https://www.codewars.com/kata/53d40c1e2f13e331fc000c26/train/python
'''

import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(fib(0),0)
    def test2(self):self.assertEqual(fib(1),1)
    def test3(self):self.assertEqual(fib(2),1)
    def test4(self):self.assertEqual(fib(3),2)
    def test5(self):self.assertEqual(fib(4),3)
    def test6(self):self.assertEqual(fib(5),5)
    def test7(self):self.assertEqual(fib(-6),-8)
    def test8(self):self.assertEqual(fib(-5),5)
    def test9(self):self.assertEqual(fib(-96),-51680708854858323072)

'''
# 太慢的常规方法
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fib(n-1) + fib(n-2)
    else: # 负数的情况
        return fib(n+2) - fib(n+1)
'''

'''
# 还是很慢没改进的方法
def fib(n):
    result = [0,1]
    if abs(n) > 1:
        for x in range(2,abs(n)+1):
            result.append(sum(result))
            result = result[1:]
        if n > 1 or n % 2 == 1:
            return result[-1]
        else:
            return -result[-1]
    else:
        return result[n]
 '''


'''
# 还是很慢没改进的方法
def fib(n):
    result = [0,1]
    if abs(n) > 1:
        for x in range(2,abs(n)+1):
            result.append(result[-2] + result[-1])
        if n > 1 or n % 2 == 1:
            return result[abs(n)]
        else:
            return -result[abs(n)]
    else:
        return result[n]
'''

'''
# 用两个通项公式计算的：
def fib(n):
    result = round((1/5.0**0.5) * (((1 + 5.0**0.5)/2)**abs(n) - ((1 - 5.0**0.5)/2)**abs(n))) #其中一个通项公式
    if n >= 0 or n % 2 == 1:
        return result
    else:
        return -result

def fib(n):
    result = round(((1+5.0**0.5)**n - (1-5.0**0.5)**n) / (2**n * (5.0**0.5))) #另外一个通项公式
    return result
'''
    


# 目前最快，但还是太慢
def fib(n):
    first, second = 0, 1
    if n == 0:
        return 0
    elif n == 1 or n == -1:
        return 1
    for x in range(abs(n)-1):
        first, second = second, first + second
    if n > 1 or n % 2 == 1:
        return second
    else:
        return -second

        
if __name__ == '__main__':
    unittest.main()
    # for x in range(5):
        # print(fib(x))
    
    # 测试时间：
    # start = time.clock()
    # for i in range(10):
        # a = fib(20000)
    # end = time.clock()
    # print(end - start)

    



    
'''
参考解法：
# an=（1/√5）*{[(1+√5)/2]^n-[(1-√5)/2]^n}（n=1,2,3.....）
'''