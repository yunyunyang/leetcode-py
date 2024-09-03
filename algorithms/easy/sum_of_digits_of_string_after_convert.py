# 1945. Sum of Digits of String After Convert

def getLucky(self, s: str, k: int) -> int:
    num = ''
    for c in s:
        num += str(ord(c) - ord('a') + 1)
        
    while k > 0:
        tmp = 0
        for digit in num:
            tmp += int(digit)
        num = str(tmp)
        k -= 1

    return int(num)