# 2520. Count the Digits That Divide a Number

class Solution:
    def countDigits(self, num: int) -> int:
        num_divide = 0
        for i in str(num):
            num_divide += 1 if num % int(i) == 0 else 0

        return num_divide


sol = Solution().countDigits(num = 1248)
print(sol)