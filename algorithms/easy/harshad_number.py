# 3099. Harshad Number

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_digits = 0
        dummy = x
        while dummy:
            sum_digits += dummy % 10
            dummy //= 10

        return sum_digits if x % sum_digits == 0 else -1


sol = Solution().sumOfTheDigitsOfHarshadNumber(x=23)
print(sol)
