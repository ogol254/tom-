import unittest
from run import *


class TestDice(unittest.TestCase):
    """docstring for TestDice"""

    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertNotEqual(add(2, 3), 6)


if __name__ == '__main__':
    unittest.main()
