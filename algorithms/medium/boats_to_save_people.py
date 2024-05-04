# 881. Boats to Save People

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
        while left < right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                boats += 1
            else:
                right -= 1
                boats += 1

        return boats + 1 if left == right else boats
    
sol = Solution().numRescueBoats(people = [1,2], limit = 3)
print(sol)