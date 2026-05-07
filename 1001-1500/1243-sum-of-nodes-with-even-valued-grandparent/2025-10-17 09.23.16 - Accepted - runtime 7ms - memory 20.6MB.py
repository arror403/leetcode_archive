# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode], p = 1, gp = 1) -> int:
        return (self.sumEvenGrandparent(root.left, root.val, p)
              + self.sumEvenGrandparent(root.right, root.val, p)
              + (0 if gp%2 else root.val)) if root else 0