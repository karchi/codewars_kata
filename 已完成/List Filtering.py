#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# List Filtering题目地址：http://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
'''

import time
import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(filter_list([1,2,'a','b']),[1,2])
    def test2(self):self.assertEqual(filter_list([1,'a','b',0,15]),[1,0,15])
    def test3(self):self.assertEqual(filter_list([1,2,'aasf','1','123',123]),[1,2,123])
    # def test4(self):self.assertEqual(find_even_index(range(1,100)),-1)
    # def test5(self):self.assertEqual(find_even_index([0,0,0,0,0]),0)

'''
def filter_list(l):
    result = []
    for item in l:
        if type(item) is int:
            result.append(item)
    return result
'''

def filter_list(l):
    return [item for item in l if type(item) is int]
    
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
def filter_list(l):
    return [i for i in l if not isinstance(i, str)]
'''