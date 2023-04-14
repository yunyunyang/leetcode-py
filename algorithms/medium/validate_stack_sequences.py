# 946. Validate Stack Sequences

from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = []
        i = 0
        for p in pushed:
            s.append(p)
            if p == popped[i]:
                s.pop()
                i += 1
            
            while s and s[-1] == popped[i]:
                s.pop()
                i += 1

        return len(s) == 0
    
sol = Solution().validateStackSequences(pushed = [1,2,3,4,5], popped = [4,3,5,1,2])
print(sol)