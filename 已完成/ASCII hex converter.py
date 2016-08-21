#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# ASCII hex converter题目地址：http://www.codewars.com/kata/52fea6fd158f0576b8000089/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.s="Look mom, no hands"
        self.h="4c6f6f6b206d6f6d2c206e6f2068616e6473"
        
    def test1(self):
        self.assertEqual(Converter.to_hex("Look mom, no hands"),"4c6f6f6b206d6f6d2c206e6f2068616e6473")
    def test2(self):
        self.assertEqual(Converter.to_ascii("4c6f6f6b206d6f6d2c206e6f2068616e6473"),"Look mom, no hands")
    def test3(self):self.assertEqual(Converter.to_hex(self.s),self.h)
    def test4(self):self.assertEqual(Converter.to_ascii(self.h),self.s)
    def test5(self):self.assertEqual(Converter.to_hex(Converter.to_ascii(self.h)),self.h)
    def test6(self):self.assertEqual(Converter.to_ascii(Converter.to_hex(self.s)),self.s)
 
    
class Converter():
    @staticmethod
    def to_ascii(h):
        res = ""
        for i in range(0,len(h),2):
            res += chr(int(h[i:i+2], 16))
        return res    

    @staticmethod
    def to_hex(s):
        return "".join([str(hex(ord(i)))[-2:] for i in s])
    

    
if __name__ == '__main__':
    unittest.main()

    


    



    
'''
参考解法：
class Converter():
    @staticmethod
    def to_ascii(h):
        return h.decode("hex")
    @staticmethod
    def to_hex(s):
        return s.encode("hex")
'''