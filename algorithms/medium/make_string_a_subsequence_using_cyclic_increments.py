# 2825. Make String a Subsequence Using Cyclic Increments

def canMakeSubsequence(self, str1: str, str2: str) -> bool:
    j = 0
    for i in range(len(str1)):
        s1 = ord(str1[i]) - ord('a')
        s2 = ord(str2[j]) - ord('a')
        if s1 == s2 or (s1 + 1) % 26 == s2:
            j += 1

        if j == len(str2):
            return True

    return False