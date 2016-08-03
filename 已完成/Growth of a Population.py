#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Growth of a Population题目地址：https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python
'''

import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(nb_year(1500, 5, 100, 5000), 15)
    def test2(self):self.assertEqual(nb_year(1500000, 2.5, 10000, 2000000), 10)
    def test3(self):self.assertEqual(nb_year(1500, 5, 100, 5000), 15)

def nb_year(p0, percent, aug, p):
    year = 0
    while p0 < p:
        p0 = int(p0 * (1 + percent / 100)) + aug
        year += 1
    return year
        
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：

'''