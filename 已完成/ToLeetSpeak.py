#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# ToLeetSpeak题目地址：https://www.codewars.com/kata/57c1ab3949324c321600013f/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(to_leet_speak("LEET"), "1337")
    def test2(self):self.assertEqual(to_leet_speak("CODEWARS"), "(0D3W@R$")
    def test3(self):self.assertEqual(to_leet_speak("HELLO WORLD"), "#3110 W0R1D")
    def test4(self):self.assertEqual(to_leet_speak("LOREM IPSUM DOLOR SIT AMET"), "10R3M !P$UM D010R $!7 @M37")
    def test5(self):self.assertEqual(to_leet_speak("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"), "7#3 QU!(K 8R0WN F0X JUMP$ 0V3R 7#3 1@2Y D06")


def to_leet_speak(str):
    alphabet = {"A" : '@', "B": '8',  "C" : '(',  "D" : 'D',  "E" : '3',  "F" : 'F',  "G" : '6',  "H" : '#',  "I" : '!',  "J" : 'J',  "K" : 'K',  "L" : '1',  "M" : 'M',  "N" : 'N',  "O" : '0',  "P" : 'P',  "Q" : 'Q',  "R" : 'R',  "S" : '$',  "T" : '7',  "U" : 'U',  "V" : 'V',  "W" : 'W',  "X" : 'X',  "Y" : 'Y',  "Z" : '2'}
    res = []
    for i in range(len(str)):
        if str[i] in alphabet:
            res.append(alphabet[str[i]])
        else:
            res.append(str[i])
    return "".join(res)
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def to_leet_speak(str):
    leet = {'A' : '@','B' : '8','C' : '(','D' : 'D','E' : '3','F' : 'F','G' : '6','H' : '#','I' : '!','J' : 'J','K' : 'K','L' : '1','M' : 'M','N' : 'N','O' : '0','P' : 'P','Q' : 'Q','R' : 'R','S' : '$','T' : '7','U' : 'U','V' : 'V','W' : 'W','X' : 'X','Y' : 'Y','Z' : '2'}
    for i in leet:
        str = str.replace(i, leet[i])
    return str
'''