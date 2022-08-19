# 1528. Shuffle String

from re import S
from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = ""
        dic = dict(zip(indices, s))
        sorted(dic)

        for i in range(len(dic)):
            output += dic[i]

        return output

sol = Solution().restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3])
print(sol)