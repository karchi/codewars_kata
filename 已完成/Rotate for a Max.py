#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Rotate for a Max题目地址：https://www.codewars.com/kata/rotate-for-a-max
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(max_rot(38458215), 85821534)
    def test2(self):self.assertEqual(max_rot(195881031), 988103115)
    def test3(self):self.assertEqual(max_rot(896219342), 962193428)
    def test4(self):self.assertEqual(max_rot(69418307), 94183076)
    def test5(self):self.assertEqual(max_rot(56789), 68957)

'''
# 稍微慢点的写法：
def max_rot(n):
    n = str(n)
    resList = [n,]
    first = ""
    last = n[:]
    while len(last) > 1:
        temp = first + last[1:] + last[0]
        resList.append(temp)
        first += last[1]
        last = temp[len(first):]
    resList.append(first + last[0])
    return max([int(item) for item in resList])
'''

def max_rot(n):
    n = str(n)
    resList = [n,]
    first = ""
    for i in range(len(n)):
        resList.append(first + resList[i][(i+1):] + resList[i][i])
        first += resList[-1][i]
    return max([int(item) for item in resList])

    
if __name__ == '__main__':
    unittest.main()
    # 测试时间：
    start = time.clock()
    for i in range(10000):
        b = (max_rot(123456789))
    end = time.clock()
    print(end - start) #7.5-8.2

    



    
'''
参考解法：
def max_rot(n):
    s, arr = str(n), [n]
    for i in range(len(s)):
        s = s[:i] + s[i+1:] + s[i]
        arr.append(int(s))
    return max(arr)
'''