# 3223. Minimum Length of String After Operations

from collections import Counter

def minimumLength(self, s: str) -> int:
    freq = Counter(s)
    count = 0
    for v in freq.values():
        if v % 2 == 1:
            count += v - 1
        else:
            count += v - 2

    return len(s) - count