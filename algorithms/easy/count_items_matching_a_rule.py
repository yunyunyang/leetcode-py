# 1773. Count Items Matching a Rule

from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        output = 0 
        for i in items:
            if ruleKey == "type" and i[0] == ruleValue:
                output += 1
            if ruleKey == "color" and i[1] == ruleValue:
                output += 1
            if ruleKey == "name" and i[2] == ruleValue:
                output += 1
            
        return output

sol = Solution().countMatches(items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver")
print(sol)
