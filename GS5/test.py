
import unittest


from GS5 import answer

# Swetha Sankar
# Testing File Lesson #21
# I used a lot of file reading, debugging, and print statements in order to test my project
# in addition to these test cases.
# Covers all functions used (other than main)


class Testing(unittest.TestCase):
    def test_split_values(self):
        actual = answer.split_values(["5", "15", "Blueprints 4 50", "HardDrive 10 2", "DogFood 10 5", "MysteriousCrystal 20 60", "SuperComputer 100 100"])
        self.assertEqual(actual, [50, 2, 5, 60, 100])

    def test_split_names(self):
        actual = answer.split_names(["5", "15", "Blueprints 4 50", "HardDrive 10 2", "DogFood 10 5", "MysteriousCrystal 20 60", "SuperComputer 100 100"])
        self.assertEqual(actual, ["Blueprints", "HardDrive", "DogFood", "MysteriousCrystal", "SuperComputer"])

    def test_split_weights(self):
        actual = answer.split_weights(["5", "15", "Blueprints 4 50", "HardDrive 10 2", "DogFood 10 5", "MysteriousCrystal 20 60", "SuperComputer 100 100"])
        self.assertEqual(actual, [4,10,10,20,100])



if __name__ == '__main__':
    unittest.main()
