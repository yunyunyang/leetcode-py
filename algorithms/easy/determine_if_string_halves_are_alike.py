# 1704. Determine if String Halves Are Alike

class Solution:

    def halvesAreAlike(self, s: str) -> bool:
        lst = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        half = int(len(s)/2)
        first = s[:half]
        second = s[half:]
        num1 = num2 = 0

        for i in range(half):
            if first[i] in lst:
                num1 += 1
            if second[i] in lst:
                num2 += 1

        return num1 == num2


sol = Solution().halvesAreAlike(s = "textbook")
print(sol)