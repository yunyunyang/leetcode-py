# 1268. Search Suggestions System

from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        
        output = []
        for i in range(1, len(searchWord) + 1):
            r = []
            for p in products:
                if p[:i] == searchWord[:i] and len(r) < 3:
                    r.append(p)
            output.append(r)
            
        return output
    
sol = Solution().suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse")
print(sol)