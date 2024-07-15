# 3162. Find the Number of Good Pairs I

from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        good_pairs = 0
        
        for n1 in nums1:
            for n2 in nums2:
                if n1 % (n2 * k) == 0:
                    good_pairs += 1
                    
        return good_pairs
    
sol = Solution().numberOfPairs(nums1 = [1,3,4], nums2 = [1,3,4], k = 1)
print(sol)