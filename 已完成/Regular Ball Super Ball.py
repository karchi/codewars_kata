#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Regular Ball Super Ball题目地址：http://www.codewars.com/kata/53f0f358b9cb376eca001079/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(Ball().ball_type, "regular")
    def test2(self):self.assertEqual(Ball("super").ball_type, "super")

    
class Ball(object):
    def __init__(self, *ball_type):
        self.ball_type = ball_type[0] if ball_type else "regular"

    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type
'''