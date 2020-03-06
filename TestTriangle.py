import unittest
from triangle_run import classify_triangle
import math

class TestTriangles(unittest.TestCase):

    def testRightTriangleA(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classify_triangle(5, 3, 4), 'Right','5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classify_triangle(1, 1, 1),'Equilateral', '1,1,1 should be equilateral')

    def testNotATriangleA(self): 
        self.assertEqual(classify_triangle(1,3,10),'NotATriangle',"1,3,10 should be NotATriangle")
    
    def testNotATriangleB(self): 
        self.assertEqual(classify_triangle(9,1,10),'NotATriangle',"9,1,10 shouldt be NotATriangle")
    
    def testNotATriangleC(self): 
        self.assertEqual(classify_triangle(3,3,10),'NotATriangle','3,3,10 should be NotATriangle')
        
    def testInvalidInput(self): 
        self.assertEqual(classify_triangle(1,0.1,4),'InvalidInput',"1,0.1,4 should be InvalidInput")
        
    def testInvalidInput2(self): 
        self.assertEqual(classify_triangle(1,-2,4),'InvalidInput',"1,-2,4 should be InvalidInput")
    
    def testInvalidInput3(self): 
        self.assertEqual(classify_triangle(1,0,4),'InvalidInput',"201,2,4 should be InvalidInput")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit = False, verbosity= 2)
