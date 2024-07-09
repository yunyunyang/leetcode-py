# 1701. Average Waiting Time

from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        times, cur_time = 0, 0
        
        for c in customers:
            end_time = max(cur_time, c[0]) + c[1]
            times += end_time - c[0]
            cur_time = end_time
            
        return times / len(customers)
    
sol = Solution().averageWaitingTime(customers = [[1,2],[2,5],[4,3]])
print(sol)