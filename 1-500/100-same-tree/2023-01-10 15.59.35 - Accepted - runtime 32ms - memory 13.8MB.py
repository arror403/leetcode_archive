# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        # 1. Both empty
        if a is None and b is None:
            return True
        # 2. Both non-empty -> Compare them
        if a is not None and b is not None:
            return ((a.val == b.val) and
                    self.isSameTree(a.left, b.left)and
                    self.isSameTree(a.right, b.right))
        # 3. one empty, one not -- false
        return False