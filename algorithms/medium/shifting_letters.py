# 848. Shifting Letters

from typing import List

def shiftingLetters(self, s: str, shifts: List[int]) -> str:
    n = len(s)
    count = [0] * n
    count[-1] = shifts[-1]
    for i in range(n - 2, -1, -1):
        count[i] = shifts[i] + count[i + 1]

    res = [0] * n
    for i in range(n):
        code = (ord(s[i]) - ord('a') + count[i]) % 26 + ord('a')
        res[i] = chr(code)

    return ''.join(res)