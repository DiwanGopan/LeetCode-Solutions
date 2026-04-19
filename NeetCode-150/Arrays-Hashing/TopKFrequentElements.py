from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: # type: ignore
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        print(count)
        freq = [[] for _ in range(len(nums) + 1)]
        
        print(freq)

        for num, c in count.items():
            freq[c].append(num)

        print(freq)
        result = []

        # print(freq[len(freq)-1])

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result