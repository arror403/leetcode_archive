# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        m=inf
        r=self.inorderTraversal(root)
        r.sort()
        for i in range(len(r)-1):
            tmp=(r[i+1]-r[i])
            if tmp<m:
                m=tmp               
        
        return (m)
        
        
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right)
        return res