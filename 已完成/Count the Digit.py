#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Count the Digit题目地址：https://www.codewars.com/kata/count-the-digit/train/python
'''

import time
import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(nb_dig(5750, 0), 4700)
    def test2(self):self.assertEqual(nb_dig(11011, 2), 9481)
    def test3(self):self.assertEqual(nb_dig(12224, 8), 7733)
    def test4(self):self.assertEqual(nb_dig(11549, 1), 11905)

def nb_dig(n, d):
    pow = lambda x: x**2
    return "".join(map(str, map(pow, range(n+1)))).count(str(d))
    
if __name__ == '__main__':
    unittest.main()
    
    # 测试时间：
    # start = time.clock()
    # for i in range(100000):
        # a = sum_pairs([20, -13, 40], -7)
        # b = sum_pairs([20, -13, 40, 23, 122, 492, 324, -245, 58, -132, -49, 942], -7)
    # end = time.clock()
    # print(end - start)

    


    

    
'''
参考解法：
def nb_dig(n, d):
    return "".join([str(k**2) for k in range(n+1)]).count(str(d))
'''