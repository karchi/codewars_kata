#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Multiplication Tables题目地址：http://www.codewars.com/kata/multiplication-tables
'''

import unittest

class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(multiplication_table(2,2), [[1,2],[2,4]])
    def test2(self):self.assertEqual(multiplication_table(3,3), [[1,2,3],[2,4,6],[3,6,9]])

def multiplication_table(row,col):
    result = []
    for i in range(1, row + 1):
        result.append([j * i for j in range(1, col + 1)])
    return result
            
if __name__ == '__main__':
    unittest.main()


    
    



    
'''
参考解法：
def multiplication_table(row,col):
    return [[(i+1)*(j+1) for j in range(col)] for i in range(row)]
'''