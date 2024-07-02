# 350. Intersection of Two Arrays II

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        
        for n in nums1:
            dict1[n] = dict1.get(n, 0) + 1
        
        output = []
        for n in nums2:
            if n in dict1 and dict1[n] > 0:
                dict1[n] = dict1[n] - 1
                output.append(n)
            
        return output
    
sol = Solution().intersect(nums1 = [1,2,2,1], nums2 = [2,2])
print(sol)