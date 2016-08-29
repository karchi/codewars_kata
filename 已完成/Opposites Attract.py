#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Opposites Attract题目地址：http://www.codewars.com/kata/555086d53eac039a2a000083/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        # self.quote = "How can mirrors be real if our eyes aren't real"
        pass
        
    def test1(self):self.assertEqual(lovefunc(1,4), True)
    def test2(self):self.assertEqual(lovefunc(2,2), False)
    def test3(self):self.assertEqual(lovefunc(0,1), True)
    def test4(self):self.assertEqual(lovefunc(0,0), False)
    
def lovefunc( flower1, flower2 ):
    return (flower1 + flower2) % 2 == 1
    
if __name__ == '__main__':
    unittest.main()

    
    

    



    
'''
参考解法：
def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2
    
解法2：
def lovefunc(flower1, flower2):
    return flower1 % 2 != flower2 % 2
'''