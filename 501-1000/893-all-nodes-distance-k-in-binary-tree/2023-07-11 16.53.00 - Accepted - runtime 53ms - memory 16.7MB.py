# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, k):
        # Build the graph representation of the binary tree
        graph = defaultdict(list)
        self.buildGraph(root, None, graph)

        # Perform breadth-first search starting from the target node
        queue = deque([(target, 0)])  # Node and its distance from target
        visited = {target}
        result = []
        
        while queue:
            node, distance = queue.popleft()
            
            if distance == k:
                result.append(node.val)
            
            if distance > k:
                break
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))
                    visited.add(neighbor)
        
        return result


    def buildGraph(self, node, parent, graph):
        if node:
            if parent:
                graph[node].append(parent)
                graph[parent].append(node)
            
            self.buildGraph(node.left, node, graph)
            self.buildGraph(node.right, node, graph)