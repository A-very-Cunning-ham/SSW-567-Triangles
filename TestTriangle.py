# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

from math import sqrt

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def test_RightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def test_RightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def test_nonright_scalene(self):
        self.assertEqual(classifyTriangle(1, 2.5, 3), "Scalene")

    def test_right_scalene(self):
        self.assertEqual(classifyTriangle(3, 4, 5), "Right")

    def test_nonright_isosceles(self):
        self.assertEqual(classifyTriangle(1, 1, 1.5), "Isosceles")

    def test_right_isosceles(self):
        self.assertEqual(classifyTriangle(1, sqrt(2), 1), "Right")

    def test_equilateral(self):
        self.assertEqual(classifyTriangle(3, 3, 3), "Equilateral")

    def test_notATriangle(self):
        self.assertEqual(classifyTriangle(1, 1, 3), "NotATriangle")
    
    def test_invalidInput_outOfRange(self):
        self.assertEqual(classifyTriangle(300, 300, 300), "InvalidInput")
    
    def test_invalidInput_wrongType(self):
        self.assertEqual(classifyTriangle("2", "3", "5"), "InvalidInput")

    def test_invalidInput_notPositive(self):
        self.assertEqual(classifyTriangle(-1, -3, -4), "InvalidInput")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

