"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        for i in s:
            if self.isOpening(i):
                stack.append(i)
            elif self.isClosing(i):
                if stack:
                    if not self.isMatch(i, stack.pop()):
                        return False
                else:
                    return False
        if len(stack):
            return False
        return True
    
    def isOpening(self, c: str) -> bool:
        opening = ['(', '[', '{']
        if c in opening:
            return True
        return False
    
    def isClosing(self, c: str) -> bool:
        closing = [')', ']', '}']
        if c in closing:
            return True
        return False
        
    def isMatch(self, c: str, top: str) -> bool:
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        if pairs[top] != c:
            return False
        return True
