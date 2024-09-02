# 1894. Find the Student that Will Replace the Chalk

from typing import List

def chalkReplacer(self, chalk: List[int], k: int) -> int:
    index = -1
    k = k % sum(chalk)
    while k >= 0:
        for i in range(len(chalk)):
            k -= chalk[i]
            if k < 0:
                index = i
                break

    return index
      