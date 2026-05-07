class Solution:
    def isSameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:

        ##### improved by chatGPT #####

        # 1. Early exit condition if either tree is empty
        if not a or not b:
            return a is None and b is None

        # 2. Compare values and recursively check left and right subtrees
        return (a.val == b.val) and \
               self.isSameTree(a.left, b.left) and \
               self.isSameTree(a.right, b.right)
