# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lca(root,p,q)
        
        
        
        
    def lca(self, root, n1, n2):
        while root:
            # If both n1 and n2 are smaller than root,
            # then LCA lies in left
            if root.val > n1.val and root.val > n2.val:
                root = root.left
                
            # If both n1 and n2 are greater than root,
            # then LCA lies in right
            elif root.val < n1.val and root.val < n2.val:
                root = root.right

            else: break

        return root