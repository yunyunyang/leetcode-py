# 34. Find First and Last Position of Element in Sorted Array

from typing import List


class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        def find_first(left, right):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if mid == 0 or nums[mid - 1] != target:
                        return mid
                    else:
                        right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        def find_last(left, right):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        return mid
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        left, right = 0, len(nums) - 1
        first = find_first(left, right)
        last = find_last(left, right)

        return [first, last]


sol = Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=6)
print(sol)
