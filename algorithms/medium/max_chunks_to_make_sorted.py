# 769. Max Chunks To Make Sorted

from typing import List

def maxChunksToSorted(self, arr: List[int]) -> int:
    cursum, chunks = 0, 0
    for i, n in enumerate(arr):
        cursum +=  i - n
        if cursum == 0:
            chunks += 1

    return chunks