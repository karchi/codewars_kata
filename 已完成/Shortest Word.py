#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Shortest Word题目地址：https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
    def test2(self):self.assertEqual(find_short("turns out random test cases are easier than writing out basic ones"), 3)
    def test3(self):self.assertEqual(find_short("lets talk about javascript the best language"), 3)
    def test4(self):self.assertEqual(find_short("i want to travel the world writing code one day"), 1)
    def test5(self):self.assertEqual(find_short("Lets all go on holiday somewhere very cold"), 2)

def find_short(s):
    return min([len(word) for word in s.split(" ")])
    
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：

'''