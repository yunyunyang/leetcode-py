# 1002. Find Common Characters

from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counters = []
        for w in words:
            count = {}
            for c in w:
                count[c] = count.get(c, 0) + 1
            counters.append(count)
        
        output = []
        size = len(words)
        first = counters[0]
        for k, v in first.items():
            count = 0
            for counter in counters:
                if k in counter and v == counter[k]:
                    count += 1
                elif k in counter and v != counter[k]:
                    first[k] = min(first[k], counter[k])
                    count += 1
            
            if count == size:
                output.extend([k] * first[k])
            
        return output
    
    
sol = Solution().commonChars(words = ["bella","label","roller"])
print(sol)