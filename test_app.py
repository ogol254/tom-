import unittest
from app import *


class TestDice(unittest.TestCase):
    """docstring for TestDice"""

    def test_main(self):
        self.assertEqual(main('n'), "Game over Goodbye!")
        self.assertEqual(main('z'), "Not recognised!")

    def test_input(self):
        self.assertEqual(input_data(), None)


if __name__ == '__main__':
    unittest.main()
