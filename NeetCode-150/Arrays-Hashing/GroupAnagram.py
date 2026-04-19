from typing import List


class Solution:

    def getfreq(self, s: str):
        freq = [0]*26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        return tuple(freq) 

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: # type: ignore
        seen = {}
        for s in strs:
            key = self.getfreq(s)
            if key in seen:
                seen[key].append(s)
            else:
                seen[key] = [s]
                
        return list(seen.values())      