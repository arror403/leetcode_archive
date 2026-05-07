# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def deleteLeaves(root, x):
            if root==None: return None

            root.left=deleteLeaves(root.left, x) 
            root.right=deleteLeaves(root.right, x) 

            if root.val==x:
                if root.left==None and root.right==None:
                    return None

            return root
        
        
        return deleteLeaves(root, target)