# 1486. XOR Operation in an Array

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        output = 0
        for i in range(n):
            num = start + 2*i
            output ^= num

        return output

sol = Solution().xorOperation(n = 4, start = 3)
print(sol)