# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(i) for i in list(n))

sol = Solution().minPartitions(n = "32")
print(sol)