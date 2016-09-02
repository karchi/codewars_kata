#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Powers of 2题目地址：https://www.codewars.com/kata/57a083a57cb1f31db7000028/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
        
    def test1(self):self.assertEqual(powers_of_two(0), [1])
    def test2(self):self.assertEqual(powers_of_two(1), [1, 2])
    def test3(self):self.assertEqual(powers_of_two(4), [1, 2, 4, 8, 16])

def powers_of_two(n):
    return [2 ** i for i in range(n + 1)]
    
if __name__ == '__main__':
    unittest.main()

    
    



    
'''
参考解法：
def powers_of_two(n):
    return [1<<x for x in range(n + 1)]
'''