# 2582. Pass the Pillow

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        forward = (time // (n - 1)) % 2 == 0
        re = time % (n - 1)
        
        if forward:
            return 1 + re
        else:
            return n - re
    
sol = Solution().passThePillow(n = 4, time = 5)
print(sol)