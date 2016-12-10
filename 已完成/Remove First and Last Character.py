#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Remove First and Last Character题目地址：https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test2(self):self.assertEqual(remove_char('eloquent'), 'loquen')
    def test3(self):self.assertEqual(remove_char('country'), 'ountr')
    def test4(self):self.assertEqual(remove_char('person'), 'erso')
    def test5(self):self.assertEqual(remove_char('place'), 'lac')
    def test6(self):self.assertEqual(remove_char('ok'), '')

    
def remove_char(s):
    return s[1:-1]
    
if __name__ == '__main__':
    unittest.main()



    
'''
参考解法：

'''