from unittest import main, TestCase


class Solution:
    # LeetCode annoyingly doesn't follow PEP 8 method naming
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index_by_difference: dict[int, int] = {}

        for index, number in enumerate(nums):
            difference = target - number
            if difference in index_by_difference:
                return [index_by_difference[difference], index]
            index_by_difference[number] = index


class TestTwoSum(TestCase):
    def test_four_element_list(self):
        numbers: list[int] = [2, 7 ,11, 15]
        target: int = 9
        expected: list[int] = [0, 1]
        actual: list[int] = Solution().twoSum(numbers, target)
        self.assertEqual(expected, actual)
    
    def test_three_element_list(self):
        numbers: list[int] = [3, 2, 4]
        target: int = 6
        expected: list[int] = [1, 2]
        actual: list[int] = Solution().twoSum(numbers, target)
        self.assertEqual(expected, actual)

    def test_two_element_list(self):
        numbers: list[int] = [3, 3]
        target: int = 6
        expected: list[int] = [0, 1]
        actual: list[int] = Solution().twoSum(numbers, target)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()