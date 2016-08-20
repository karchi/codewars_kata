#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Linked Lists - Push & BuildOneTwoThree题目地址：http://www.codewars.com/kata/linked-lists-push-and-buildonetwothree/train/python
# Linked Lists - Length & Count题目地址：http://www.codewars.com/kata/55beec7dd347078289000021/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(length(None), 0, "Length of null list should be zero.")
    def test2(self):self.assertEqual(length(Node(99)), 1, "Length of single node list should be one.")
    def test3(self):self.assertEqual(length(build_one_two_three()), 3, "Length of the three node list should be three.")
    def test4(self):self.assertEqual(count(build_one_two_three(), 1), 1, "list should only contain one 1.")
    def test5(self):self.assertEqual(count(build_one_two_three(), 2), 1, "list should only contain one 2.")
    def test6(self):self.assertEqual(count(build_one_two_three(), 99), 0, "list should return zero for integer not found in list.")
    def test7(self):self.assertEqual(count(None, 1), 0, "null list should always return count of zero.")
    def test8(self):self.assertEqual(length(build_one_two_three()), 3, "Length of the three node list should be three.")

# 第一题
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def push(head, data):
    node = Node(data)
    node.next = head
    return node
  
def build_one_two_three():
    return push(push(push(None,3),2),1)
    
# 第二题：  
def length(node):
    res = 0
    thisNode = node
    while thisNode != None:
        res += 1
        thisNode = thisNode.next
    return res
  
def count(node, data):
    res = 0
    thisNode = node
    while thisNode != None:
        if thisNode.data == data:
            res += 1
        thisNode = thisNode.next
    return res

    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    leng = 0
    while node:
        leng += 1
        node = node.next
    return leng
  
def count(node, data):
    c = 0
    while node:
        if node.data==data:
            c += 1
        node = node.next
    return c
'''