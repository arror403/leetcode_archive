# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        def convert_tree_to_graph(root):
            graph = {}
            queue = [(root, None)]

            while queue:
                node, parent_val = queue.pop(0)

                if parent_val is not None:
                    if parent_val not in graph:
                        graph[parent_val] = []
                    graph[parent_val].append(node.val)

                    if node.val not in graph:
                        graph[node.val] = []
                    graph[node.val].append(parent_val)

                if node.left:
                    queue.append((node.left, node.val))

                if node.right:
                    queue.append((node.right, node.val))

            return graph


        def max_distance_to_node(graph, s):
            visited = set()
            queue = deque([(s, 0)])

            while queue:
                current_node, distance = queue.popleft()

                if current_node not in visited:
                    visited.add(current_node)

                    for neighbor in graph.get(current_node, []):
                        queue.append((neighbor, distance + 1))

            return distance-1


        g = convert_tree_to_graph(root)
        # print(g)
        return max_distance_to_node(g, start) if len(g)!=0 else 0