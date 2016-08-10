#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Leonardo Dicaprio and Oscars题目地址：http://www.codewars.com/kata/56d49587df52101de70011e4/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(leo(88),"Leo finally won the oscar! Leo is happy")

def leo(oscar):
    res = ""
    if oscar == 88:
        res = "Leo finally won the oscar! Leo is happy"
    elif oscar == 86:
        res = "Not even for Wolf of wallstreet?!"
    elif oscar < 88:
        res = "When will you give Leo an Oscar?"
    else:
        res = "Leo got one already!"
    return res
            
        
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
def leo(oscar):
    if oscar <= 88:
        return {86: 'Not even for Wolf of wallstreet?!',
                88: 'Leo finally won the oscar! Leo is happy'}.get(
            oscar, 'When will you give Leo an Oscar?')
    return 'Leo got one already!'
'''