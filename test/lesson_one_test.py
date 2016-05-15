import unittest
from app import lesson_one

# this is a test plan for codility lesson one
class Test(unittest.TestCase):


    def test_solution(self):
        result1 = lesson_one.solution(8)
        self.assertEqual(0, result1)
        
        result2 = lesson_one.solution(5)
        self.assertEqual(1, result2)

        result3 = lesson_one.solution(69)
        self.assertEqual(3, result3)

    def test_remove_zeros_in_the_ned(self):
        result1 = lesson_one._remove_zeros_in_the_end(8)
        self.assertEqual(1, result1)

        result2 = lesson_one._remove_zeros_in_the_end(9)
        self.assertEqual(9, result2)