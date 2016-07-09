#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目地址：
https://www.codewars.com/kata/51675d17e0c1bed195000001/train/python
'''

import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(solution("12345"),12345)
    def test2(self):self.assertEqual(solution("123456"),23456)
    def test3(self):self.assertEqual(solution("895432123"),95432)
    def test4(self):self.assertEqual(solution("8245123199999"),99999)
    # def test5(self):self.assertEqual(ipv4_address("10.256.30.40"), False)
    # def test6(self):self.assertEqual(ipv4_address("10.20.030.40"), False)
    # def test7(self):self.assertEqual(ipv4_address("127.0.1"), False)

def solution(digits):
    max = 0
    for i in range(len(digits[:-4])):
        cam = int(digits[i:i+5])
        if cam > max:
            max = cam
    return max


if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def solution(dd):
    return max(int(dd[i:i+5]) for i in range(len(dd) - 4))
    
另一种解法：  
def solution(d):
  for x in '9876543210':
    for y in '9876543210':
      for z in '9876543210':
        for a in '9876543210':
          for b in '9876543210':
            if d.find(x+y+z+a+b) != -1:
              return int(x+y+z+a+b)
'''