from unittest import main, TestCase


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(' ', '')
        



class TestValidPalindrome(TestCase):
    def test_top_k_frequent_large_list(self):
        numbers: list[int] = [1, 1, 1, 2, 2, 3]
        k: int = 2
        expected: list[int] = [1, 2]
        actual: list[int] = Solution().topKFrequent(numbers, k)
        self.assertEqual(expected, actual)
    
    def test_top_k_frequent_short_list(self):
        numbers: list[int] = [1]
        k: int = 1
        expected: list[int] = [1]
        actual: list[int] = Solution().topKFrequent(numbers, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()