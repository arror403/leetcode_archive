# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # Base case 1: We've reached the end of a branch (node is None).
        if not original:
            return None
        
        # Base case 2: We've found the target node in the original tree.
        if original == target:
            # Return the corresponding node from the cloned tree.
            return cloned
        
        # Recursive step: Search in the left subtree.
        left_result = self.getTargetCopy(original.left, cloned.left, target)
        if left_result:
            # If we found the target in the left subtree, return it immediately.
            return left_result
        
        # If not in the left, search in the right subtree and return its result.
        return self.getTargetCopy(original.right, cloned.right, target)