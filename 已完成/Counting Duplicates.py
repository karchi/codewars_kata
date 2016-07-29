#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目地址：
https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
'''

import time
import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(duplicate_count("abcde"), 0)
    def test2(self):self.assertEqual(duplicate_count("abcdea"), 1)
    def test3(self):self.assertEqual(duplicate_count("indivisibility"), 1)

def duplicate_count(text):
    text = text.lower()
    text_one = list(set(text))
    result = 0
    for item in text_one:
        if text.count(item) > 1:
            result +=1
    return result

    
'''
# 另一种写法：
def duplicate_count(text):
    text = text.lower()
    text_one = list(set(text))
    return len([item for item in text_one if text.count(item) > 1])
'''

if __name__ == '__main__':
    unittest.main()
    
    '''
    # 测试时间：
    start = time.clock()
    for i in range(100000):
        a = duplicate_count("abcdfegixwsx")
    end = time.clock()
    print(end - start)
    '''

    



    
'''
参考解法：
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
'''