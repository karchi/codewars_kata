#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Mumbling题目地址：https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(accum("ZpglnRxqenU"), "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
    def test2(self):self.assertEqual(accum("NyffsGeyylB"), "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")
    def test3(self):self.assertEqual(accum("MjtkuBovqrU"), "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu")
    def test4(self):self.assertEqual(accum("EvidjUnokmM"), "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm")
    def test5(self):self.assertEqual(accum("HbideVbxncC"), "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc")
    def test6(self):self.assertEqual(accum("abcd"), "A-Bb-Ccc-Dddd")


def accum(s):
    number = 0
    res = ""
    for string in s:
        long_string = string.lower() * number
        res += "".join([string.upper(), long_string, "-"])
        number += 1
    return res[:-1]
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
'''