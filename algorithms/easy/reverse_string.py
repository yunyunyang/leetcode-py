# 344. Reverse String

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        index = round(len(s))-1
        for i in range(round(len(s)/2)):
            tmp = s[index]
            s[index] = s[i]
            s[i] = tmp
            index -=1

        return s


sol = Solution().reverseString(s = ["h","e","l","l","o"])
print(sol)