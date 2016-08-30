#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Square Every Digit题目地址：http://www.codewars.com/kata/546e2562b03326a88e000020/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
        
    def test1(self):self.assertEqual(square_digits(9119), 811181)

    
def square_digits(num):
    res = ""
    for string in str(num):
        res += str(int(string)**2)
    return int(res)
    
if __name__ == '__main__':
    unittest.main()

    

    



    
'''
参考解法：

'''