# 739. Daily Temperatures

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                id, temp = stack.pop()
                days[id] = i - id

            stack.append((i, t))

        return days


sol = Solution().dailyTemperatures(
    temperatures=[73, 74, 75, 71, 69, 72, 76, 73])
print(sol)
