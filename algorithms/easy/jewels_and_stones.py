# 771. Jewels and Stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in [*jewels]:
            count += stones.count(i)
            
        return count


sol = Solution().numJewelsInStones(jewels = "aA", stones = "aAAbbbb")
print(sol)