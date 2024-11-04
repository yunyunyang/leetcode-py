# 3163. String Compression III

def compressedString(self, word: str) -> str:
    comp = ""

    char, count = word[0], 1
    for i in range(1, len(word)):
        if word[i] == char and count < 9:
            count += 1
        else:
            comp += str(count) + char
            char = word[i]
            count = 1

    return comp + str(count) + char