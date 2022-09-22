# 1656. Design an Ordered Stream

from typing import List

class OrderedStream:

    def __init__(self, n: int):
        self.obj = [None] * (n+1)
        self.idx = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.obj[idKey-1] = value
        output = []

        while self.obj[self.idx]:
            output.append(self.obj[self.idx])
            self.idx += 1

        return output
