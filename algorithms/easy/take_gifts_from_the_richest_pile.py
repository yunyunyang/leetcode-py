# 2558. Take Gifts From the Richest Pile

from typing import List

import heapq
import math

def pickGifts(self, gifts: List[int], k: int) -> int:
    heap = []
    for n in gifts:
        heapq.heappush(heap, n * -1)

    for i in range(k):
        maxPile = heapq.heappop(heap) * -1
        rest = math.floor(math.sqrt(maxPile))
        heapq.heappush(heap, rest * -1)

    return sum(heap) * -1