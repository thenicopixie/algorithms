"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        i = 1
        s = "1"
        while i < n:
            r = ''
            c = 0
            l = s[0]
            for j, v in enumerate(s):
                if l == v:
                    c += 1
                else:
                    r += str(c) + l
                    l = v
                    c = 1
            r += str(c) + l
            i += 1
            s = r  
        return s
