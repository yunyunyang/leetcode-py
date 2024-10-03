# 71. Simplify Path

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dirs = path.split("/")
        
        for d in dirs:
            if d == "" or d == ".":
                continue;
            if d == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(d)

        return "/" + "/".join(stack)
