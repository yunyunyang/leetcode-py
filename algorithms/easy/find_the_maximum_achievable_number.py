# 2769. Find the Maximum Achievable Number

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2*t
    
sol = Solution().theMaximumAchievableX(num = 3, t = 2)
print(sol)