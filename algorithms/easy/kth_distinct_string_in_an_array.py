# 2053. Kth Distinct String in an Array

from typing import List
from collections import defaultdict

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = defaultdict(int)
        for c in arr:
            count[c] = count.get(c, 0) + 1

        print(count)
            
        for key, value in count.items():
            if value == 1:
                k -= 1
                if k == 0:
                    return key
            
        return ""
    
sol = Solution().kthDistinct(arr = ["d","b","c","b","c","a"], k = 2)
print(sol)