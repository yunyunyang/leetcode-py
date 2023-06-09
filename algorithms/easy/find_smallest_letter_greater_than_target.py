# 744. Find Smallest Letter Greater Than Target

from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        
        for l in letters:
            if l > target:
                return l
    
sol = Solution().nextGreatestLetter(letters = ["x","x","y","y"], target = "z")
print(sol)