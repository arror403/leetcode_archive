class Solution:
    ##### power by chatGPT #####
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        
        def depth(node):
            if not node: return 0
            # Recursively find the depth of left and right subtrees
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            # Update the max_length if the sum of depths is greater
            self.max_length = max(self.max_length, left_depth + right_depth)
            # Return the depth of the current node
            return 1+max(left_depth, right_depth)
        
        depth(root)

        return self.max_length