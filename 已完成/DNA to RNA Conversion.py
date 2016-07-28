#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# DNA to RNA Conversion题目地址：http://www.codewars.com/kata/5556282156230d0e5e000089/train/python
'''

import time
import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):self.assertEqual(DNAtoRNA("TTTT"), "UUUU")
    def test2(self):self.assertEqual(DNAtoRNA("GCAT"), "GCAU")
    def test3(self):self.assertEqual(DNAtoRNA("GACCGCCGCC"), "GACCGCCGCC")
    # def test4(self):self.assertEqual(find_even_index(range(1,100)),-1)
    # def test5(self):self.assertEqual(find_even_index([0,0,0,0,0]),0)

def DNAtoRNA(dna):
    return dna.replace("T","U")
    
if __name__ == '__main__':
    unittest.main()
    
    # 测试时间：
    # start = time.clock()
    # for i in range(100000):
        # b = filter_list([1,2,'aasf','1','123',123])
    # end = time.clock()
    # print(end - start)

    



    
'''
参考解法：
def DNAtoRNA(dna):
    return "".join(["U" if c=="T" else c for c in dna])
    
解法2：
import re
def DNAtoRNA(dna):
    return re.sub('T', 'U', dna)
'''