#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Descending Order题目地址：https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(Descending_Order(0), 0)
    def test2(self):self.assertEqual(Descending_Order(15), 51)
    def test3(self):self.assertEqual(Descending_Order(123456789), 987654321)


def Descending_Order(num):
    return int("".join(sorted(str(num), reverse = True)))

    
if __name__ == '__main__':
    unittest.main()
    # a = {'jjjjj': 'jjjjj'}
    # b = "asd"
    # print(type(b))
    # reverse_words(a)
    # for i in range(0,len(a),2):
        # print(a[i:i+2])
        # print(a)
    # print("yeCt\nCSbg\nJVhv\nlVHt")
    # 测试时间：
    # start = time.clock()
    # for i in range(100000):
        # b = sort_array([5, 3, 2, 8, 1, 4])
    # end = time.clock()
    # print(end - start) #2.04

    



    
'''
参考解法：

'''