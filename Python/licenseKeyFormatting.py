"""
You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.

Example:
Input: S = "5F3Z-2e-9-w" K = 4
Output: "5F3Z-2E9W"
"""

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '')
        S = S.upper()
        i = len(S)-1
        c = 0
        l = []
        while i >= 0:
            if c < K:
                l.append(S[i])
                i -= 1
            else:
                l.append('-')
                l.append(S[i])
                i -= 1
                c = 0
            c += 1
        return ''.join(l[::-1])
