# 2182. Construct String With Repeat Limit

def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
    count = [0] * 26
    for c in s:
        count[ord(c) - ord('a')] += 1

    output, i = [], 25
    while i >= 0:
        if count[i] > 0:
            ch = chr(ord('a') + i)
            if count[i] <= repeatLimit:
                output.append(ch * count[i])
                count[i] = 0
            elif count[i] > repeatLimit:
                output.append(ch * repeatLimit)
                count[i] -= repeatLimit
                
                nxt = -1
                for j in range(i - 1, -1, -1):
                    if count[j] > 0:
                        nxt = j
                        count[j] -= 1
                        break

                if nxt == -1:
                    return ''.join(output)
                else:
                    output.append(chr(ord('a') + j))
                    i += 1

        i -= 1

    return ''.join(output)