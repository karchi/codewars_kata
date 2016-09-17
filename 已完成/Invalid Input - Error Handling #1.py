#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Invalid Input - Error Handling #1题目地址：https://www.codewars.com/kata/55e6125ad777b540d9000042/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(get_count('Test'),{"vowels":1,"consonants":3},'Should return 1 vowel and 3 consonants')
    def test2(self):self.assertEqual(get_count('Here is some text'),{"vowels":6,"consonants":8},'Should return 6 vowel and 8 consonants')
    def test3(self):self.assertEqual(get_count('To be a Codewarrior or not to be'),{"vowels":12,"consonants":13},'Should return 12 vowel and 13 consonants')
    def test4(self):self.assertEqual(get_count('To Kata or not to Kata'),{"vowels":8,"consonants":9},'Should return 8 vowel and 9 consonants')
    def test5(self):self.assertEqual(get_count('aeiou'),{"vowels":5,"consonants":0},'Should return 5 vowel and 0 consonants')
    def test6(self):self.assertEqual(get_count('TEst'),{"vowels":1,"consonants":3},'Should return 1 vowel and 3 consonants')
    def test7(self):self.assertEqual(get_count('HEre Is sOme text'),{"vowels":6,"consonants":8},'Should return 6 vowel and 8 consonants')
    def test8(self):self.assertEqual(get_count(),{"vowels":0,"consonants":0},'Should return 0 vowel and 0 consonants')
    def test9(self):self.assertEqual(get_count(['To Kata or not to Kata']),{"vowels":0,"consonants":0},'Should return 0 vowel and 0 consonants')
    def test9(self):self.assertEqual(get_count(None),{"vowels":0,"consonants":0},'Should return 5 vowel and 0 consonants')


def get_count(words = None):
    res = {"vowels":0, "consonants":0}
    if type(words) == str:
        for i in words:
            if i.isalpha():
                res["consonants"] += 1
                if i in "aeiouAEIOU":
                    res["vowels"] += 1
        res["consonants"] -= res["vowels"]
    return res
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def get_count(words=''):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    v,c = 0,0
    try:
        for l in words.lower():
            if l in vowels: v += 1
            elif l in consonants: c += 1
        return {"vowels":v,"consonants":c}
    except:
        return {"vowels":0,"consonants":0}
        
解法2：
def get_count(words=None):
    ret = {"vowels": 0, "consonants": 0}
    if words and isinstance(words, str):
        for char in words.lower():
            if char in 'aeiouy':
                ret["vowels"] += 1
            elif char.isalpha():
                ret["consonants"] += 1
    return ret
'''