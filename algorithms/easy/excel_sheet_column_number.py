# 171. Excel Sheet Column Number

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = list(columnTitle[::-1])
        sum = 0
        for i, n in enumerate(columnTitle):
            sum += (ord(n) - 64) * (26 ** i)

        return sum


sol = Solution().titleToNumber(columnTitle = "ZY")
print(sol)