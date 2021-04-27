
import unittest


from GS5 import answer

# Swetha Sankar
# Testing File Lesson #21
# I used a lot of file reading, debugging, and print statements in order to test my project
# in addition to these test cases.
# Covers all functions used (other than main)


class Testing(unittest.TestCase):
    def test_map_lines(self):
        # testing conversion of file to dictionary
        actual = answer.map_lines(["5", "15", "Blueprints 4 50", "HardDrive 10 2", "DogFood 10 5", "MysteriousCrystal 20 60", "SuperComputer 100 100"])
        self.assertEqual(actual, {'Blueprints': [4, 50],  'HardDrive': [10,2],
                                  'DogFood': [10,5], 'MysteriousCrystal': [20,60], 'SuperComputer':[100,100]});



if __name__ == '__main__':
    unittest.main()
