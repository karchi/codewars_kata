#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Count the Monkeys题目地址：http://www.codewars.com/kata/count-the-monkeys/train/python
'''

import time
import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(monkey_count(5), [1, 2, 3, 4, 5])
    def test2(self):self.assertEqual(monkey_count(3), [1, 2, 3])
    def test3(self):self.assertEqual(monkey_count(9), [1, 2, 3, 4, 5, 6, 7, 8, 9])
    def test4(self):self.assertEqual(monkey_count(10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test5(self):self.assertEqual(monkey_count(20), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

def monkey_count(n):
    return list(range(1,n+1))
    
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

'''