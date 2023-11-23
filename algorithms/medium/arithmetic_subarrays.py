# 1630. Arithmetic Subarrays

from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = []
        for i in range(len(l)):
            subary = nums[l[i]:r[i]+1]
            subary.sort()
            diff = subary[0] - subary[1]
            check = True
            for i in range(1, len(subary)-1):
                if subary[i] - subary[i+1] != diff:
                    check = False
                    break

            output.append(check)

        return output


sol = Solution().checkArithmeticSubarrays(
    nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5])
print(sol)
