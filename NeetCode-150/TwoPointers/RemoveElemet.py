from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int: # type: ignore
        l = 0
        h = len(nums) - 1

        while l <= h:
            if nums[l] == val:
                nums[l], nums[h] = nums[h], nums[l]
                h -= 1
            else:
                l += 1
        
        return l