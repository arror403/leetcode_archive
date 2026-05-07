# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def get_leaf_nodes(root):
            ##### power by Bing #####
            if root is None: return []
            
            if root.left is None and root.right is None:
                return [root.val]
            
            return get_leaf_nodes(root.left) + get_leaf_nodes(root.right)


        return get_leaf_nodes(root1)==get_leaf_nodes(root2)