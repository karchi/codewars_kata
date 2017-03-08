#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Remove String Spaces题目地址：https://www.codewars.com/kata/57eae20f5500ad98e50002c5/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'), '8j8mBliB8gimjB8B8jlB')
    def test2(self):self.assertEqual(no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'), '88Bifk8hB8BB8BBBB888chl8BhBfd')
    def test3(self):self.assertEqual(no_space('8aaaaa dddd r     '), '8aaaaaddddr')
    def test4(self):self.assertEqual(no_space('jfBm  gk lf8hg  88lbe8 '), 'jfBmgklf8hg88lbe8') 
    def test5(self):self.assertEqual(no_space('8j aam'), '8jaam')

    
def no_space(x):
    return "".join([i for i in list(x) if i is not " "])
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def no_space(x):
    return x.replace(' ' ,'')
'''