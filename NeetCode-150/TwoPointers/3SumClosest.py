from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        closest_sum = float('inf')

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if abs(s - target) < abs(closest_sum - target):
                    closest_sum = s

                if s == target:
                    return s
                elif s < target:
                    left += 1
                else:
                    right -= 1

        return int(closest_sum)