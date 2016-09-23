#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Vowel Count题目地址：https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(getCount("abracadabra"), 5)


def getCount(inputStr):
    num_vowels = 0
    num_vowels += len([i for i in inputStr if i in "aeiouAEIOU"])
    return num_vowels
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")
'''