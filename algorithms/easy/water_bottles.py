# 1518. Water Bottles

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        output = cur = numBottles 
        while cur >= numExchange:
            q = cur // numExchange
            r = cur % numExchange
            cur = q + r
            output += q
            
        return output 
        
sol = Solution().numWaterBottles(numBottles = 9, numExchange = 3)
print(sol)