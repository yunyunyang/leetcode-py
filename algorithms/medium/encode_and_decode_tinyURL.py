# 535. Encode and Decode TinyURL

class Codec:

    def __init__(self):
        self.dict = {}

    def encode(self, longUrl: str) -> str:
        shortUrl = hash(longUrl)
        self.dict[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.dict[shortUrl]
        

# Your Codec object will be instantiated and called as such:
codec = Codec()
codec.decode(codec.encode(url = "https://leetcode.com/problems/design-tinyurl"))