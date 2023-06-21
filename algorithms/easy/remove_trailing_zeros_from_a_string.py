# 2710. Remove Trailing Zeros From a String

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        if num[-1] != "0":
            print("x")
            return num
        
        for i in range(len(num)-1, -1, -1):
            if num[i] != "0":
                return num[:i+1]
    
sol = Solution().removeTrailingZeros(num = "51230100")
print(sol)