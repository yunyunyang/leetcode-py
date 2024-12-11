# 2981. Find Longest Special Substring That Occurs Thrice I (Google)
def maximumLength(self, s: str) -> int:
    count = {}
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            count[sub] = count.get(sub, 0) + 1

    output = -1
    for k, v in count.items():
        if v >= 3 and len(set(k)) == 1:
            output = max(output, len(k))

    return output