from unittest import main, TestCase


class Solution:
    # LeetCode annoyingly doesn't follow PEP 8 method naming
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count_by_character: dict[str, int] = {}
        t_count_by_character: dict[str, int] = {}

        for index in range(len(s)):
            s_count_by_character[s[index]] = s_count_by_character.get(s[index], 0) + 1
            t_count_by_character[t[index]] = t_count_by_character.get(t[index], 0) + 1
        
        return s_count_by_character == t_count_by_character


class TestValidAnagram(TestCase):
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