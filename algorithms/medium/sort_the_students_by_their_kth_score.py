# Sort the Students by Their Kth Score

from typing import List

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        o = [[]] * len(score)
        m = {}
        print(len(score))
        for i in range(len(score)):
            m[i] = score[i][k]
            
        m = dict(sorted(m.items(), key=lambda item: item[1], reverse=True))
        i = 0
        for v in m.keys():
            o[i] = score[v]
            i += 1

        return o

sol = Solution().sortTheStudents(score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2)
print(sol)