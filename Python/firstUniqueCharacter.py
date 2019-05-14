"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
	"""
	create hash table to store index of chars
	if char is not unique in string store -1 at value in dictionary
	store dictionary value in a list only if the value is not -1
	sort list
	return first index of list
	"""

        d = {}
        for i, v in enumerate(s):
            if v not in d:
                d[v] = i
            else:
                d[v] = -1
        a = d.values()
        a = [x for x in a if x != -1]
        if not a:
            return -1
        a.sort()
        return a[0]
