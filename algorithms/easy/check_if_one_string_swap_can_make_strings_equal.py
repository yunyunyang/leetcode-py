# 1790. Check if One String Swap Can Make Strings Equal

def areAlmostEqual(self, s1: str, s2: str) -> bool:
    if s1 == s2:
        return True
    if len(s1) != len(s2):
        return False

    swap, indexes = 0, []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            swap += 1
            indexes.append(i)
        if swap > 2:
            return False

    if len(indexes) == 2:
        i, j = indexes            
        return s1[i] == s2[j] and s1[j] == s2[i]
    
    return swap == 0