class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(current, parent, grandParent):
            nonlocal res
            if (current == None): return # base case 
            if (grandParent != None) and (grandParent.val%2 == 0):
                res += current.val
            
            dfs(current.left, current, parent) # (newChild, parent, GrandParent)
            dfs(current.right, current, parent)

        dfs(root, None, None)


        return res