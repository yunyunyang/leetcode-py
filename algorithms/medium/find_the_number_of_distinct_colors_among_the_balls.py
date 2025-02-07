# 3160. Find the Number of Distinct Colors Among the Balls

from typing import List
from collections import defaultdict

def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
    ball, color = defaultdict(), defaultdict(list)
    res = []
    for x, y in queries:
        if x in ball:
            color[ball[x]].remove(x)
            if len(color[ball[x]]) == 0:
                del color[ball[x]]
        ball[x] = y
        color[y].append(x)
        res.append(len(color))
    
    return res