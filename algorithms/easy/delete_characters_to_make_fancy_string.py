# 1957. Delete Characters to Make Fancy String

def makeFancyString(self, s: str) -> str:
    stack = []
    for c in s:
        if len(stack) >= 2 and stack[-1] == c and stack[-2] == c:
            continue
        stack.append(c)

    return ''.join(stack)