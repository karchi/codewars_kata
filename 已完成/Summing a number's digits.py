#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Summing a number's digits题目地址：https://www.codewars.com/kata/52f3149496de55aded000410/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(sumDigits(10), 1)
    def test2(self):self.assertEqual(sumDigits(99), 18)
    def test3(self):self.assertEqual(sumDigits(-32), 5)

def sumDigits(number):
    return sum([int(string) for string in str(number) if string.isdigit()])
    
if __name__ == '__main__':
    unittest.main()

    

    



    
'''
参考解法：
def sumDigits(number):
    return sum(int(d) for d in str(abs(number)))
'''