#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Removing Elements题目地址：https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(remove_every_other(['Hello', 'Goodbye', 'Hello Again']),['Hello', 'Hello Again'])
    def test2(self):self.assertEqual(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),[1, 3, 5, 7, 9])
    def test3(self):self.assertEqual(remove_every_other([[1, 2]]), [[1, 2]])
    def test4(self):self.assertEqual(remove_every_other([['Goodbye'], {'Great': 'Job'}]),[['Goodbye']])


def remove_every_other(my_list):
    for i in range(len(my_list)-1, 0, -1):
        if i % 2:
            my_list.pop(i)
    return my_list
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def remove_every_other(my_list):
    return my_list[::2]
    
解法2：
def remove_every_other(my_list):
    return [ my_list[i] for i in range(0,len(my_list),2)]
'''