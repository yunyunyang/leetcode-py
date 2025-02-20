# 1980. Find Unique Binary String

from typing import List

def findDifferentBinaryString(self, nums: List[str]) -> str:
    n = len(nums)
    nums_set = set(nums)

    def backtrack(i, cur):
        if i == n:
            num = ''.join(cur)
            if num not in nums_set:
                return num
            return None

        for j in range(2):
            cur.append(str(j))
            res = backtrack(i + 1, cur)
            if res:
                return res
            cur.pop()
            
    return backtrack(0, [])