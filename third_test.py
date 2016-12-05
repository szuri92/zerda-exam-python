from third import count_letter_in_string
import unittest

class TestMyFunctions(unittest.TestCase):
    def test_count_letter_in_string_with_no_string(self):
        self.assertEqual(count_letter_in_string(2, 'b'), 0)
    def test_count_letter_in_string_with_letter_as_number(self):
        self.assertEqual(count_letter_in_string('alma5', 5), 0)

if __name__ == '__main__':
    unittest.main(exit=False)
