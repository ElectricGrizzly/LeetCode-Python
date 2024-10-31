from unittest import main, TestCase


class Solution:
    # LeetCode annoyingly doesn't follow PEP 8 function naming
    def containsDuplicate(self, nums: list[int]) -> bool:
        number_set: set[int] = set()
        for number in nums:
            if number in number_set:
                return True
            number_set.add(number)
        return False

class TestContainsDuplicate(TestCase):
    def test_when_duplicate_in_small_list(self):
        numbers: list[int] = [1, 2, 3, 1]
        self.assertTrue(Solution().containsDuplicate(numbers))
    
    def test_when_duplicate_in_large_list(self):
        numbers: list[int] = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        self.assertTrue(Solution().containsDuplicate(numbers))

    def test_when_no_duplicate_in_small_list(self):
        numbers: list[int] = [1, 2, 3, 4]
        self.assertFalse(Solution().containsDuplicate(numbers))

if __name__ == '__main__':
    main()