#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目地址：
https://www.codewars.com/kata/5476f4ca03810c0fc0000098/train/python
'''

import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(get_function([0, 1, 2, 3, 4]), "f(x) = x", "Nope! Try again.");
    def test2(self):self.assertEqual(get_function([0, 3, 6, 9, 12]), "f(x) = 3x", "Nope! Try again.");
    def test3(self):self.assertEqual(get_function([1, 4, 7, 10, 13]), "f(x) = 3x + 1", "Nope! Try again.");



def get_function(sequence):
    result = ""
    m = sequence[0]
    n = sequence[1] - m
    for x in range(2,5):
        if n * x + m != sequence[x]:
            result = "Non-linear sequence"
            return result 
    if n == 0:
        n_part = ""
    elif n == 1:
        n_part = "x"
    elif n == -1:
        n_part = "-x"
    else:
        n_part = str(n) + "x"
    if m == 0:
        m_part = ""
    elif n != 0:
        if m > 0:
            m_part = " + " + str(m)
        else:
            m_part = " - " + str(-m)
    else:
        if m > 0:
            m_part = str(m)
        else:
            m_part = str(-m)
    result = "f(x) = " + n_part + m_part
    return result
        

if __name__ == '__main__':
    unittest.main()



    
'''
参考解法：
def get_function(sequence):
    m = sequence[0]
    n = sequence[1] - m
    if [n*x+m for x in range(5)] != sequence:
        return 'Non-linear sequence'
    return 'f(x) = {}'.format(format_function(n, m))
    
def format_function(n, m):
    if not n:
        return m
    n_string = '{}{}x'.format('-' if n < 0 else '', abs(n) if abs(n) != 1 else '')
    m_string = ' {} {}'.format('+' if m > 0 else '-', abs(m)) if m else ''
    return ''.join([n_string, m_string])
'''