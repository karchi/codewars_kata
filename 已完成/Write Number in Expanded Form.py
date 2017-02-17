#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Write Number in Expanded Form题目地址：https://www.codewars.com/kata/write-number-in-expanded-form
'''

import unittest

class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(expanded_form(40), '40')
    def test2(self):self.assertEqual(expanded_form(12), '10 + 2')
    def test3(self):self.assertEqual(expanded_form(42), '40 + 2')
    def test4(self):self.assertEqual(expanded_form(70304), '70000 + 300 + 4')
    def test5(self):self.assertEqual(expanded_form(3), '3')


    
def expanded_form(num):
    num = list(str(num))
    zero = len(num) - 1
    res = []
    for i in num:
        if i != "0":
            res.append(i + zero * "0")
        zero -= 1
    return " + ".join(res)
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def expanded_form(num):
    return " + ".join([str(int(d) * 10**p) for p, d in enumerate(str(num)[::-1]) if d != "0"][::-1])
    
    
def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')
'''