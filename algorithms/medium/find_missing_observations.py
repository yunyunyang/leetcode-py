# 2028. Find Missing Observations

from typing import List

def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
    sum_n = mean * (len(rolls) + n) - sum(rolls)
    output = []
    if sum_n > 6 * n or sum_n < n:
        return []

    while n > 0:
        v = sum_n // n
        output.append(v)
        sum_n -= v
        n -= 1

    return output