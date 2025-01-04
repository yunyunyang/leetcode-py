# 1930. Unique Length-3 Palindromic Subsequences

def countPalindromicSubsequence(self, s: str) -> int:
    left, right = set(), {}
    for c in s:
        right[c] = right.get(c, 0) + 1
    
    res = set()
    for c in s:
        right[c] -= 1
        for ch in left:
            if right[ch] > 0:
                res.add((c, ch))
        left.add(c)
        
    return len(res)