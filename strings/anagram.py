"""
Valid Anagram

Given two strings s and t, return true if t is an of s, and false otherwise.


Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false


Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # from collections import Counter
        # return Counter(s) == Counter(t)
    
        if len(s) != len(t):
            return False
    
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        for ch in t:
            if ch not in freq:
                return False
            
            freq[ch] -= 1
            if freq[ch] < 0:
                return False
        
        for count in freq.values():
            if count != 0:
                return False
        return True

    
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))

    s = "rat"
    t = "car"
    print(Solution().isAnagram(s, t))
