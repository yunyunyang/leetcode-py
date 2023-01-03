# 944. Delete Columns to Make Sorted

from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deletion = 0
        for j in range(len(strs[0])):
            isLexicography = True
            for i in range(1, len(strs)):
                if strs[i-1][j] > strs[i][j]:
                    isLexicography = False
            if not isLexicography:
                deletion += 1

        return deletion


sol = Solution().minDeletionSize(strs = ["zyx","wvu","tsr"])
print(sol)