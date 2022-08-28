
# 2037. Minimum Number of Moves to Seat Everyone

from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        output = 0
        seats = sorted(seats)
        students = sorted(students)
        for i in range(len(seats)):
            output += abs(students[i] - seats[i])

        return output

sol = Solution().minMovesToSeat(seats = [3,1,5], students = [2,7,4])
print(sol)