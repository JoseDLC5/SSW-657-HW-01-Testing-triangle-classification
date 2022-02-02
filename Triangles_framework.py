# -*- coding: utf-8 -*-
import unittest     
import math


def classifyTriangle(a, b, c):
    array = [a, b, c]
    array.sort()

    if array[0]+array[1] <= array[2]:
        return 'NotATriangle'
    elif a == b and b == c:
        return 'Equilateral'
    elif a == b or b == c:
        return 'Isosceles'
    elif array[0]**2+array[1]**2 == array[2]**2:
        return 'Right'
    elif array[0] < array[1] and array[1] < array[2]:
        return 'Scaline'

def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(', a, ',', b, ',', c, ')=',
          classifyTriangle(a, b, c), sep="")

class TestTriangles(unittest.TestCase):
    def testRightTriangles(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right',
                         '3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(1, 1, math.sqrt(2)), 'Right',
                         '1,1,sqrt(2) is a Right triangle')

    def testEqualTriangle(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral',
                         '1,1,1 is an Equilateral Triangle')
        self.assertEqual(classifyTriangle(99999999, 99999999, 99999999), 'Equilateral',
                         '99999999,99999999,99999999 is an Equilateral Triangle')
        self.assertNotEqual(classifyTriangle(-1, -1, -1), 'Equilateral',
                            '-1,-1,-1 is not an Equilateral Triangle')

    def testIsoscelesTris(self):
        self.assertEqual(classifyTriangle(1, 1, math.sqrt(2)), 'Isosceles',
                         '1,1,sqrt(2) is an Isosceles')
        self.assertEqual(classifyTriangle(1, 2, 2), 'Isosceles',
                         '1,1000,1000 is an Isosceles')

    def testScalineTris(self):
        self.assertEqual(classifyTriangle(7, 12, 15), 'Scaline',
                         '1,1,sqrt(2) is an Scaline')
        self.assertEqual(classifyTriangle(7, 13, 14), 'Scaline',
                         '1,1,sqrt(2) is an Scaline')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(-1, -1, -1), 'NotATriangle',
                         '-1,-1,-1 is a Not a Triangle')
        self.assertEqual(classifyTriangle(10, 15, 30),
                         'NotATriangle', '10,15,30 is a Not a Triangle')


if __name__ == '__main__':
    unittest.main(exit=True)
