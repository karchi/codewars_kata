#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Data Reverse题目地址：https://www.codewars.com/kata/569d488d61b812a0f7000015/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
        self.data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
        self.data3 = [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]
        self.data4 = [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]
    def test1(self):self.assertEqual(data_reverse(self.data1), self.data2)
    def test2(self):self.assertEqual(data_reverse(self.data3), self.data4)


def data_reverse(data):
    res = []
    while data:
        for item in data[-8:]:
            res.append(item)
        data = data[:-8]
    return res
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def data_reverse(data):
    res = []
    for i in range(len(data)-8, -1, -8):
        res.extend(data[i:i+8])
    return res
'''