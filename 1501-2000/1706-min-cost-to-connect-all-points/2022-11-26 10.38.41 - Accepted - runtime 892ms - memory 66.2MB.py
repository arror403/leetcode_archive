class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points_set = set(range(len(points)))
        heap = [(0, 0)]
        visited_node = set()
        total_distance = 0
        while heap and len(visited_node) < len(points):
            distance, current_index = heapq.heappop(heap)
            if current_index not in visited_node:
                visited_node.add(current_index)
                points_set.discard(current_index)
                total_distance += distance
                x0, y0 = points[current_index]
                for next_index in points_set:
                    x1, y1 = points[next_index]
                    heapq.heappush(heap, (abs(x0 - x1) + abs(y0 - y1), next_index))
        return total_distance