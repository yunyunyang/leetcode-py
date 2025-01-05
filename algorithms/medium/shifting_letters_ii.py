# 2381. Shifting Letters II

from typing import List

def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
    n = len(s)
    count = [0] * (n + 1)
    for start, end, direction in shifts:
        if direction == 1:
            count[start] += 1
            count[end + 1] -= 1
        else:
            count[start] -= 1
            count[end + 1] += 1

    for i in range(1, n):            
        count[i] += count[i - 1]

    res = []
    for i in range(n):
        char = chr((ord(s[i]) - ord('a') + count[i]) % 26 + ord('a'))
        res.append(char)

    return ''.join(res)