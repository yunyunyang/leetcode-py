# 2798. Number of Employees Who Met the Target

from typing import List

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        hours.sort()
        if hours[-1] < target:
            return 0
        
        for i in range(len(hours)-1, -1, -1):
            if hours[i] < target:
                return len(hours) - i -1
            
        return len(hours)
            
sol = Solution().numberOfEmployeesWhoMetTarget(hours = [98], target = 5)
print(sol)