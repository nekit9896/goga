import unittest

from leetcode_progs.twoSum import Solution


class TestsUnittest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_twoSum1(self):
        self.assertEqual(self.solution.twoSum([1, 4, 5, 7, 13, 2], 6), [2, 0])


class TestPytest(Solution):
    solution = Solution()

    def test_twoSum2(self):
        assert self.solution.twoSum([1, 4, 5, 7, 13, 2], 6) == [2, 0]
