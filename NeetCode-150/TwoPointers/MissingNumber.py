from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        ones = 0

        for i in nums:
            if i == 1:
                ones += 1
                max_ones = max(ones, max_ones)
            else:
                ones = 0
        return max_ones