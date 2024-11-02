from unittest import main, TestCase


class Solution:
    # LeetCode annoyingly doesn't follow PEP 8 method naming
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        matching_anagrams_by_anagram_identifier: dict[tuple[int], list[str]] = {}

        for string in strs:
            anagram_identifier: list[int] = [0] * 26
            for character in string:
                anagram_identifier[ord(character) - ord('a')] += 1

            anagram_identifier: tuple[int] = tuple(anagram_identifier)

            matching_anagrams: list[str] = matching_anagrams_by_anagram_identifier.get(anagram_identifier, [])
            matching_anagrams.append(string)
            matching_anagrams_by_anagram_identifier[anagram_identifier] = matching_anagrams
        
        return list(matching_anagrams_by_anagram_identifier.values())


class TestGroupAnagrams(TestCase):
    def test_group_anagrams(self):
        strings: list[str] = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected: list[int] = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        actual: list[int] = Solution().groupAnagrams(strings)
        self.assertEqual(tuple(expected), tuple(actual))
    
    def test_group_anagrams_empty_string(self):
        strings: list[str] = [""]
        expected: list[int] = [[""]]
        actual: list[int] = Solution().groupAnagrams(strings)
        self.assertEqual(tuple(expected), tuple(actual))

    def test_group_anagrams_single_character(self):
        strings: list[str] = ["a"]
        expected: list[int] = [["a"]]
        actual: list[int] = Solution().groupAnagrams(strings)
        self.assertEqual(tuple(expected), tuple(actual))


if __name__ == '__main__':
    main()