class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # power by chatGPT
        adjacency = {}
        for pair in adjacentPairs:
            adjacency.setdefault(pair[0], []).append(pair[1])
            adjacency.setdefault(pair[1], []).append(pair[0])

        start = None
        for key, values in adjacency.items():
            if len(values) == 1:
                start = key
                break

        size = len(adjacentPairs) + 1
        result = [0] * size
        result[0] = start
        result[1] = adjacency[start][0]

        for i in range(2, size):
            current = result[i - 1]
            neighbors = adjacency[current]
            result[i] = neighbors[0] if result[i - 2] != neighbors[0] else neighbors[1]

        return result