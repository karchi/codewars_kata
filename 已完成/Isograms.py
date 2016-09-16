#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Isograms题目地址：https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(is_isogram("Dermatoglyphics"), True )
    def test2(self):self.assertEqual(is_isogram("isogram"), True )
    def test3(self):self.assertEqual(is_isogram("aba"), False, "same chars may not be adjacent" )
    def test4(self):self.assertEqual(is_isogram("moOse"), False, "same chars may not be same case" )
    def test5(self):self.assertEqual(is_isogram("isIsogram"), False )
    def test6(self):self.assertEqual(is_isogram(""), True, "an empty string is a valid isogram" )


def is_isogram(string):
    string = string.upper()
    setString = set(string)
    return True if len(string) == len(setString) else False

    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def is_isogram(string):
    return len(string) == len(set(string.lower()))
'''