# 506. Relative Ranks

from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_dict = {}
        for i, s in enumerate(score):
            score_dict[s] = i
        
        score.sort(reverse=True)
        for i, s in enumerate(score):
            if i == 0:
                score_dict[s] = "Gold Medal"
            elif i == 1:
                score_dict[s] = "Silver Medal"
            elif i == 2:
                score_dict[s] = "Bronze Medal"
            else:
                score_dict[s] = str(i + 1)
        
        return score_dict.values()
    
sol = Solution().findRelativeRanks(score = [10,3,8,9,4])
print(sol)