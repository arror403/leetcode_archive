# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], x: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(x,None,None)
        else:
            if root.val <= x:
                root.right = self.insertIntoBST(root.right, x)
            else:
                root.left = self.insertIntoBST(root.left, x)
            return root