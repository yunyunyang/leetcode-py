# 1859. Sorting the Sentence

class Solution:
    def sortSentence(self, s: str) -> str:
        output = ""
        s_list = s.split(" ")
        s_sort = sorted(s_list, key=lambda x:x[-1])
        
        for s in s_sort:
            output += s[0:-1] 
            output += " "

        return output[0:len(output)-1]

sol = Solution().sortSentence(s = "is2 sentence4 This1 a3")
print(sol)