#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目地址：
https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python
'''

import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(delete_nth([20,37,20,21], 1), [20,37,21])
    def test2(self):self.assertEqual(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])
    # def test3(self):self.assertEqual(get_function([1, 4, 7, 10, 13]), "f(x) = 3x + 1", "Nope! Try again.")



def delete_nth(order,max_e):
    result = []
    for number in order:
        if result.count(number) < max_e:
            result.append(number)
    return result
        

if __name__ == '__main__':
    unittest.main()



    
'''
参考解法：

'''