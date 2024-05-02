# 2000. Reverse Prefix of Word

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        stack = []
        output = ""
        for w in word:
            if w != ch and not output:
                stack.append(w)
            elif w == ch:
                output += w
                while stack:
                    output += stack.pop()
            else:
                output += w
                
        return output

        
        

    
sol = Solution().reversePrefix(word = "abcdefd", ch = "d")
print(sol)