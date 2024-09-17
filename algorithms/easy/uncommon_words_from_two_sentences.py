# 884. Uncommon Words from Two Sentences

from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a1, a2 = s1.split(" "), s2.split(" ")
        count = {}
        for w in a1 + a2:            
            count[w] = count.get(w, 0) + 1

        output = []
        for k, v in count.items():
            if v == 1:
                output.append(k)
        
        return output