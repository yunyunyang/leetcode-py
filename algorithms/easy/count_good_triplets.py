#1534. Count Good Triplets

from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        output = 0
        size = len(arr)

        for i in range(size-2):
            for j in range(i+1, size-1) :
                for k in range(j+1, size):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        output += 1

        return output


sol = Solution().countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3)
print(sol)