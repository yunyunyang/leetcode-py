# 2315. Count Asterisks

class Solution:
    def countAsterisks(self, s: str) -> int:
        output = 0
        divider = 0
        for i in [*s]:
            if i == "|":
                divider += 1
            if divider % 2 == 0:
                if i == "*":
                    output += 1

        return output

sol = Solution().countAsterisks(s = "l|*e*et|c**o|*de|")
print(sol)