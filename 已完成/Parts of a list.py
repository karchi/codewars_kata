#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Parts of a list题目地址：https://www.codewars.com/kata/56f3a1e899b386da78000732/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test2(self):self.assertEqual(partlist(["I", "wish", "I", "hadn't", "come"]),[("I", "wish I hadn't come"), ("I wish", "I hadn't come"), ("I wish I", "hadn't come"), ("I wish I hadn't", "come")])
    def test3(self):self.assertEqual(partlist(["cdIw", "tzIy", "xDu", "rThG"]), [("cdIw", "tzIy xDu rThG"), ("cdIw tzIy", "xDu rThG"), ("cdIw tzIy xDu", "rThG")])
    def test1(self):self.assertEqual(partlist(["vJQ", "anj", "mQDq", "sOZ"]),[("vJQ", "anj mQDq sOZ"), ("vJQ anj", "mQDq sOZ"), ("vJQ anj mQDq", "sOZ")])


    
def partlist(arr):
    res = []
    for i in range(1, len(arr)):
        res.append((" ".join(arr[:i])," ".join(arr[i:])))
    return res
    
if __name__ == '__main__':
    unittest.main()

    
    



    
'''
参考解法：
def partlist(arr):
    return [(' '.join(arr[:i]), ' '.join(arr[i:])) for i in range(1, len(arr))]
'''