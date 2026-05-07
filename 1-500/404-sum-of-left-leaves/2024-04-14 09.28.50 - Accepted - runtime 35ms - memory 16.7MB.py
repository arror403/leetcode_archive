# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def isLeaf(node):
            return node and (node.left==None) and (node.right==None)
            
        # @lru_cache(maxsize=None)
        def leftLeavesSum(t):
            res=0
            
            if t:
                if isLeaf(t.left):
                    res+=t.left.val
                else:
                    res+=leftLeavesSum(t.left)
        
                res+=leftLeavesSum(t.right)

            return res

        return leftLeavesSum(root)