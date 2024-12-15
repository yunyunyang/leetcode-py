# 1792. Maximum Average Pass Ratio

from typing import List
import heapq

def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
    
    def calculateRatio(passes, students):
        return (passes + 1) / (students + 1) - passes / students

    maxHeap = []
    for passes, students in classes:
        heapq.heappush(maxHeap, (-calculateRatio(passes, students), passes, students))

    for _ in range(extraStudents):
        ratio, passes, students = heapq.heappop(maxHeap)
        heapq.heappush(maxHeap, (
            -calculateRatio(passes + 1, students + 1),
            passes + 1,
            students + 1
        ))

    totalRatio = 0
    while maxHeap:
        _, passes, students = heapq.heappop(maxHeap)
        totalRatio += passes / students

    return totalRatio / len(classes)