# 2491. Divide Players Into Teams of Equal Skill

from typing import List


def dividePlayers(self, skill: List[int]) -> int:
    skill.sort()

    product, chemistry = 0, skill[0] + skill[-1]
    left, right = 0, len(skill) - 1
    while left < right:
        if skill[left] + skill[right] == chemistry:
            product += skill[left] * skill[right]
            left += 1
            right -= 1
        else:
            return -1

    return product