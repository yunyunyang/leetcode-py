# 2375. Construct Smallest Number From DI String

def smallestNumber(self, pattern: str) -> str:
    res, stack = [], []

    for i in range(len(pattern) + 1):
        stack.append(str(i + 1))
        if i < len(pattern) and pattern[i] == 'I':
            while stack:
                res.append(stack.pop())
    while stack:
        res.append(stack.pop())

    return ''.join(res)