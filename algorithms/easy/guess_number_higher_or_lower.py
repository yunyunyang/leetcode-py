# 374. Guess Number Higher or Lower

class Solution:
    def guess(n):
        return
    
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        
        while l <= r:
            m = l + (r - l) // 2
            pick = self.guess(m)
            print(pick)
            if pick == 1:
                l = m + 1
            elif pick == -1:
                r = m
            else:
                return m
