#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Two fighters, one winner.题目地址：https://www.codewars.com/kata/577bd8d4ae2807c64b00045b/train/python
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):self.assertEqual(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew"), "Lew")
    def test2(self):self.assertEqual(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Harry"),"Harry")
    def test3(self):self.assertEqual(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry"),"Harald")
    def test4(self):self.assertEqual(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harald"),"Harald")
    def test5(self):self.assertEqual(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry"), "Harald")
    def test6(self):self.assertEqual(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald"),"Harald")

    
class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        
        
def declare_winner(fighter1, fighter2, first_attacker):
    def fight(fighter1, fighter2):
        while(fighter1.health > 0 and fighter2.health > 0):
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health <= 0:
                return fighter1.name
            fighter1.health -= fighter2.damage_per_attack
            if fighter1.health <= 0:
                return fighter2.name
    if first_attacker == fighter1.name:
        res = fight(fighter1, fighter2)
    else:
        res = fight(fighter2, fighter1)
    return res
    
if __name__ == '__main__':
    unittest.main()

    
    
    
    

    



    
'''
参考解法：
from math import ceil
from operator import attrgetter
def declare_winner(fighter1, fighter2, first_attacker):
    fighter1.turns = ceil(fighter1.health / float(fighter2.damage_per_attack))
    fighter2.turns = ceil(fighter2.health / float(fighter1.damage_per_attack))
    if fighter1.turns == fighter2.turns:
        return first_attacker
    return max(fighter1, fighter2, key=attrgetter('turns')).name
    
解法2：
def declare_winner(a, b, n):
    if a.name != n:
        a, b = b, a
    while a.health > 0:
        b.health -= a.damage_per_attack
        a, b = b, a
    return b.name
'''