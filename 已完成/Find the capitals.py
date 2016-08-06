#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Find the capitals题目地址：http://www.codewars.com/kata/find-the-capitals-1/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual( capitals('CodEWaRs'), [0,3,4,6] )

def capitals(word):
    return [i for i in range(len(word)) if word[i].isupper()]
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def capitals(word):
    return [i for (i, c) in enumerate(word) if c.isupper()]
'''