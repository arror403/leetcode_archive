# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        if (r1==None or r2==None): return r1==r2
        else:
            return (r1.val==r2.val and (self.flipEquiv(r1.left, r2.left) and self.flipEquiv(r1.right, r2.right) or self.flipEquiv(r1.left, r2.right) and self.flipEquiv(r1.right, r2.left)))