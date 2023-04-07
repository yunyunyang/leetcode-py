# 1374. Generate a String With Characters That Have Odd Counts

class Solution:
    def generateTheString(self, n: int) -> str:
        o = ''
        if n%2 == 0:
            o = 'a' + 'b'*(n-1)
        else:
            o = 'a'*n

        return o
    
sol = Solution().generateTheString(n = 4)
print(sol)