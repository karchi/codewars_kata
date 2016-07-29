#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Two to One题目地址：http://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python
'''

import time
import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(longest("aretheyhere", "yestheyarehere"), "aehrsty")
    def test2(self):self.assertEqual(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
    def test3(self):self.assertEqual(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")


def longest(s1, s2):
    return "".join([char for char in "abcdefghijklmnopqrstuvwxyz" if char in s1 + s2])
    
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
def longest(s1, s2):
    return ''.join(sorted((set(s1+s2))))
'''