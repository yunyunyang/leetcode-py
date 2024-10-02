# 1331. Rank Transform of an Array

from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(list(set(arr)))
        
        rank = {}
        for i in range(len(sorted_arr)):
            rank[sorted_arr[i]] = i + 1

        for i in range(len(arr)):
            arr[i] = rank[arr[i]]
        
        return arr