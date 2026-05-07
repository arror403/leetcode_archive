# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        f=1
        r=self.inorderTraversal(root)
        if r!=sorted(r): return False
        
        # r.sort()
        for i in range(len(r)-1):
            if r[i+1]>r[i]: 
                continue
            else:
                f=0
                break
            
        # print(r)
        
        return f
        
        
        
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right)
        return res