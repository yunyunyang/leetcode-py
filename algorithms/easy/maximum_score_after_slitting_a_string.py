# 1422. Maximum Score After Splitting a String

def maxScore(self, s: str) -> int:
    zero, one = 0, s.count('1')
    score = 0

    for i in range(len(s) - 1):
        if s[i] == '0':
            zero += 1            
        else:
            one -= 1
        score = max(score, zero + one)

    return score