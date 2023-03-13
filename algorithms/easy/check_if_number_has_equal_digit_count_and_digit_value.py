# 2283. Check if Number Has Equal Digit Count and Digit Value

class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            if int(num[i]) != num.count(str(i)):
                return False
        return True
    
sol = Solution().digitCount(num = "1210")
print(sol)