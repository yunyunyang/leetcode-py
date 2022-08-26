# 804. Unique Morse Code Words

from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        uniqueMorse = set()
        morses = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in words:
            morse = ""
            for j in [*i]:
                morse += morses[ord(j) - 97]
            uniqueMorse.add(morse)

        return len(uniqueMorse)

sol = Solution().uniqueMorseRepresentations(words = ["gin","zen","gig","msg"])
print(sol)