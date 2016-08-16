#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Recursive reverse string题目地址：http://www.codewars.com/kata/536a9f94021a76ef0f00052f/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual("hello world", reverse("dlrow olleh"))


def reverse(str):
    if len(str) == 1:
        return str
    else:
        return str[-1] + reverse(str[:-1])
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def reverse(str):
  return str[-1] + reverse(str[:-1]) if len(str) > 1 else str
'''