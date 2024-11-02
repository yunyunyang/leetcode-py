# 2490. Circular Sentence

def isCircularSentence(self, sentence: str) -> bool:
    words = sentence.split()
    if len(words) == 1 and sentence[0] != sentence[-1]:
        return False

    for i in range(1, len(words)):
        if words[i][0] != words[i - 1][-1]:
            return False
        if i == len(words) - 1 and words[len(words) - 1][-1] != words[0][0]:
            return False

    return True