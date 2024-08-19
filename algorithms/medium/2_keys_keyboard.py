# 650. 2 Keys Keyboard

class Solution:
    def minSteps(self, n: int) -> int:
        output = 0
        count, copy = 1, 0
        
        while count != n:
            if n % count == 0:
                copy = count
                output += 1

            count += copy
            output += 1

        return output

sol = Solution().minSteps(3)
print(sol)