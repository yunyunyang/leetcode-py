# 3042. Count Prefix and Suffix Pairs I

from typing import List

def countPrefixSuffixPairs(self, words: List[str]) -> int:
    count = 0
    for i in range(len(words)):
        n = len(words[i])
        for j in range(i + 1, len(words)):
            if words[j][0:n] == words[i] and words[j][len(words[j]) - n:len(words[j])] == words[i]:
                count += 1

    return count