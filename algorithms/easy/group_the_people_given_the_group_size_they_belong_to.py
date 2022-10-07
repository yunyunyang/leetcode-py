# 1282. Group the People Given the Group Size They Belong To

from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        output = []
        group = {}
        for i, p in enumerate(groupSizes):
            if group.get(p) is None:
                dic = {p: [i]}
                group.update(dic)
            else:
                group.get(p).append(i)

        for k, v in group.items():
            if k == len(v):
                output.append(v)
            else:
                sub = []
                for i in v:
                    if len(sub) == k:
                        output.append(sub)
                        sub = []
                        sub.append(i)
                    else:
                        sub.append(i)
                output.append(sub)

        return output


sol = Solution().groupThePeople(groupSizes = [3,3,3,3,3,1,3])
print(sol)