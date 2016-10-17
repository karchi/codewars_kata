#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Compare Strings by Sum of Chars题目地址：https://www.codewars.com/kata/576bb3c4b1abc497ec000065/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(compare("AD", "BC"), True, "\'AD\' vs \'BC\'")
    def test2(self):self.assertEqual(compare("AD", "DD"), False, "\'AD\' vs \'DD\'")
    def test3(self):self.assertEqual(compare("gf", "FG"), True, "\'gf\' vs \'FG\'")
    def test4(self):self.assertEqual(compare("Ad", "DD"), False, "\'Ad\' vs \'DD\'")
    def test5(self):self.assertEqual(compare("zz1", ""), True, "\'zz1\' vs \'\'")
    def test6(self):self.assertEqual(compare("ZzZz", "ffPFF"), True, "\'ZzZz\' vs \'ffPFF\'")
    def test7(self):self.assertEqual(compare(None, ""), True, "\'<null>\' vs \'\'")
    def test8(self):self.assertEqual(compare("!!", "7476"), True, "\'!!\' vs \'7476\'")
    def test9(self):self.assertEqual(compare("kl", "lz"), False, "\'kl\' vs \'lz\'")

    
def compare(s1,s2):
    sum1 = sum2 = 0
    if type(s1) == str and s1.isalpha():
        for i in s1.upper():
            sum1 += ord(i)
    if type(s2) == str and s2.isalpha():
        for i in s2.upper():
            sum2 += ord(i)
    return sum1 == sum2
    
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def compare(s1,s2):
    a,b =  (sum(ord(c) for c in s.upper()) for s in (s1, s2) if s.isalpha())
    return a == b
'''