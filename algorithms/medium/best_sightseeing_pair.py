# 1014. Best Sightseeing Pair

from typing import List

def maxScoreSightseeingPair(self, values: List[int]) -> int:
    curMax, maxScore = values[0] - 1, 0
    for i in range(1, len(values)):
        maxScore = max(maxScore, curMax + values[i])
        curMax = max(curMax - 1, values[i] - 1)
        
    return maxScore