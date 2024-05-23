# 290. Word Pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patterns = list(pattern)
        words = s.split(' ')
        
        if len(patterns) != len(words):
            return False
        
        dicts = {}
        seen = set()
        for k, v in zip(patterns, words):
            if k not in dicts and v not in seen:
                dicts[k] = v
                seen.add(v)
            else:
                if k not in dicts or dicts[k] != v:
                    return False
                
        return True