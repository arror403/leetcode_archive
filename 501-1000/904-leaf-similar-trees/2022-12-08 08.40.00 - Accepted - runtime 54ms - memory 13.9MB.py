# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # print(self.get_leaf_nodes(root1))
        return self.get_leaf_nodes(root1)==self.get_leaf_nodes(root2)

    def get_leaf_nodes(self, root):
        leaves = []
        
        # If no child nodes
        if not root.left and not root.right:
            return [root.val]
        
        # If no any left child
        if not root.left:
            leaves = self.get_leaf_nodes(root.right)
        
        # If no any right child
        if not root.right:
            leaves = self.get_leaf_nodes(root.left)
        
        # If has left as well left child
        if root.left and root.right:
            leaves = self.get_leaf_nodes(root.left) + self.get_leaf_nodes(root.right)
        
        return leaves