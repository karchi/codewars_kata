#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Linked Lists - Push & BuildOneTwoThree题目地址：http://www.codewars.com/kata/linked-lists-push-and-buildonetwothree/train/python
# Linked Lists - Length & Count题目地址：http://www.codewars.com/kata/55beec7dd347078289000021/train/python
# Linked Lists - Get Nth Node题目地址：http://www.codewars.com/kata/linked-lists-get-nth-node
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.list = build_one_two_three()
        
    def test1(self):self.assertEqual(get_nth(self.list, 0).data, 1, "First node should be located at index 0.")
    def test2(self):self.assertEqual(get_nth(self.list, 1).data, 2, "Second node should be located at index 1.")
    def test3(self):self.assertEqual(get_nth(self.list, 2).data, 3, "Third node should be located at index 2.")

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

# 第三题：
def get_nth(node, index):
    if node == None:
        raise Exception
    elif index not in range(length(node)):
        raise Exception
    else:
        while index > 0:
            node = node.next
            index -= 1
    return node
    
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
    
def get_nth(node, index):
  if node and index >= 0: return node if index < 1 else get_nth(node.next, index - 1)
  raise ValueError
  
解法2：
def get_nth(node, index, i=0):
    if node is None:
        raise IndexError
    else:
        return node if index == i else get_nth(node.next, index, i + 1)
'''