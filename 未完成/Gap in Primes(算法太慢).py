#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
# print(time.localtime())

# 查看对象类别：type(obj)，查看对象内存地址：id(obj)， 查看对象属性：dir(obj)

'''
# 题目地址：
https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4/train/python
'''

import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(gap(2,100,110), [101, 103])
    def test2(self):self.assertEqual(gap(4,100,110), [103, 107])
    def test3(self):self.assertEqual(gap(6,100,110), None)
    def test4(self):self.assertEqual(gap(8,300,400), [359, 367])
    def test5(self):self.assertEqual(gap(10,300,400), [337, 347])
    # def test6(self):self.assertEqual(gap(10,300,400), [337, 347])


global primes
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]

def add_prime(n):
    number = primes[-1]+2
    while primes[-1] <= n:
        flag = True
        for _ in primes[:]:
            if number % _ == 0:
                flag = False
                break
            if _ ** 2 > number:
                break
        if flag == True:
            primes.append(number)
        number += 2
        
def mid_search_start(searchlist, x):
    begin = 0
    last = len(searchlist)
    while(begin <= last):
        mid = (begin + last) // 2
        if x == searchlist[mid]:
            return mid
        elif searchlist[mid] < x:
            begin = mid + 1
        else:
            last = mid - 1
    if searchlist[mid] < x <= searchlist[mid+1]:
        return mid + 1
    elif searchlist[mid-1] < x <= searchlist[mid]:
        return mid

def gap(g, m, n):
    if primes[-1] <= n:
        add_prime(n)
    start = end = None        
    # for x in primes[:]:
        # if m <= x:
            # start = primes.index(x)
            # break
    # for y in primes[:]:
        # if n <= y:
            # end = primes.index(y)
            # break
    start = mid_search_start(primes[:], m)
    for y in range(len(primes),0,-1):
        if primes[y-1] <= n < primes[y]:
            end = y - 1
            break
    if start == end or start == None:
        return None
    for z in range(start, end):
        if primes[z+1] - primes[z] == g:
            return [primes[z], primes[z+1]]
    return None
        
        
if __name__ == '__main__':
    # unittest.main()
    # print(gap(4,100,110))
    # for i in range(10,1,-1):
        # print(i)
    
    # 测试时间：
    start = time.clock()
    for i in range(5):
        a = gap(4,30000,100000)
    end = time.clock()
    print(end - start)

    



    
'''
参考解法：

'''