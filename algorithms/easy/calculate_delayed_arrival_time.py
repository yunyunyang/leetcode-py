# 2651. Calculate Delayed Arrival Time

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24
    
sol = Solution().findDelayedArrivalTime(arrivalTime = 13, delayedTime = 11)
print(sol)