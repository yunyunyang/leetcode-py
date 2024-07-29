# 202. Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        
        while n not in visit:
            visit.add(n)
            s = 0
            while n > 0:
                digit = n % 10
                s += digit ** 2
                n //= 10
            n = s
            
            if n == 1:
                return True
            
        return False


sol = Solution().isHappy(n=2)
print(sol)
