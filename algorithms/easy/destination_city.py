# 1436. Destination City

from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        map_city = dict(zip([x[0] for x in paths], [x[1] for x in paths]))
        for city in map_city.values():
            if city not in map_city.keys():
                return city


sol = Solution().destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])
print(sol)