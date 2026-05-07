# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        return self.PreorderTraversal(root)
        
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.val)
            res += self.PreorderTraversal(root.left)
            res += self.PreorderTraversal(root.right)
        return res