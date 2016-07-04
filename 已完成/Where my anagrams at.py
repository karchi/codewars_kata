#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
    def test2(self):self.assertEqual(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
    # def test3(self):self.assertEqual(0, count_change(11, [5,7]))
    # def test4(self):self.assertEqual(countBits(10), 2)
    # def test5(self):self.assertEqual(lowercase_count("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), 0)
    # def test6(self):self.assertEqual(lowercase_count("abcdefghijklmnopqrstuvwxyz"), 26)

def anagrams(word, words):
    result = []
    for strings in words:
        if len(word) != len(strings):words.remove(strings)
    new_words = []
    for strings in words:
        new_words.append(strings)
    dict = {}
    for char in word:
        dict[char] = word.count(char)
    for n in range(len(words)):
        for k in dict:
            if dict[k] != words[n].count(k):
                new_words.remove(words[n])
                break
    return new_words

if __name__ == '__main__':
    unittest.main()

    
    
    
    
    
    
'''
# http://www.codewars.com/kata/523a86aa4230ebb5420001e1/solutions/python
# 最佳答案之一：
def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]
'''