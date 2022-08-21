# 2325. Decode the Message

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        output = ""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        ks = "".join(dict.fromkeys(key.replace(" ", "")))
        dic = dict(zip(ks, alphabet))
        dic[" "] = " "
        
        for m in [*message]:
            output += dic.get(m)

        return output

sol = Solution().decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv")
print(sol)
