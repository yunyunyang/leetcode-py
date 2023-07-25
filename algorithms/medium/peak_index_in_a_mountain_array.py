# 852. Peak Index in a Mountain Array

from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1
        m = len(arr)//2
        while l < r:
            m = l + (r-l)//2
            if arr[m] > arr[m-1] and arr[m] > arr[m+1]:
                return m
            if arr[m] < arr[m-1]:
                r = m
            if arr[m] < arr[m+1]:
                l = m + 1

        return m
    
sol = Solution().peakIndexInMountainArray(arr = [3,9,8,6,4])
print(sol)