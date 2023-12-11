# 1287. Element Appearing More Than 25% In Sorted Array

import math
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        threshold = math.ceil(len(arr) / 4)
        output = -1
        num, count = 0, 0
        for n in arr:
            if num == n:
                count += 1
            else:
                num = n
                count = 1

            if count >= threshold:
                output = num

        return output


sol = Solution().findSpecialInteger(arr=[1])
print(sol)
