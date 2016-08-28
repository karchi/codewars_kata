#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Maximum Length Difference题目地址：https://www.codewars.com/kata/5663f5305102699bad000056/train/python
'''

import time
import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):
        s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
        s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
        self.assertEqual(mxdiflg(s1, s2), 13)


def mxdiflg(a1, a2):
    if a1 == [] or a2 == []:
        return -1
    a1 = list(map(len, a1))
    a2 = list(map(len, a2))
    return max(abs(max(a1) - min(a2)), abs(max(a2) - min(a1)))
    
    
if __name__ == '__main__':
    unittest.main()
    # print(hor_mirror("lVHt\nJVhv\nCSbg\nyeCt"))
    # print("\n")
    # print("yeCt\nCSbg\nJVhv\nlVHt")
    # 测试时间：
    # start = time.clock()
    # for i in range(100000):
        # b = filter_list([1,2,'aasf','1','123',123])
    # end = time.clock()
    # print(end - start)

    



    
'''
参考解法：
def mxdiflg(a1, a2):
    if a1 and a2:
        return max(abs(len(x) - len(y)) for x in a1 for y in a2)
    return -1
'''