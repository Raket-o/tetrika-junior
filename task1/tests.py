import unittest

from solution import sum_two


class TestStrictDecorator(unittest.TestCase):
    def test_correct_types(self):
        self.assertEqual(sum_two(1, 2), 3)
        self.assertEqual(sum_two(-1, 1), 0)
        self.assertEqual(sum_two(0, 0), 0)

    def test_incorrect_types_positional(self):
        with self.assertRaises(TypeError):
            sum_two("1", 2)
        with self.assertRaises(TypeError):
            sum_two(1, "2")
        with self.assertRaises(TypeError):
            sum_two(1, False)

    def test_incorrect_types_keyword(self):
        with self.assertRaises(TypeError):
            sum_two(a=1, b="2")
        with self.assertRaises(TypeError):
            sum_two(a=True, b=1)

    def test_mixed_arguments(self):
        self.assertEqual(sum_two(1, b=2), 3)
        with self.assertRaises(TypeError):
            sum_two(1, b="two")


if __name__ == '__main__':
    unittest.main()
