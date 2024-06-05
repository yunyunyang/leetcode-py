# 345. Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', \
                  'A', 'E', 'I', 'O', 'U']
        
        output = list(s)
        l, r = 0, len(s) - 1
        while l <= r:
            if output[l] not in vowels:
                l += 1
            elif output[r] not in vowels:
                r -= 1
            else:
                output[l], output[r] = output[r], output[l]
                l += 1
                r -= 1
            
        return ''.join(output)
    
sol = Solution().reverseVowels(s = "hello")
print(sol)