import unittest
from user_input_validation import input_validated


class TestInputValidated(unittest.TestCase):
    def test_valid_input_3_is_True(self):
        expect = True
        actual = input_validated("3")
        self.assertEqual(expect, actual)

    def test_valid_input_empty_string_is_False(self):
        expect = False
        actual = input_validated("")
        self.assertEqual(expect, actual)

    def test_valid_input_0_is_False(self):
        expect = False
        actual = input_validated("0")
        self.assertEqual(expect, actual)

    def test_valid_input_7_is_False(self):
        expect = False
        actual = input_validated("7")
        self.assertEqual(expect, actual)

    def test_valid_input_non_number(self):
        expect = False
        actual = input_validated("a%")
        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
