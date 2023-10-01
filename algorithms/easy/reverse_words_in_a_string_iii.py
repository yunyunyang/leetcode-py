# 557. Reverse Words in a String III

class Solution:
    def reverseWords(self, s: str) -> str:
        output = []
        words = s.split(" ")
        for w in words:
            ws = list(w)
            for i in range(len(w)//2):
                j = len(ws) - i - 1
                ws[i], ws[j] = ws[j], ws[i]
            output.append("".join(ws))

        return " ".join(output)


sol = Solution().reverseWords(s="Let's take LeetCode contest")
print(sol)
