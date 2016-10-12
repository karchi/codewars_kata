#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Counting sheep题目地址：https://www.codewars.com/kata/54edbc7200b811e956000556/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.array1 = [True,  True,  True,False,True,  True,  True,  True ,True,  False, True,  False,True,  False, False, True ,True,  True,  True,  True ,False, False, True,  True]
    def test1(self):self.assertEqual(count_sheeps(self.array1), 17)


def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)

    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：

'''