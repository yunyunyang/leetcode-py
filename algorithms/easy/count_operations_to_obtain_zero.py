# 2169. Count Operations to Obtain Zero

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ops = 0
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                num1 = num1 - num2
            elif num1 < num2:
                num2 = num2 - num1
            ops += 1
                    
        return ops
    
sol = Solution().countOperations(num1 = 2, num2 = 3)
print(sol)