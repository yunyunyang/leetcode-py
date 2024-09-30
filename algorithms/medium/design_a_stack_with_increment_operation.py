# 1381. Design a Stack With Increment Operation

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.top = -1

    def push(self, x: int) -> None:
        if self.top < len(self.stack) - 1:
            self.top += 1
            self.stack[self.top] = x

    def pop(self) -> int:
        if self.top != -1:            
            val = self.stack[self.top]
            self.top -= 1
            return val
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if k >= len(self.stack):
            k = len(self.stack)
        for i in range(k):
            self.stack[i] += val
