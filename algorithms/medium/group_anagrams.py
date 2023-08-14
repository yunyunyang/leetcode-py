# 49. Group Anagrams

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        
        m = {}
        for s in strs:
            w = "".join(sorted(s))
            if w not in m:
                m[w] = [s]
            else:
                m[w].append(s)

        return m.values()
    
sol = Solution().groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])
print(sol)