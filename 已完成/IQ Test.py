#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目地址：
https://www.codewars.com/kata/552c028c030765286c00007d/train/python
'''

import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(iq_test("2 4 7 8 10"),3)
    def test2(self):self.assertEqual(iq_test("1 2 2"), 1)
    def test3(self):self.assertEqual(iq_test("1 2 1 1"), 2)

def iq_test(numbers):
    int_numbers = []
    for string in numbers.split():
        int_numbers.append(int(string)%2)
    if sum(int_numbers) > 1:
        result = int_numbers.index(0)+1
    else:
        result = int_numbers.index(1)+1
    return result

if __name__ == '__main__':
    unittest.main()

