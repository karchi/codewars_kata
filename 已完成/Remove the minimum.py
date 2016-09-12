#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Remove the minimum题目地址：https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]")
    def test2(self):self.assertEqual(remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]")
    def test3(self):self.assertEqual(remove_smallest([1, 2, 3, 1, 1]), [2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]")
    def test4(self):self.assertEqual(remove_smallest([]), [], "Wrong result for []")

    
def remove_smallest(numbers):
    if numbers:
        numbers.remove(min(numbers))
    return numbers
  
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：

'''