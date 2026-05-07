class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res=0

        def dfs(node, num):
            if not node: 
                return

            nonlocal res
            num+=str(node.val)

            if not node.left and not node.right: 
                res+=int(num, 2)

            dfs(node.left, num)
            dfs(node.right, num)

        dfs(root, '')


        return res