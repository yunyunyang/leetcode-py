# 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
    for idx, word in enumerate(sentence.split(' ')):
        if len(word) >= len(searchWord):
            i = 0
            while i < len(searchWord) and word[i] == searchWord[i]:
                i += 1
        
            if i == len(searchWord):
                return idx + 1

    return -1