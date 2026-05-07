# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def left_height(node):
            ht = 0
            while(node):
                ht += 1
                node = node.left
             # Return the left height obtained
            return ht

        
        # Function to get the right height
        # of the binary tree
        def right_height(node):
            ht = 0
            while(node):
                ht += 1
                node = node.right
            # Return the right height obtained
            return ht
        

        # Function to get the count of nodes
        # in complete binary tree
        def TotalNodes(root):
          # Base case
            if(root == None):
                return 0
            # Find the left height and the
            # right heights
            lh = left_height(root)
            rh = right_height(root)
            # If left and right heights are
            # equal return 2^height(1<<height) -1
            if(lh == rh):
                return (1 << lh) - 1
             # Otherwise, recursive call
            return 1 + TotalNodes(root.left) + TotalNodes(root.right)
        
        return TotalNodes(root)