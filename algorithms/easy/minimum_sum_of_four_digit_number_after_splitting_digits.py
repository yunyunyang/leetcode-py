# 2160. Minimum Sum of Four Digit Number After Splitting Digits

class Solution:
    def minimumSum(self, num: int) -> int:
        n = sorted([*str(num)])
        return int(n[0] + n[2]) + int(n[1] + n[3])

ans = Solution().minimumSum(num = 2932)
print(ans)