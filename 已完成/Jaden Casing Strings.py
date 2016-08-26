#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Jaden Casing Strings题目地址：http://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.quote = "How can mirrors be real if our eyes aren't real"
        pass
        
    def test1(self):self.assertEqual(toJadenCase(self.quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")

    
def toJadenCase(string):
    res = []
    wordList = string.split()
    for word in wordList:
        res.append(word.capitalize())
    return " ".join(res)

    
if __name__ == '__main__':
    unittest.main()

    



    
'''
参考解法：
def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())
    
解法2:
import string
def toJadenCase(string1):
    return string.capwords(string1)
'''