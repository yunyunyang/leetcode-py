# 771. Jewels and Stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in [*jewels]:
            count += stones.count(i)
            
        return count


ans = Solution().numJewelsInStones(jewels = "aA", stones = "aAAbbbb")
print(ans)