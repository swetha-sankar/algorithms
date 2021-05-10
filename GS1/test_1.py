import unittest
import answer


class TestLast(unittest.TestCase):
    def test_gets_last(self):
        actual = answer.summation([2,2,3])
        self.assertEqual(actual, 5)

    def test_handles_empty(self):
        actual = answer.summation([])
        self.assertEqual(actual, "EMPTY")

    def test_1(self):
        actual = answer.summation([2,-1, 5 ])
        self.assertEqual(actual, 5)


    def test_2(self):
        actual = answer.summation([2,-1, -999])
        self.assertEqual(actual, "EMPTY")


    def test_3(self):
        actual = answer.summation([3,7, -999, 38])
        self.assertEqual(actual, 7)


if __name__ == '__main__':
    unittest.main()