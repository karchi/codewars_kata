#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Printer Errors题目地址：http://www.codewars.com/kata/56541980fa08ab47a0000040/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def test1(self):
        s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
        self.assertEqual(printer_error(s), "3/56")

def printer_error(s):
    return str(len([i for i in s if ord(i) > ord("m")])) + "/" + str(len(s))
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def printer_error(s):
    import re
    return str(len(re.findall('[n-z]', s))) + "/" + str(len(s))
'''