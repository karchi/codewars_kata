#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目地址：
https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python
'''

import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(tickets([25, 25, 50]), "YES")
    def test2(self):self.assertEqual(tickets([25, 100]), "NO")



def tickets(people):
    change = []
    result = "YES"
    for ticket in people:
        if ticket == 25:
            change.append(ticket)
            continue
        elif ticket == 50:
            if 25 in change:
                change.remove(25)
                change.append(ticket)
            else:
                result = "NO"
                break
            continue
        elif ticket == 100:
            if 50 in change and 25 in change:
                change.remove(50)
                change.remove(25)
            elif change.count(25) >= 3:
                for _ in range(3):
                    change.remove(25)
            else:
                result = "NO"
                break
    return result

if __name__ == '__main__':
    unittest.main()
    


    
'''
参考解法：

'''