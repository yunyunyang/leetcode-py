# 1780. Check if Number is a Sum of Powers of Three

def checkPowersOfThree(self, n: int) -> bool:
    
    def backtrack(i, cur_sum):
        if cur_sum == n:
            return True
        if cur_sum > n or 3**i > n:
            return False
        
        if backtrack(i + 1, cur_sum + 3**i):
            return True

        return backtrack(i + 1, cur_sum)

    return backtrack(0, 0)