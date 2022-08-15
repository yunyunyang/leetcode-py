# Goal Parser Interpretation

class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")

sol = Solution().interpret(command = "G()(al)")
print(sol)