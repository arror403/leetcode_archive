class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return [-1, -1, -1]
            
            # Recursive calls for left and right subtrees
            left_subtree = dfs(node.left)
            right_subtree = dfs(node.right)
            
            # Maximum zigzag path
            max_path = max(
                left_subtree[1] + 1,  # path going right from current node
                right_subtree[0] + 1,  # path going left from current node
                self.max_len
            )
            
            # Update global max length
            self.max_len = max(self.max_len, max_path)
            
            # Return [left path length, right path length, current node max path]
            return [
                left_subtree[1] + 1,  # length of path going right
                right_subtree[0] + 1,  # length of path going left
                max_path
            ]
        
        self.max_len = 0
        dfs(root)

        return self.max_len