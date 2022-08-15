# 1342. Number of Steps to Reduce a Number to Zero

class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
                steps += 1
            else:
                num -=1
                steps += 1

        return steps

sol = Solution().numberOfSteps(num = 14)
print(sol)