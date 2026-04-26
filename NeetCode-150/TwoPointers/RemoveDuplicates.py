from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        low = 0
        high = 1
        k = 1

        while high < len(nums):
            if nums[high] == nums[high - 1]:
                high += 1
                continue
            nums[low + 1] = nums[high]
            low += 1
            k += 1
            high += 1

        return k