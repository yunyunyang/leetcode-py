# 874. Walking Robot Simulation

from typing import List

def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
    directions, index = [[0, 1], [1, 0], [0, -1], [-1, 0]], 0
    point, max_distance = [0, 0], 0
    obstacles = {tuple(obs) for obs in obstacles}
    for cmd in commands:
        if cmd == -1:
            index = 0 if index == 3 else index + 1
        elif cmd == -2:
            index = 3 if index == 0 else index - 1
        else:
            for _ in range(cmd):
                if (point[0] + directions[index][0],
                    point[1] + directions[index][1]) not in obstacles:
                    point[0] += directions[index][0]
                    point[1] += directions[index][1]
                else:
                    break

            max_distance = max(max_distance, point[0] ** 2 + point[1] ** 2)

    return max_distance