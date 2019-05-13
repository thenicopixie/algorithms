"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        maxsub = nums[0]
        current = 0
        for i in nums:
            current += i
            maxsub = max(current, maxsub)
            current = max(0, current)
        return maxsub
