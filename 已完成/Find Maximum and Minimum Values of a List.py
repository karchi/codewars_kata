#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Find Maximum and Minimum Values of a List题目地址：http://www.codewars.com/kata/577a98a6ae28071780000989/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(min([-52, 56, 30, 29, -54, 0, -110]), -110)
    def test2(self):self.assertEqual(min([42, 54, 65, 87, 0]), 0)
    def test3(self):self.assertEqual(min([1, 2, 3, 4, 5, 10]), 1)
    def test4(self):self.assertEqual(min([-1, -2, -3, -4, -5, -10]), -10)
    def test5(self):self.assertEqual(max([-52, 56, 30, 29, -54, 0, -110]), 56)
    def test6(self):self.assertEqual(min([9]), 9)
    def test7(self):self.assertEqual(max([4,6,2,1,9,63,-134,566]), 566)
    def test8(self):self.assertEqual(max([5]), 5)
    def test9(self):self.assertEqual(max([534,43,2,1,3,4,5,5,443,443,555,555]), 555)
    def test10(self):self.assertEqual(max([9]), 9)

def min(arr):
    # return min(arr)
    return sorted(arr)[0]

def max(arr):
    # return max(arr)
    return sorted(arr)[-1]
            
        
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
pass

解法2：
class assert_equals():
    def min(arr):
        return min(arr)
    def max(arr):
        return max(arr)
        
解法3：
def max(arr):
  temp = __builtins__.max(arr) ##builtin used because naming conflict with func
  return temp
def min(arr):
  temp = __builtins__.min(arr)
  return temp
  
解法4：
import builtins
def min(arr):
    return builtins.min(arr)
def max(arr):
    return builtins.max(arr)
'''