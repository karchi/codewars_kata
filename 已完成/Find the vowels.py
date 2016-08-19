#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Find the vowels题目地址：http://www.codewars.com/kata/5680781b6b7c2be860000036/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(vowel_indices("super"), [2,4])
    
def vowel_indices(word):
    return [i + 1 for i in range(len(word)) if word[i] in "aeiouyAEIOUY"]

if __name__ == '__main__':
    unittest.main()


    

    


    
'''
参考解法：
def vowel_indices(word):
    return [i for i,x in enumerate(word,1) if x.lower() in 'aeiouy']
'''