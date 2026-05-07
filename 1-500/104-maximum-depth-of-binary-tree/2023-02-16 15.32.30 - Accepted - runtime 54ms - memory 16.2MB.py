# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def height(root):   
            # Check if the binary tree is empty
            if root is None:
                # If TRUE return 0
                return 0 
                # Recursively call height of each node
            leftAns = height(root.left)
            rightAns = height(root.right)

            # Return max(leftHeight, rightHeight) at each iteration
            return max(leftAns, rightAns) + 1
        return height(root)