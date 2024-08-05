# 271. Encode and Decode Strings (LeetCode)
# 659 · Encode and Decode Strings (LintCode)

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        encodes = ""
        for s in strs:
            encodes += str(len(s)) + "#" + s
        return encodes

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        strs, i = [], 0
        while i < len(str):
            j = i
            
            while str[j] != "#":
                j += 1
            size = int(str[i:j])
            word = str[j+1:j+size+1]
            strs.append(word)
            i = j + size + 1

        return strs