"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s.rstrip()) == 0:
            return 0
        return len(s.strip().split(' ')[-1])
