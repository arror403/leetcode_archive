# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def inorderTraversal(a, b):
            if a:
                inorderTraversal(a.left, b.left)
                if a == target: 
                    self.res = b
                inorderTraversal(a.right, b.right)

        inorderTraversal(original, cloned)


        return self.res