#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Are they the "same"题目地址：http://www.codewars.com/kata/are-they-the-same
'''

import time
import unittest
        
class TestCases(unittest.TestCase):
    def test1(self):
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
        self.assertEqual(comp(a1, a2), True)

def comp(array1, array2):
    result = True
    if len(array1) != len(array2) or array1 == None:
        result = False
    else:
        for item in array1:
            if not item ** 2 in array2:
                result = False
                break
            else:
                array2.remove(item ** 2)
    return result
    
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
def comp(a1, a2):
    return None not in (a1,a2) and [i*i for i in sorted(a1)]==sorted(a2)
'''