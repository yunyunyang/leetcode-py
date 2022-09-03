# 1816. Truncate Sentence

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        output = ""
        words = s.split(" ")
        for i, w in enumerate(words):
            if i < k:
                output += w + " "

        return output.strip()

sol = Solution().truncateSentence(s = "Hello how are you Contestant", k = 4)
print(sol)