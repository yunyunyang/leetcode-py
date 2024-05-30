# 981. Time Based Key-Value Store

class TimeMap:

    def __init__(self):
        self.key_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_store:
            self.key_store[key] = []
        self.key_store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        output, values = "", self.key_store.get(key, [])
        l, r = 0, len(values)
        while l <= r:
            m = l + (r - l) // 2
            if values[m][1] <= timestamp:
                output = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return output
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)