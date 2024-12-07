# 1760. Minimum Limit of Balls in a Bag

from typing import List

def minimumSize(self, nums: List[int], maxOperations: int) -> int:
    left, right = 1, max(nums)
    output = right

    while left <= right:
        mid = (left + right) // 2
        ops = 0

        for n in nums:
            ops += (n - 1) // mid
            if ops > maxOperations:
                break

        if ops <= maxOperations:
            output = mid
            right = mid - 1
        else:
            left = mid + 1

    return output