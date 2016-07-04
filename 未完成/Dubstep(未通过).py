#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目地址：
https://www.codewars.com/kata/551dc350bf4e526099000ae5/train/python
'''

import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(song_decoder("AWUBBWUBC"), "A B C","WUB should be replaced by 1 space")
    def test2(self):self.assertEqual(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C","multiples WUB should be replaced by only 1 space")
    def test3(self):self.assertEqual(song_decoder("WUBAWUBBWUBCWUB"), "A B C","heading or trailing spaces should be removed")
    # def test4(self):self.assertEqual(countBits(10), 2)
    # def test5(self):self.assertEqual(lowercase_count("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), 0)
    # def test6(self):self.assertEqual(lowercase_count("abcdefghijklmnopqrstuvwxyz"), 26)

def song_decoder(song):
    song = song.replace("WUB"," ")
    while song.find("  ") > 0:
        song = song.replace("  "," ")
    while song[0] == " ":
        song = song[1:]
    while song[-1] == " ":
        song = song[:-1]
    return song

if __name__ == '__main__':
    unittest.main()
