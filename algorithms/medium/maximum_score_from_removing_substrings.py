# 1717. Maximum Score From Removing Substrings

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:        
        if x > y:
            high, low = "ab", "ba"
            high_score, low_score = x, y
        else:
            high, low = "ba", "ab"
            high_score, low_score = y, x
        
        scores, stack = 0, []

        # First phase: remove all "ab"
        for c in s:
            if c == high[1] and stack and stack[-1] == high[0]:
                stack.pop()
                scores += high_score
            else:
                stack.append(c)
        
        # Second phase: rmove all "ba"
        stack2 = []
        for c in stack:
            if c == low[1] and stack2 and stack2[-1] == low[0]:
                stack2.pop()
                scores += low_score
            else:
                stack2.append(c)
                
        return scores
    
sol = Solution().maximumGain(s = "cdbcbbaaabab", x = 4, y = 5)
print(sol)