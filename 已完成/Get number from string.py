#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Get number from string题目地址：https://www.codewars.com/kata/57a37f3cbb99449513000cd8/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.tests = [["1", 1],["123", 123],["this is number: 7",7],["$100 000 000",100000000],["hell5o wor6ld",56],["one1 two2 three3 four4 five5", 12345]]
        pass
    def test1(self):
        for t in self.tests:
            inp, exp = t
            self.assertEqual(get_number_from_string(inp), exp)

    
def get_number_from_string(string):
    return int("".join([str(i) for i in string if i.isdigit()]))
    
if __name__ == '__main__':
    unittest.main()

    



    
'''
参考解法：
def get_number_from_string(strng):
    return int(''.join(a for a in strng if a.isdigit()))
'''