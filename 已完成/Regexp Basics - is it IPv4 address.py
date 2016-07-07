#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目地址：
https://www.codewars.com/kata/567fe8b50c201947bc000056/train/python
'''

import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(ipv4_address(""), False)
    def test2(self):self.assertEqual(ipv4_address("127.0.0.1"), True)
    def test3(self):self.assertEqual(ipv4_address("0.0.0.0"), True)
    def test4(self):self.assertEqual(ipv4_address("255.255.255.255"), True)
    def test5(self):self.assertEqual(ipv4_address("10.256.30.40"), False)
    def test6(self):self.assertEqual(ipv4_address("10.20.030.40"), False)
    def test7(self):self.assertEqual(ipv4_address("127.0.1"), False)
    def test8(self):self.assertEqual(ipv4_address("127.0.0.0.1"), False)
    def test9(self):self.assertEqual(ipv4_address("..255.255"), False)
    def test10(self):self.assertEqual(ipv4_address("127.0.0.1\n"), False)
    def test11(self):self.assertEqual(ipv4_address("\n127.0.0.1"), False)
    def test12(self):self.assertEqual(ipv4_address(" 127.0.0.1"), False)
    def test13(self):self.assertEqual(ipv4_address("127.0.0.1 "), False)
    def test14(self):self.assertEqual(ipv4_address(" 127.0.0.1 "), False)


def ipv4_address(address):
    for x in list(set(address)):
        if x not in ".0123456789":
            return False
    new_address = address.split(".")
    if len(new_address) != 4:
        return False
    for x in new_address:
        if x == "" or (len(x) > 1 and x[0] == "0"):
            return False        
        elif int(x) > 255:
            return False
    return True
        

if __name__ == '__main__':
    unittest.main()

    
    

    
'''
参考解法：
def ipv4_address(address):
  max=address.split(".")
  if len(max)!=4:
    return False
  for i in max:
    if not i.isdigit():
      return False
    if len(i)>1 and i[0]=="0":
      return False
    if not 0<=int(i)<=255:
      return False
  return True
    
或：
import re
def ipv4_address(address):
    match = re.match(
        r"^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){4}$",
        address + "."
    )
    return bool(match)
'''