# 2054. Two Best Non-Overlapping Events

"""
- Time complexity: 
  Sorting takes (O(nlogn), precomputing the maximum values takes (O(n), and binary search for each event takes (O(nlogn). 
  Overall: (O(nlogn).
- Space complexity: 
  Additional space is used for the maxValue array, which is O(n)
"""

from typing import List

def maxTwoEvents(self, events: List[List[int]]) -> int:
    events.sort(key=lambda x: x[0])

    maxVal = [0] * len(events)
    maxVal[-1] = events[-1][2]
    for i in range(len(events) - 2, -1, -1):
        maxVal[i] = max(maxVal[i + 1], events[i][2])

    output = 0
    for i in range(len(events)):
        output = max(output, events[i][2])            
        left, right = i + 1, len(events) - 1
        target = -1
        while left <= right:
            mid = (left + right) // 2
            if events[mid][0] > events[i][1]:
                target = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if target != -1:
            output = max(output, events[i][2] + maxVal[target])
                
    return output