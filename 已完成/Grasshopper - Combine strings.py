#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Grasshopper - Combine strings题目地址：https://www.codewars.com/kata/55f73f66d160f1f1db000059/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(combine_names("James", "Stevens"), "James Stevens")
    def test2(self):self.assertEqual(combine_names("Davy", "Back"), "Davy Back")
    def test3(self):self.assertEqual(combine_names("Arthur", "Dent"), "Arthur Dent")
        
def combine_names(s1, s2):
    return " ".join([s1, s2])
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def combine_names(first, last):
    return first + " " + last

解法2：
def combine_names(*args):
    return ' '.join(args)
'''