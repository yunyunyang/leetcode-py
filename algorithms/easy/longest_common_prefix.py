# 14. Longest Common Prefix

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        strs.sort()
        first, last = strs[0], strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                output += first[i]
            else:
                break
                
        return output

sol = Solution().longestCommonPrefix(strs = ["flower","flow","flight"])
print(sol)