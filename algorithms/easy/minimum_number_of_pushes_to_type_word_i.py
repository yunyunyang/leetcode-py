# 3014. Minimum Number of Pushes to Type Word I

class Solution:
    def minimumPushes(self, word: str) -> int:
        output = 0
        n = len(word)
        if n <= 8:
            return n
        elif n // 8 == 1:
            return 8 + 2 * (n % 8)
        elif n // 8 == 2:
            return 8 + 8 * 2 + 3 * (n % 8)
        elif n // 8 == 3:
            return 8 + 8 * 2 + 8 * 3 + 4 * (n % 8)
    
sol = Solution().minimumPushes(word = "abcde")
print(sol)