#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Make them bark题目地址：https://www.codewars.com/kata/5535572c1de94ba2db0000f6/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.apollo = Dog('Apollo', 'Dobermann', 'male', '4')
        self.zeus = Dog('Zeus', 'Dobermann', 'male', '4')
        pass
        
    def test1(self):self.assertEqual(self.apollo.bark(), 'Woof!')
    def test2(self):self.assertEqual(self.zeus.bark(), 'Woof!')

'''   
class Dog(object):
    def __init__(self, name, breed, sex, age):
        self.name  = name
        self.breed = breed
        self.sex   = sex
        self.age   = age
'''

        
def bark(self):
    return "Woof!"

Dog.bark = bark  # 方法的动态特性
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
Dog.bark = lambda self: "Woof!"
'''