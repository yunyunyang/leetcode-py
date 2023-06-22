# 1812. Determine Color of a Chessboard Square

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if (ord(coordinates[0]) - 96) % 2 == 0:
            if int(coordinates[1]) % 2 == 1:
                return True
            else:
                return False
        else:
            if int(coordinates[1]) % 2 == 0:
                return True
            else:
                return False
        
    
sol = Solution().squareIsWhite(coordinates = "h3")
print(sol)