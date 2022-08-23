# 1688. Count of Matches in Tournament

class Solution:
    def numberOfMatches(self, n: int) -> int:
        output = 0
        while n != 1:
            if n % 2 == 0:
                output += n/2
                n = (n/2)
            else:
                output += (n-1)/2
                n = (n-1)/2 + 1

        return int(output)

sol = Solution().numberOfMatches(n = 7)
print(sol)