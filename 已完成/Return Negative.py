#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Return Negative题目地址：https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(make_negative(42),-42)
    def test2(self):self.assertEqual(make_negative(-9),-9)
    def test3(self):self.assertEqual(make_negative(0),0)


def make_negative( number ):
    return number if number <= 0 else -number
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def make_negative( number ):
    return -abs(number)
'''