
import unittest


from GS6 import answer

# Swetha Sankar
# Testing File Lesson #25
# Covers all functions used (other than main)


class Testing(unittest.TestCase):
    # Testing conversion of strings to the 2D int arrays
    def test_create_matrix1(self):
        actual = answer.create_matrix(
            ["5", "15", "0 4 50", "7 10 2", "8 10 5", "3 20 60", "8 100 100"])
        self.assertEqual(actual, [[5], [15], [0, 4, 50], [7, 10, 2], [8, 10, 5], [3, 20, 60], [8, 100, 100]])

    def test_create_matrix2(self):
        actual = answer.create_matrix(
            ["0  3  4  2  7", "3  0  4  6  3", "4  4  0  5  8", "2  6  5  0  6", "7  3  8  6  0"])
        self.assertEqual(actual, [[0, 3, 4, 2, 7], [3, 0, 4, 6, 3], [4, 4, 0, 5, 8], [2, 6, 5, 0, 6], [7, 3, 8, 6, 0]])





if __name__ == '__main__':
    unittest.main()
