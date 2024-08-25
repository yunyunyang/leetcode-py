# 49. Group Anagrams

from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            output[tuple(count)].append(s)

        return output.values()
    
sol = Solution().groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])
print(sol)