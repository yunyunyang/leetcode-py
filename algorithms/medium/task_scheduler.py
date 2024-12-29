# 621. Task Scheduler

from typing import List
from collections import deque
import heapq

def leastInterval(self, tasks: List[str], n: int) -> int:
    heap, count = [], {}
    for t in tasks:
        count[t] = count.get(t, 0) + 1
    for v in count.values():
        heapq.heappush(heap, -v)

    timer, q = 0, deque()
    while heap or q:
        timer += 1
        if heap:
            task = heapq.heappop(heap)
            if task + 1 != 0:
                q.append((task + 1, timer + n))
        if q and q[0][1] == timer:
            heapq.heappush(heap, q.popleft()[0])

    return timer