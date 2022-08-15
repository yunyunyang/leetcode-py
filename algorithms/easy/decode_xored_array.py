# 1720. Decode XORed Array

from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        undecoded = [first]
        for i, e in enumerate(encoded):
            undecoded.append(undecoded[i]^e)
        
        return undecoded

sol = Solution().decode(encoded = [1,2,3], first = 1)
print(sol)