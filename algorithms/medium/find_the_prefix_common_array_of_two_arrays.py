# 2657. Find the Prefix Common Array of Two Arrays

from typing import List

def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
    res = [0] * len(A)
    once, twice = set(), set()
    for i in range(len(A)):
        if A[i] not in once:
            once.add(A[i])
        elif A[i] in once and A[i] not in twice:
            twice.add(A[i])
        
        if B[i] not in once:
            once.add(B[i])
        elif B[i] in once and B[i] not in twice:
            twice.add(B[i])

        res[i] = len(twice)

    return res