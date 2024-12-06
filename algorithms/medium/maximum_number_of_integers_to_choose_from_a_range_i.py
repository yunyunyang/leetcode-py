# 2554. Maximum Number of Integers to Choose From a Range I

from typing import List

def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
    banned = set(banned)
    curSum, count = 0, 0
    for i in range(1, n + 1):
        if i not in banned:
            curSum += i
            count += 1
        if curSum == maxSum:
            return count
        if curSum > maxSum:
            return 0 if count == 0 else count - 1

    return count