# 1233. Remove Sub-Folders from the Filesystem

from typing import List

def removeSubfolders(self, folder: List[str]) -> List[str]:
    folder = sorted(folder)
    folder_set = set(folder)
    output = []

    for f in folder:
        output.append(f)
        for i in range(len(f)):
            if f[i] == '/' and f[:i] in output:
                output.pop()
                break

    return output