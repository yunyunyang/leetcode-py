# 1769. Minimum Number of Operations to Move All Balls to Each Box

from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        output = []
        for i, o in enumerate(boxes):
            ops = 0 
            for j, p in enumerate(boxes):
                if p != "0":
                    ops += abs(j-i)

            output.append(ops)

        return output


sol = Solution().minOperations(boxes = "110")
print(sol)