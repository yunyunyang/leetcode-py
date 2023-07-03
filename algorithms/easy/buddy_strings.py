# 859. Buddy Strings

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal and len(set(s)) < len(s):
            return True
        
        d = [(a, b) for a, b in zip(s, goal) if a != b]

        print(d)

        return len(d) == 2 and d[0] == d[1][::-1]

    
sol = Solution().buddyStrings(s = "ab", goal = "ba")
print(sol)