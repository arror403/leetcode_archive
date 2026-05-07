class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stk = []

        for i in range(len(nums)):
            cur = TreeNode(nums[i])

            while stk and stk[-1].val<nums[i]:
                cur.left = stk[-1]
                stk.pop()
            
            if stk: stk[-1].right = cur

            stk.append(cur)
        

        return stk[0]