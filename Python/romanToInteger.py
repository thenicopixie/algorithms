"""
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        if s is None or type(s) is not str:
            return 0
        numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sums = 0
        nums = []
        for i in (s):
            if i in numerals:
                nums.append(numerals[i])
            else:
                return 0
        i = 0
        while i < len(nums)-1:
            if nums[i] > nums[i + 1]:
                sums += nums[i]
            elif nums[i] < nums[i + 1]:
                sums -= nums[i]
            else:
                sums += nums[i]
            i += 1
        sums += nums[i]
        return sums
        
