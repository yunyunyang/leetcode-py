# 2109. Adding Spaces to a String

from typing import List

def addSpaces(self, s: str, spaces: List[int]) -> str:
    spaces = set(spaces)
    output = []
    for i in range(len(s)):
        if i in spaces:
            output.append(' ')
        output.append(s[i])

    return ''.join(output)