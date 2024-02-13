# 2108. Find First Palindromic String in the Array

from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            l, r = 0, len(w)-1
            while l <= r:
                if len(w) == 1:
                    return w

                if w[l] == w[r] and r - l <= 2:
                    return w
                elif w[l] == w[r]:
                    l += 1
                    r -= 1
                else:
                    break

        return ""


sol = Solution().firstPalindrome(
    words=["cqllrtyhw", "swwisru", "gpzmbders", "wqibjuqvs", "pp", "usewxryy", "ybqfuh", "hqwwqftgyu", "jggmatpk"])
print(sol)
