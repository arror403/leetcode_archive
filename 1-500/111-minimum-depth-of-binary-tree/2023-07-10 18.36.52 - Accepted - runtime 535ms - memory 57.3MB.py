# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # If the root has no children, it is a leaf node
        if not root.left and not root.right:
            return 1

        # If the root has a left child but no right child, calculate the depth of the left subtree
        if not root.right:
            return 1 + self.minDepth(root.left)

        # If the root has a right child but no left child, calculate the depth of the right subtree
        if not root.left:
            return 1 + self.minDepth(root.right)

        # If the root has both left and right children, calculate the minimum depth of the two subtrees
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))