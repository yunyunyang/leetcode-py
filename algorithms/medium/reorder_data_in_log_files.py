# 937. Reorder Data in Log Files

from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        for log in logs:
            if log[-1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
                
        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        return letter_logs + digit_logs
    
sol = Solution().reorderLogFiles(logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])
print(sol)