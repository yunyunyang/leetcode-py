# 786. K-th Smallest Prime Fraction

from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        prime = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                prime.append((arr[i]/arr[j], arr[i], arr[j]))
            
        prime.sort()
        print
        return [prime[k - 1][1], prime[k - 1][2]]
    
sol = Solution().kthSmallestPrimeFraction(arr = [1,2,3,5], k = 3)
print(sol)