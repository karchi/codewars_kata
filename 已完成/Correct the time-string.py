#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Correct the time-string题目地址：https://www.codewars.com/kata/57873ab5e55533a2890000c7/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(time_correct(None), None)
    def test2(self):self.assertEqual(time_correct(""), "")
    def test3(self):self.assertEqual(time_correct("001122"), None)
    def test4(self):self.assertEqual(time_correct("00;11;22"), None)
    def test5(self):self.assertEqual(time_correct("0a:1c:22"), None)
    def test6(self):self.assertEqual(time_correct("09:10:01"), "09:10:01")
    def test7(self):self.assertEqual(time_correct("11:70:10"), "12:10:10")
    def test8(self):self.assertEqual(time_correct("19:99:99"), "20:40:39")
    def test9(self):self.assertEqual(time_correct("24:01:01"), "00:01:01")
    def test10(self):self.assertEqual(time_correct("52:01:01"), "04:01:01")

    
import re

def time_correct(t):
    res = None
    if type(t) != str or len(t) == 0:
        res = t
    elif not re.search("\d{2,}:\d{2,}:\d{2,}", t):
        res = None
    else:
        temp = t.split(":")
        for i in range(3):
            temp[i] = int(temp[i])
        while temp[2] >= 60:
            temp[1] += 1
            temp[2] -= 60
        while temp[1] >= 60:
            temp[0] += 1
            temp[1] -= 60
        while temp[0] >= 24:
            temp[0] -= 24
        for i in range(3):
            if temp[i] < 10:
                temp[i] = "0" + str(temp[i])
            else:
                temp[i ]= str(temp[i])
        res = ":".join(temp)
    return res
        
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def time_correct(t):
    if not t: return t
    try:
        h, m, s = map(int, t.split(':'))
        if s >= 60: s -= 60; m += 1
        if m >= 60: m -= 60; h += 1
        return '%02d:%02d:%02d' % (h % 24, m, s)
    except: pass
'''