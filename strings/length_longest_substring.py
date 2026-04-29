"""
Longest Substring Without Repeating Characters


Given a string s, find the length of the longest without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        max_length = 0
        char_map = {}

        for right in range(len(s)):
            char = s[right]

            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1

            char_map[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length
            

if __name__ == "__main__":
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))

    s = "bbbbb"
    print(Solution().lengthOfLongestSubstring(s))

    s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s))