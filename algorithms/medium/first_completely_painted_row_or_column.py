# 2661. First Completely Painted Row or Column

from typing import List

def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
    rows, cols = len(mat), len(mat[0])
    position = {}
    row_cnt, col_cnt = [0] * rows, [0] * cols
    for r in range(rows):
        for c in range(cols):
            position[mat[r][c]] = (r, c)
            row_cnt[r] += 1
            col_cnt[c] += 1

    for i, n in enumerate(arr):
        r, c = position[n]
        row_cnt[r] -= 1
        col_cnt[c] -= 1
        if row_cnt[r] == 0 or col_cnt[c] == 0:
            return i
    
    return 0