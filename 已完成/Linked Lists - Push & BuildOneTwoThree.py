#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Linked Lists - Push & BuildOneTwoThree题目地址：http://www.codewars.com/kata/linked-lists-push-and-buildonetwothree/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(push(None, 1).data, 1, "Should be able to create a new linked list with push().")
    def test2(self):self.assertEqual(push(None, 1).next, None, "Should be able to create a new linked list with push().")
    def test3(self):self.assertEqual(push(Node(1), 2).data, 2, "Should be able to prepend a node to an existing node.")
    def test4(self):self.assertEqual(push(Node(1), 2).next.data, 1, "Should be able to prepend a node to an existing node.")
    def test5(self):self.assertEqual(build_one_two_three().data, 1, "First node should should have 1 as data.")
    def test6(self):self.assertEqual(build_one_two_three().next.data, 2, "First node should should have 1 as data.")
    def test7(self):self.assertEqual(build_one_two_three().next.next.data, 3, "Second node should should have 2 as data.")
    def test8(self):self.assertEqual(build_one_two_three().next.next.next, None, "Third node should should have 3 as data.")

    
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

if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：

'''