
import unittest


from GS3 import answer

# Swetha Sankar
# Testing File Lesson #15
# I used a lot of file reading, debugging, and print statements in order to test my project
# in addition to these test cases.
# Covers all functions used (other than main)


class Testing(unittest.TestCase):
    def test_map_lines(self):
        # testing conversion of file to dictionary
        actual = answer.map_lines(["4",
                                   "Kitchen empty Office Parlor",
                                   "Office robot Kitchen",
                                   "Parlor robot Kitchen Stairs",
                                   "Stairs empty Parlor"])
        self.assertEqual(actual, {'Kitchen': [['Office', 'Parlor'], 'empty'], 'Office': [['Kitchen'], 'robot'],
                                  'Parlor': [['Kitchen', 'Stairs'], 'robot'], 'Stairs': [['Parlor'], 'empty']})

    def test_mapping(self):
        actual2 = answer.map_lines(["10", "A empty B C", "B robot A D", "C empty A D E", "D empty B C E F I J"])
        self.assertEqual(actual2, {'A': [['B', 'C'], 'empty'], 'B': [['A', 'D'], 'robot'],
                                  'C': [['A', 'D', 'E'], 'empty'], 'D': [['B', 'C', 'E', 'F', 'I', 'J'], 'empty']})

    def testing_more_mapping(self):
        actual3 = answer.map_lines(["4", "F empty D G", "G empty F H","H empty G","I empty D J"])
        self.assertEqual(actual3, {'F': [['D', 'G'], 'empty'], 'G': [['F', 'H'], 'empty'],
                                  'H': [['G'], 'empty'], 'I': [['D', 'J'], 'empty']})

    def test_mapping_again(self):
        # testing conversion of file to dictionary
        actual = answer.map_lines(["2",
                                   "Kitchen empty Office",
                                   "Office robot Kitchen"])
        self.assertEqual(actual, {'Kitchen': [['Office'], 'empty'], 'Office': [['Kitchen'], 'robot']})

    def testing_build(self):
        # testing whether the path reconstructs given a start, end, and previous path
        actual4 = answer.build('B', 'H', {'A':'B', 'D':'B', 'C':'A', 'E':'D', 'F':'D', 'I':'D','J':'D', 'G':'F', 'H':'G'})
        self.assertEqual(actual4, ['B', 'D', 'F', 'G', 'H'])

    def testing_more_build(self):
        # testing whether the path reconstructs given an incorrect previous path
        actual5 = answer.build('A', 'H', {'A':'B', 'D':'B', 'C':'A', 'E':'D', 'F':'D', 'I':'D','J':'D', 'G':'F', 'H':'G'})
        self.assertEqual(actual5, [])

    def test_dr_bart(self):
        # does it find dr.bart to be in the room that is the last one visited?
        actual6 = answer.find_bart('Kitchen', {'Kitchen': ['Office', 'Parlor'], 'Office': ['Kitchen'],
                                  'Parlor': ['Kitchen', 'Stairs'], 'Stairs': ['Parlor']})
        self.assertEqual(actual6, 'Stairs')

    def test_once_more_dr_bart(self):
        actual17 = answer.find_bart('Redding', {'Redding': ['Harrington', 'Turf'], 'Harrington': ['Redding', 'Pod'],
                                  'Turf': ['Redding', 'Harrington'], 'Pod': ['Harrington']})
        self.assertEqual(actual17, 'Pod')

    def test_finding_bart(self):
        actual7 = answer.find_bart('A', {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D', 'E'], 'D': ['B', 'C', 'E', 'F', 'I', 'J'], 'E': ['C', 'D'],
                                         'F': ['D', 'G'], 'G': ['F', 'H'],
                                         'H': ['G'], 'I': ['D', 'J'], 'J': ['D', 'I']})
        self.assertEqual(actual7, 'H')

    def test_solve(self):
        actual8 = answer.solve('B', {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D', 'E'], 'D': ['B', 'C', 'E', 'F', 'I', 'J'], 'E': ['C', 'D'],
                                         'F': ['D', 'G'], 'G': ['F', 'H'],
                                         'H': ['G'], 'I': ['D', 'J'], 'J': ['D', 'I']})
        self.assertEqual(actual8, {'A': 'B', 'C': 'A','D': 'B', 'E': 'D', 'F': 'D', 'G': 'F','H': 'G','I': 'D','J': 'D'})

    def testing_solve_again(self):
        actual9 = answer.solve('Kitchen', {'Kitchen': ['Office', 'Parlor'], 'Office': ['Kitchen'],
                                  'Parlor': ['Kitchen', 'Stairs'], 'Stairs': ['Parlor']})
        self.assertEqual(actual9, {'Office': 'Kitchen', 'Parlor': 'Kitchen', 'Stairs': 'Parlor'})

    def testing_solve_once_again(self):
        actual10 = answer.solve('Office', {'Kitchen': ['Office', 'Parlor'], 'Office': ['Kitchen'],
                                  'Parlor': ['Kitchen', 'Stairs'], 'Stairs': ['Parlor']})
        self.assertEqual(actual10, {'Kitchen': 'Office', 'Parlor': 'Kitchen', 'Stairs': 'Parlor'})

    def testing_bfs_driver(self):
        actual11 = answer.bfs('B', 'H', {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D', 'E'], 'D': ['B', 'C', 'E', 'F', 'I', 'J'], 'E': ['C', 'D'],
                                         'F': ['D', 'G'], 'G': ['F', 'H'],
                                         'H': ['G'], 'I': ['D', 'J'], 'J': ['D', 'I']})
        self.assertEqual(actual11, ['B', 'D', 'F', 'G', 'H'])

    def testing_bfs_again(self):
        actual12 = answer.bfs('Office', 'Stairs', {'Kitchen': ['Office', 'Parlor'], 'Office': ['Kitchen'],
                                  'Parlor': ['Kitchen', 'Stairs'], 'Stairs': ['Parlor']})
        self.assertEqual(actual12, ['Office', 'Kitchen', 'Parlor', 'Stairs'])

    def testing_bfs_more(self):
        actual13 = answer.bfs('Parlor', 'Stairs', {'Kitchen': ['Office', 'Parlor'], 'Office': ['Kitchen'],
                                  'Parlor': ['Kitchen', 'Stairs'], 'Stairs': ['Parlor']})
        self.assertEqual(actual13, ['Parlor', 'Stairs'])

    def testing_bfs_even_more(self):
        # if there is a robot in the kitchen
        actual14 = answer.bfs('Kitchen', 'Stairs', {'Kitchen': ['Office', 'Parlor'], 'Office': ['Kitchen'],
                                  'Parlor': ['Kitchen', 'Stairs'], 'Stairs': ['Parlor']})
        self.assertEqual(actual14, ['Kitchen', 'Parlor', 'Stairs'])

    def testing_bfs_even_even_more(self):
        actual15 = answer.bfs('D', 'H', {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D', 'E'], 'D': ['B', 'C', 'E', 'F', 'I', 'J'], 'E': ['C', 'D'],
                                         'F': ['D', 'G'], 'G': ['F', 'H'],
                                         'H': ['G'], 'I': ['D', 'J'], 'J': ['D', 'I']})
        self.assertEqual(actual15, ['D', 'F', 'G', 'H'])

    def testing_bfs_so_much_more(self):
        actual16 = answer.bfs('A', 'H', {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D', 'E'], 'D': ['B', 'C', 'E', 'F', 'I', 'J'], 'E': ['C', 'D'],
                                         'F': ['D', 'G'], 'G': ['F', 'H'],
                                         'H': ['G'], 'I': ['D', 'J'], 'J': ['D', 'I']})
        self.assertEqual(actual16, ['A', 'B', 'D', 'F', 'G', 'H'])

    def test_bfs_one(self):
        actual16 = answer.bfs('G', 'H', {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D', 'E'], 'D': ['B', 'C', 'E', 'F', 'I', 'J'], 'E': ['C', 'D'],
                                         'F': ['D', 'G'], 'G': ['F', 'H'],
                                         'H': ['G'], 'I': ['D', 'J'], 'J': ['D', 'I']})
        self.assertEqual(actual16, ['G', 'H'])

    def test_bfs_two(self):
        actual16 = answer.bfs('C', 'H', {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D', 'E'], 'D': ['B', 'C', 'E', 'F', 'I', 'J'], 'E': ['C', 'D'],
                                         'F': ['D', 'G'], 'G': ['F', 'H'],
                                         'H': ['G'], 'I': ['D', 'J'], 'J': ['D', 'I']})
        self.assertEqual(actual16, ['C', 'D', 'F', 'G', 'H'])

if __name__ == '__main__':
    unittest.main()
