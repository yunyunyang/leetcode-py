# 1352. Product of the Last K Numbers

def __init__(self):
    self.prefix = [1]
    self.size = 0

def add(self, num: int) -> None:
    if num == 0:
        self.prefix = [1]
        self.size = 0
    else:
        n = self.prefix[-1] * num
        self.prefix.append(n)
        self.size += 1

def getProduct(self, k: int) -> int:
    if k > self.size:
        return 0
    else:
        return self.prefix[-1] // self.prefix[self.size - k]
