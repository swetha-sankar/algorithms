
import unittest


from GS5 import answer

# Swetha Sankar
# Testing File Lesson #21
# Covers all functions used (other than main)


class Testing(unittest.TestCase):
    def test_split_values(self):
        actual = answer.split_values(
            ["5", "15", "Blueprints 4 50", "HardDrive 10 2", "DogFood 10 5", "MysteriousCrystal 20 60",
             "SuperComputer 100 100"])
        self.assertEqual(actual, [50, 2, 5, 60, 100])

    def test_split_names(self):
        actual = answer.split_names(
            ["5", "15", "Blueprints 4 50", "HardDrive 10 2", "DogFood 10 5", "MysteriousCrystal 20 60",
             "SuperComputer 100 100"])
        self.assertEqual(actual, ["Blueprints", "HardDrive", "DogFood", "MysteriousCrystal", "SuperComputer"])

    def test_split_weights(self):
        actual = answer.split_weights(
            ["5", "15", "Blueprints 4 50", "HardDrive 10 2", "DogFood 10 5", "MysteriousCrystal 20 60",
             "SuperComputer 100 100"])
        self.assertEqual(actual, [4, 10, 10, 20, 100])

    def test_knapsack(self):
        t = [[-1 for i in range(15 + 1)] for j in range(5 + 1)]
        actual = answer.knapsack(
            [4, 10, 10, 20, 100], [50, 2, 5, 60, 100], 15, 5, t,
            ["Blueprints", "HardDrive", "DogFood", "MysteriousCrystal", "SuperComputer"])
        self.assertEqual(actual, 55)

    def test_knapsack2(self):
        t = [[-1 for i in range(15 + 1)] for j in range(2 + 1)]
        actual = answer.knapsack(
            [20, 100], [60, 100], 15, 2, t,
            ["MysteriousCrystal", "SuperComputer"])
        self.assertEqual(actual, 0)

    def test_knapsack3(self):
        t = [[-1 for i in range(15 + 1)] for j in range(3 + 1)]
        actual = answer.knapsack(
            [10, 20, 100], [5, 60, 100], 15, 3, t,
            ["DogFood", "MysteriousCrystal", "SuperComputer"])
        self.assertEqual(actual, 5)


if __name__ == '__main__':
    unittest.main()
