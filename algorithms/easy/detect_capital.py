class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return

        num_capital = num_not_capital = len(word) - 1
        if ord(word[0]) in range(65, 90):
            for i in word[1:]:
                if ord(i) in range(65, 91):
                    num_capital -= 1
                if ord(i) in range(97, 123):
                    print(i)
                    num_not_capital -= 1

            return True if num_capital == 0 or num_not_capital == 0 else False

        else:
            for i in word:
                if ord(i) in range(65, 91):
                    return False
            return True


sol = Solution().detectCapitalUse(word = "Z")
print(sol)