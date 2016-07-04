#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目网址：
http://www.codewars.com/kata/550f22f4d758534c1100025a/train/python
'''

import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(dirReduc(['EAST', 'NORTH', 'EAST', 'WEST']), ['EAST', 'NORTH'])
    def test2(self):self.assertEqual(dirReduc( ['EAST', 'EAST', 'NORTH', 'WEST']), ['EAST', 'EAST', 'NORTH', 'WEST'])
    def test3(self):self.assertEqual(dirReduc( ['EAST', 'EAST', 'WEST', 'WEST']), [])
    # def test4(self):self.assertEqual(countBits(10), 2)
    # def test5(self):self.assertEqual(lowercase_count("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), 0)
    # def test6(self):self.assertEqual(lowercase_count("abcdefghijklmnopqrstuvwxyz"), 26)

def dirReduc(arr):
    result = []
    # print(arr)
    # if arr == ["NORTH"] or arr == ["SOUTH"] or arr == ["EAST"] or arr == ["WEST"]: return result
    for word in arr[:]:
        result.append(arr.pop(0))
        while len(result) >= 2 and ((result[-1] == "NORTH" and result[-2] == "SOUTH") or (result[-1] == "SOUTH" and result[-2] == "NORTH") or (result[-1] == "EAST" and result[-2] == "WEST") or (result[-1] == "WEST" and result[-2] == "EAST")):
            del result[-2:]
    # if result == ["NORTH"] or result == ["SOUTH"] or result == ["EAST"] or result == ["WEST"]: del result[:]
    return result
            
if __name__ == '__main__':
    # unittest.main()
    a = ["NORTH", "SOUTH"]
    # del a[-1]
    # del a[-1]
    print(len(a))
   
   
'''
Something wrong with the last testcase in python version?

I passed other testcases except the last testcase. It is a **randomlise** testcase, only one 
'''