import unittest
from GS2 import answer


class TestLast(unittest.TestCase):
    def test_it_out(self):
        actual = answer.map_lines(["1", "1 S 6 2", "1 P 1400 3", "1 S 8 8", "2 S 5 2", "2 P 5 2"])
        self.assertEqual(actual,
                         {
                            1: {'sid': 1, 'lowest_pid': "6", 'latest_pid': "1400", 'sub_score': '7'},
                            2: {'sid': 2, 'lowest_pid': "5", 'latest_pid': "5", 'sub_score': '5'}
                         })


if __name__ == '__main__':
    unittest.main()
