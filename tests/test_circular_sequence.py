import unittest

from demo.circular_sequence import (
    SequenceError,
    SequenceOverlapError,
    SequenceRange,
    ensure_no_overlap,
    normalize_sequence,
    ranges_overlap,
)


class CircularSequenceTests(unittest.TestCase):
    def test_normalizes_to_three_digits(self):
        self.assertEqual(normalize_sequence("7"), "007")
        self.assertEqual(normalize_sequence("000"), "000")
        self.assertEqual(normalize_sequence(999), "999")

    def test_rejects_invalid_values(self):
        for value in ("", "-1", "1000", "1A", "1234"):
            with self.subTest(value=value), self.assertRaises(SequenceError):
                normalize_sequence(value)

    def test_detects_overlap_across_cycle_boundary(self):
        wrapped = SequenceRange("850", "040", 1)
        next_cycle = SequenceRange("020", "030", 2)
        self.assertTrue(ranges_overlap(wrapped, next_cycle))
        with self.assertRaises(SequenceOverlapError):
            ensure_no_overlap(next_cycle, [wrapped])

    def test_allows_gaps_and_non_overlapping_ranges(self):
        first = SequenceRange("850", "895", 1)
        second = SequenceRange("900", "920", 1)
        ensure_no_overlap(second, [first])
        self.assertFalse(ranges_overlap(first, second))

    def test_rejects_invalid_cycle(self):
        with self.assertRaises(SequenceError):
            SequenceRange("001", "010", 0)


if __name__ == "__main__":
    unittest.main()
