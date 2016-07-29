#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目地址：
https://www.codewars.com/kata/53368a47e38700bd8300030d/train/python
'''

import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]), 'Bart, Lisa, Maggie, Homer & Marge',
"Must work with many names")
    def test2(self):self.assertEqual(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]), 'Bart, Lisa & Maggie',
"Must work with many names")
    def test3(self):self.assertEqual(namelist([{'name': 'Bart'},{'name': 'Lisa'}]), 'Bart & Lisa', 
"Must work with two names")
    def test4(self):self.assertEqual(namelist([{'name': 'Bart'}]), 'Bart', "Wrong output for a single name")
    def test5(self):self.assertEqual(namelist([]), '', "Must work with no names")

def namelist(names):
    result = ""
    if len(names) >= 3:
        for items in names[0:-2]:
            result = result + items.get("name") + ", "
        result = result + names[-2].get("name") + " & " + names[-1].get("name")
    elif len(names) == 2:
        result = result + names[-2].get("name") + " & " + names[-1].get("name")
    elif len(names) == 1:
        result = names[0].get("name")
    return result

if __name__ == '__main__':
    unittest.main()

    
    
    
    
    
'''
参考解法：
def namelist(names):
  return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ",1)[::-1]
'''