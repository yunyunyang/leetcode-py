# 2433. Find The Original Array of Prefix Xor

# pref[index]     = arr[0] ^ arr[1] ^ ... ^ arr[index]
# pref[index - 1] = arr[0] ^ arr[1] ^ ... ^ arr[index - 1]
# pref[index]     = pref[index - 1] ^ arr[index]
# arr[index]      = pref[index] ^ pref[index - 1]

from typing import List

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if (len(pref) == 0) | (len(pref) == 1):
            return pref

        o = []
        o.append(pref[0])
        for i in range(1, len(pref)):
            o.append(pref[i-1]^pref[i])
            
        return o
    
sol = Solution().findArray(pref = [5,2,0,3,1])
print(sol)

