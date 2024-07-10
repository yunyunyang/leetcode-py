# 1598. Crawler Log Folder

from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == '../':
                if stack:
                    stack.pop()
            elif log == './':
                continue
            else:
                stack.append(log)
                
        return len(stack)
    
    
sol = Solution().minOperations()
print(sol)