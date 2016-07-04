#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 题目地址：
http://www.codewars.com/kata/541af676b589989aed0009e7
'''

import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(3, count_change(4, [1,2]))
    def test2(self):self.assertEqual(4, count_change(10, [5,2,3]))
    def test3(self):self.assertEqual(0, count_change(11, [5,7]))
    # def test4(self):self.assertEqual(countBits(10), 2)
    # def test5(self):self.assertEqual(lowercase_count("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), 0)
    # def test6(self):self.assertEqual(lowercase_count("abcdefghijklmnopqrstuvwxyz"), 26)

'''
#可运行，但太慢
from itertools import combinations
def count_change(money, coins):
    result = 0
    if money == 0 or len(coins) == 0: #可能会有输入错误
        return result
    coins.sort(reverse = True)
    temp_sum = []

    for coin in coins:
        n = money//coin
        for x in range(1,n+1):
            temp_sum.append(coin)
    for pick in range(1,money//coins[-1]+1):
        for pick_coins in combinations(temp_sum,pick):
            if sum(pick_coins) == money:
                result +=1
                break
    return result
'''   
 
    

from itertools import combinations

def count_change(money, coins):
    result = 0
    if money == 0 or len(coins) == 0: #可能会有输入错误
        return result
    coins.sort(reverse = True)
    temp_sum = []

    for coin in coins:
        temp_sum.append(list(range(0, money+1, coin)))
        # for x in range(0, money+1, coin):
            # temp_sum.append(x)
            
    # 只选一个，但每次需要从该coin的分段中选
    '''
    result_list = []
    def select_coins(sub_coins, money, result_list):
        result_list_in = result_list[:]
        if len(sub_coins) > 1:
            # select_coins(sub_coins[1:], money, result_list_in) #递归
        for coin in sub_coins[0]:      #递归之后执行
            if coin + select_coins(sub_coins[1:], money, result_list_in) == money:
    '''
    
    def select_coins(sub_coins):
        if len(sub_coins) > 1:
            for coin in sub_coins[0]:      #递归之后执行
                yield coin + select_coins(sub_coins[1:])
        else:
            for coin in sub_coins[0]:
                yield coin
    
    for pick_coins in select_coins(temp_sum):
        if pick_coins == money:
            result +=1
    return result

if __name__ == '__main__':
    unittest.main()
    # a = 4//5
    # print(a)
    # a = []
    # for x in (1,2,3):
        # a.append(list(range(0,10,x)))
    # print(len(a))
    
