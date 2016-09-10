#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Moves in squared strings (I)题目地址：http://www.codewars.com/kata/moves-in-squared-strings-i
'''

import time
import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(oper(vert_mirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"), "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw") 
    def test2(self):self.assertEqual(oper(vert_mirror, "IzOTWE\nkkbeCM\nWuzZxM\nvDddJw\njiJyHF\nPVHfSx"), "EWTOzI\nMCebkk\nMxZzuW\nwJddDv\nFHyJij\nxSfHVP")
    def test3(self):self.assertEqual(oper(hor_mirror, "lVHt\nJVhv\nCSbg\nyeCt"), "yeCt\nCSbg\nJVhv\nlVHt")
    def test4(self):self.assertEqual(oper(hor_mirror, "njMK\ndbrZ\nLPKo\ncEYz"), "cEYz\nLPKo\ndbrZ\nnjMK")

def vert_mirror(strng):
    splitStrng = strng.split("\n")
    return "\n".join([item[::-1] for item in splitStrng])
    
def hor_mirror(strng):
    splitStrng = strng.split("\n")
    splitStrng.reverse()
    return "\n".join(splitStrng)

def oper(fct, s):
    return fct(s)
    
    
if __name__ == '__main__':
    unittest.main()

    # 测试时间：
    # start = time.clock()
    # for i in range(100000):
        # b = filter_list([1,2,'aasf','1','123',123])
    # end = time.clock()
    # print(end - start)

    



    
'''
参考解法：
def vert_mirror(s):
    return "\n".join(line[::-1] for line in s.split("\n"))
def hor_mirror(s):
    return "\n".join(s.split("\n")[::-1])
def oper(fct, s):
    return fct(s)
    
解法2：
def vert_mirror(strng):
    return map(reversed, strng)
def hor_mirror(strng):
    return reversed(strng)
def oper(fct, s):
    return '\n'.join(map(''.join, fct(s.split('\n'))))
'''