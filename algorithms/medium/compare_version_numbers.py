# 165. Compare Version Numbers

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        for i in range(max(len(v1), len(v2))):
            n1 = int(v1[i]) if i <= len(v1) - 1 else 0
            n2 = int(v2[i]) if i <= len(v2) - 1 else 0
            if n1 < n2:
                return -1
            elif n1 > n2:
                return 1
               
        return 0
    
sol = Solution().compareVersion(version1 = "7.5.2.4", version2 = "7.5.3")
print(sol)