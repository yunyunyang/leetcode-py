# 2011. Final Value of Variable After Performing Operations

from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for op in operations:
            if "++" in op:
                result += 1
            if "--" in op:
                result -= 1
        
        return result


sol = Solution().finalValueAfterOperations(operations = ["--X","X++","X++"])
print(sol)