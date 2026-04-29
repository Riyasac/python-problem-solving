"""
Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

    Each letter in pattern maps to exactly one unique word in s.
    Each unique word in s maps to exactly one letter in pattern.
    No two letters map to the same word, and no two words map to the same letter.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

    'a' maps to "dog".
    'b' maps to "cat".

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false
"""

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_mapped = {}
        word_mapped = {}
        for ch, word in zip(pattern, words):
            if ch in char_mapped:
                if char_mapped[ch] != word:
                    return False
            else:
                if word in word_mapped:
                    return False
                char_mapped[ch] = word
                word_mapped[word] = ch
        return True


if __name__ == "__main__":
    pattern = "abba"
    s = "dog cat cat dog"
    print(Solution().wordPattern(pattern, s))

    pattern = "abba"
    s = "dog cat cat fish"
    print(Solution().wordPattern(pattern, s))

    pattern = "aaaa"
    s = "dog cat cat dog"
    print(Solution().wordPattern(pattern, s))