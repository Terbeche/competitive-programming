from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [ i for i in range(26)]
        size = [ 1 for i in range(26)]
  
        def find(var):
            if var == parent[var]:
                return var
            
            parent[var] = find(parent[var])
            return parent[var]

        def union(var1, var2):
            part1, part2 = find(var1), find(var2)

            if part1 == part2:
                return
            if size[part1] > size[part2]:
                parent[part2] = part1
                size[part1] += part2

            else:
                parent[part1] = part2
                size[part2] += part1

        for equation in equations:
            var1, var2 = equation[0], equation[-1]
            var1 = ord(var1) - 97
            var2 = ord(var2) - 97
            condition = equation[1]

            if condition == "=":
                union(var1, var2)

        for equation in equations:
            var1, var2 = equation[0], equation[-1]
            var1 = ord(var1) - 97
            var2 = ord(var2) - 97
            condition = equation[1]

            if condition != "=":
                if find(var1) == find(var2):
                    return False

        return True
