# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        totalTreeSum=0
        result=0
        def SumUnder(root):
            nonlocal result
            nonlocal totalTreeSum
            if root==None: return 0
            sum=SumUnder(root.left)+SumUnder(root.right)+root.val
            result=max(result, sum*(totalTreeSum-sum))
            return sum

        totalTreeSum=SumUnder(root)
        SumUnder(root)
        return result%(10**9+7)
        