class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def SumUnder(root):
            nonlocal res
            nonlocal totalTreeSum
            if root == None: return 0
            S = SumUnder(root.left) + SumUnder(root.right) + root.val
            res = max(res, S*(totalTreeSum-S))

            return S

        totalTreeSum = 0
        res = 0
        totalTreeSum = SumUnder(root)
        SumUnder(root)


        return res % (10**9 + 7)