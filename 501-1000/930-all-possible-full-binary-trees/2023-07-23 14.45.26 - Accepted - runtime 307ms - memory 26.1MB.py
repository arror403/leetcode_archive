# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        # Check whether tree exists for given n value or not.
        if n == 1:
            return [TreeNode(0)]
        
        result = []
        # The tree must have an odd number of nodes, so we use step size 2 in the loop
        for x in range(1, n, 2):
            y = n - 1 - x
            
            # Recursively calculate possible left and right subtrees
            left_trees = self.allPossibleFBT(x)
            right_trees = self.allPossibleFBT(y)
            
            # Combine left and right subtrees to form full binary trees
            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(0)
                    root.left = left_tree
                    root.right = right_tree
                    result.append(root)
        
        return result