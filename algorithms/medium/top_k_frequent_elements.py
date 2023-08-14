# 347. Top K Frequent Elements

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for i in nums:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1

        m = dict(sorted(m.items(), key=lambda k:k[1], reverse=True))
        return list(m.keys())[:k]
        
sol = Solution().topKFrequent(nums = [3,0,1,0], k = 1)
print(sol)