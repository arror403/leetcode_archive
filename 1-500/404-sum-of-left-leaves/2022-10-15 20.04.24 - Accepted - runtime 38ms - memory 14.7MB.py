# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # A utility function to check if a given node is leaf or not
        def isLeaf(node):
            if node is None:
                return False
            if node.left is None and node.right is None:
                return True
            return False
        
        # This function return sum of all left leaves in a
        # given binary tree
        def leftLeavesSum(root):
        
            # Initialize result
            res = 0
            
            # Update result if root is not None
            if root is not None:
        
                # If left of root is None, then add key of
                # left child
                if isLeaf(root.left):
                    res += root.left.val
                else:
                    # Else recur for left child of root
                    res += leftLeavesSum(root.left)
        
                # Recur for right child of root and update res
                res += leftLeavesSum(root.right)
            return res
        return leftLeavesSum(root)