#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Sort array by string length题目地址：https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.tests = [[["i", "to", "beg", "life"], ["beg", "life", "i", "to"]],    [["", "pizza", "brains", "moderately"], ["", "moderately", "brains", "pizza"]],    [["short", "longer", "longest"], ["longer", "longest", "short"]],    [["a", "of", "dog", "food"], ["dog", "food", "a", "of"]],    [["", "bees", "eloquent", "dictionary"], ["", "dictionary", "eloquent", "bees"]],    [["a short sentence", "a longer sentence", "the longest sentence"], ["a longer sentence", "the longest sentence", "a short sentence"]],]
        pass
        
    def test1(self):
        for exp, inp in self.tests:
            self.assertEqual(sort_by_length(inp), exp)


    
def sort_by_length(arr):
    arrDict = {}
    for items in arr:
        arrDict[len(items)] = items
    return [j for k,j in sorted(arrDict.items(), key = lambda arrDict:arrDict[0])]
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def sort_by_length(arr):
    return sorted(arr, key=len)
'''