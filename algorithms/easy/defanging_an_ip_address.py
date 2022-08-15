# 1108. Defanging an IP Address

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

sol = Solution().defangIPaddr(address = "1.1.1.1")
print(sol)