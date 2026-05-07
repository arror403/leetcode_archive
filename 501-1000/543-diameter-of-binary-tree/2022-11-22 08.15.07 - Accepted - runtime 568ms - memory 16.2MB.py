# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # The function Compute the "height" of a tree. Height is the
        # number of nodes along the longest path from the root node
        # down to the farthest leaf node.
        
        def height(node):
        
            # Base Case : Tree is empty
            if node is None:
                return 0
        
            # If tree is not empty then height = 1 + max of left
            # height and right heights
            return 1 + max(height(node.left), height(node.right))
        
        # Function to get the diameter of a binary tree
        
        
        def diameter(root):
        
            # Base Case when tree is empty
            if root is None:
                return 0
        
            # Get the height of left and right sub-trees
            lheight = height(root.left)
            rheight = height(root.right)
        
            # Get the diameter of left and right sub-trees
            ldiameter = diameter(root.left)
            rdiameter = diameter(root.right)
        
            # Return max of the following tree:
            # 1) Diameter of left subtree
            # 2) Diameter of right subtree
            # 3) Height of left subtree + height of right subtree +1
            return max(lheight + rheight + 1, max(ldiameter, rdiameter))
        return diameter(root)-1