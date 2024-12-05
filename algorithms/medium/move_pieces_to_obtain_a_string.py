# 2337. Move Pieces to Obtain a String

def canChange(self, start: str, target: str) -> bool:
    if start.replace('_', '') != target.replace('_', ''):
        return False

    j = 0
    for i in range(len(start)):
        if start[i] == 'L':
            while j < len(target) and target[j] != 'L':
                j += 1
            if i < j and start[i - 1] != '_':
                return False
            j += 1

        elif start[i] == 'R':
            while j < len(target) and target[j] != 'R':
                j += 1
            if i > j:
                return False
            j += 1

    return True