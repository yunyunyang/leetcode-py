# 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        y = 0
        n = x
        while n > 0:
            r = n % 10
            y = y * 10 + r
            n //= 10
            
        return x == y