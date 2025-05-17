import unittest

from solution import united_intervals, intersection_intervals, convert_pairs, appearance


class TestIntervalsFunctions(unittest.TestCase):
    def test_united_intervals(self):
        self.assertEqual(united_intervals([]), [])
        self.assertEqual(united_intervals([(1, 5)]), [(1, 5)])
        self.assertEqual(united_intervals([(1, 5), (6, 10)]), [(1, 5), (6, 10)])
        self.assertEqual(united_intervals([(1, 5), (4, 8), (10, 15)]), [(1, 8), (10, 15)])
        self.assertEqual(united_intervals([(1, 10), (2, 3), (5, 6)]), [(1, 10)])

    def test_intersection_intervals(self):
        self.assertEqual(intersection_intervals((1, 5), (3, 7)), (3, 5))
        self.assertIsNone(intersection_intervals((1, 5), (6, 10)))
        self.assertEqual(intersection_intervals((1, 5), (5, 10)), (5, 5))
        self.assertEqual(intersection_intervals((1, 10), (2, 3)), (2, 3))

    def test_convert_pairs(self):
        self.assertEqual(convert_pairs([1, 2, 3, 4]), [(1, 2), (3, 4)])
        self.assertEqual(convert_pairs([1, 2, 3]), [(1, 2)])
        self.assertEqual(convert_pairs([]), [])

    def test_appearance(self):
        data = {
            'lesson': [1594663200, 1594666800],
            'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
            'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
        }
        result = appearance(data)
        self.assertEqual(result, 3117)

        data = {
            'lesson': [1594702800, 1594706400],
            'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                      1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                      1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                      1594706524, 1594706524, 1594706579, 1594706641],
            'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]
        }
        result = appearance(data)
        self.assertEqual(result, 3577)

        data = {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692033, 1594696347],
            'tutor': [1594692017, 1594692066, 1594692068, 1594696341]
        }
        result = appearance(data)
        self.assertEqual(result, 3565)


if __name__ == '__main__':
    unittest.main()