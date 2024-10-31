from unittest import main, TestCase


class Solution:
    # LeetCode annoyingly doesn't follow PEP 8 function naming
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_letter_counts: dict[str, int] = {}
        t_letter_counts: dict[str, int] = {}

        for index in range(len(s)):
            s_letter_counts[s[index]] = s_letter_counts.get(s[index], 0) + 1
            t_letter_counts[t[index]] = t_letter_counts.get(t[index], 0) + 1
        
        return s_letter_counts == t_letter_counts


class TestContainsDuplicate(TestCase):
    def test_valid_anagram(self):
        target: str = "anagram"
        potential_anagram: str = "nagaram"
        self.assertTrue(Solution().isAnagram(target, potential_anagram))
    
    def test_invalid_anagram(self):
        target: str = "rat"
        potential_anagram: str = "car"
        self.assertFalse(Solution().isAnagram(target, potential_anagram))

if __name__ == '__main__':
    main()