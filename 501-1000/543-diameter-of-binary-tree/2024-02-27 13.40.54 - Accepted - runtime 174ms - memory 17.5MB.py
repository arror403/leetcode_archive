class Solution:
    ##### power by chatGPT #####
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        max_diameter = 0
        queue = deque([root])

        while queue:
            node = queue.popleft()
            left_depth, right_depth = 0, 0
            if node.left:
                queue.append(node.left)
                left_depth = self.get_depth(node.left)
            if node.right:
                queue.append(node.right)
                right_depth = self.get_depth(node.right)
            
            max_diameter = max(max_diameter, left_depth + right_depth)

        return max_diameter
    

    def get_depth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return depth