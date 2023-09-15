# 2483. Minimum Penalty for a Shop

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        p = 0
        for c in customers:
            if c == "Y":
                p += 1

        penalty = []
        penalty.append(p)

        for i in range(1, len(customers)):
            if customers[i] == "Y":
                penalty.append(penalty[i-1]-1)
            else:
                penalty.append(penalty[i-1])

        print(penalty)
        return


sol = Solution().bestClosingTime(customers="YYNY")
print(sol)
