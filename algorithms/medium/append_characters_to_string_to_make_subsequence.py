# 2486. Append Characters to String to Make Subsequence

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        right = 0
        
        for left in range(len(s)):
            if s[left] == t[right]:
                right += 1
            
            if right >= len(t):
                break
                
        return len(t) - right
    
sol = Solution().appendCharacters(s = "coaching", t = "coding")
print(sol)