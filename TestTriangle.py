# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

import math

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right','5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1),'Equilateral', '1,1,1 should be equilateral')

        
    def testNotATriangleA(self): 
        self.assertEqual(classifyTriangle(1,3,10),'NotATriangle',"1,3,10 should be NotATriangle")
    
    def testNotATriangleB(self): 
        self.assertEqual(classifyTriangle(9,1,10),'NotATriangle',"9,1,10 shouldt be NotATriangle")
    
    def testNotATriangleC(self): 
        self.assertEqual(classifyTriangle(3,3,10),'NotATriangle','3,3,10 should be NotATriangle')
        
    def testInvalidInput(self): 
        self.assertEqual(classifyTriangle(1,0.1,4),'InvalidInput',"1,0.1,4 should be InvalidInput")
        
    def testInvalidInput2(self): 
        self.assertEqual(classifyTriangle(1,-2,4),'InvalidInput',"1,-2,4 should be InvalidInput")
        

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit = False, verbosity= 2)
