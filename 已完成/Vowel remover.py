#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Vowel remover题目地址：http://www.codewars.com/kata/5547929140907378f9000039/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(shortcut('hello'),'hll')
    
def shortcut( s ):
    return "".join([string for string in s if string not in "aeiou"])

    


    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：

'''