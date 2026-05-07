class Solution:
    def isPathCrossing(self, path: str) -> bool:

        ##### power by chatGPT #####

        p = (0, 0)
        visited = set([(0, 0)])

        for move in path:
            if move == 'N':
                p = (p[0], p[1] + 1)
            elif move == 'S':
                p = (p[0], p[1] - 1)
            elif move == 'E':
                p = (p[0] + 1, p[1])
            elif move == 'W':
                p = (p[0] - 1, p[1])

            if p in visited:
                return True

            visited.add(p)

        return False