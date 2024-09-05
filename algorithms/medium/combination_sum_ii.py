# 40. Combination Sum II

from typing import List

def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    output = []

    def dfs(i, comb, total):
        if total == target:
            output.append(comb.copy())
            return
        
        if i >= len(candidates) or total > target:
            return
        
        comb.append(candidates[i])
        dfs(i + 1, comb, total + candidates[i])
        comb.pop()

        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1

        dfs(i + 1, comb, total)
    
    dfs(0, [], 0)
    return output