# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        ##### power by chatGPT, Bing #####
        ##### improved by Bing #####

        def convert_tree_to_graph(root):
            graph = defaultdict(list)
            queue = deque([(root, None)])

            while queue:
                node, parent_val = queue.popleft()

                if parent_val is not None:
                    graph[parent_val].append(node.val)
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

                    for neighbor in graph[current_node]:
                        if neighbor not in visited:
                            queue.append((neighbor, distance + 1))

            return distance



        g = convert_tree_to_graph(root)
        return max_distance_to_node(g, start) if g else 0