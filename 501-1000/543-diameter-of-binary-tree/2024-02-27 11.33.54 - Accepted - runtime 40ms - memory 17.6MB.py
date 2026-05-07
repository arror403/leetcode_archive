# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_length = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            # max_length=0
            if not node: return -1 # Returning -1 to count edges, if counting nodes return 0 instead of -1
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            # Update the maximum length if the sum of left and right depths is greater
            self.max_length = max(self.max_length, left_depth + right_depth + 2)
            # Return the depth of the current node
            return 1 + max(left_depth, right_depth)
        
        dfs(root)

        return self.max_length