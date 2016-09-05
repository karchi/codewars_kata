#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Convert boolean values to strings 'Yes' or 'No'.题目地址：https://www.codewars.com/kata/53369039d7ab3ac506000467/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(bool_to_word(True), 'Yes')
    def test2(self):self.assertEqual(bool_to_word(False), 'No')

def bool_to_word(bool):
    return "Yes" if bool else "No"
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：

'''