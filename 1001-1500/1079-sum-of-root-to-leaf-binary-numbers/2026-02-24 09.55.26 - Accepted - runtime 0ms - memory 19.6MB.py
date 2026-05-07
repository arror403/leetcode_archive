class Solution:
    def sumRootToLeaf(self, root, val=0):
        # copied from solution, pretty brilliant
        if not root: 
            return 0

        val = val*2 + root.val

        if root.left==root.right: 
            return val


        return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)