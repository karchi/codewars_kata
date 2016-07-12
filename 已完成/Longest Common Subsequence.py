#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目地址：
https://www.codewars.com/kata/52756e5ad454534f220001ef/train/python
'''

import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(lcs("a", "b"), "")
    def test2(self):self.assertEqual(lcs("abcdef", "abc"), "abc")
    def test3(self):self.assertEqual(lcs("abcdef", "acf"), "acf")
    def test4(self):self.assertEqual(lcs("132535365", "123456789"), "12356")
    # def test5(self):self.assertEqual(fib(4),3)


def lcs(x, y):
    long_list = [[0 for col in range(len(x)+1)] for row in range(len(y)+1)]
    result = ""
    for m in range(len(x)):
        for n in range(len(y)):
            if x[m] == y[n]:
                long_list[n+1][m+1] = long_list[n][m] + 1
            else:
                long_list[n+1][m+1] = max(long_list[n][m+1],long_list[n+1][m])
    i = len(x) - 1
    j = len(y) - 1
    while i > -1 and j > -1:
        if x[i] == y[j]:
            result = x[i] + result
            i -= 1
            j -= 1
        else:
            if long_list[j][i+1] > long_list[j+1][i]:
                j -= 1
            else:
                i -= 1
    return result

        
if __name__ == '__main__':
    unittest.main()


    



    
'''
参考解法：
from itertools import combinations
def subsequences(s):
    """Returns set of all subsequences in s."""
    return set(''.join(c) for i in range(len(s) + 1) for c in combinations(s, i))
def lcs(x, y):
    """Returns longest matching subsequence of two strings."""
    return max(subsequences(x).intersection(subsequences(y)), key=len)
    
# 参考解法2：
def lcs(x, y):
    if len(x) == 0 or len(y) == 0:
        return ''
    if x[-1] == y[-1]:
        return lcs(x[:-1], y[:-1]) + x[-1]
    else:
        lcs1 = lcs(x,y[:-1])
        lcs2 = lcs(x[:-1],y)
        if len(lcs1) > len(lcs2):
            return lcs1
        else:
            return lcs2
            
#参考解法3：
def lcs(x, y):
  res=[]
  i=0
  for item in y:
     if item in x[i:]:
        res+=[item]
        i=x.index(item)+1
  return "".join(res)
'''