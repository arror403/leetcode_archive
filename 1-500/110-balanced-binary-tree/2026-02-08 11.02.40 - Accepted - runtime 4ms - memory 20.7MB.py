
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root: return 0
            return max(height(root.left), height(root.right)) + 1
        
        def isBalanced(root):
            if not root: return True
            lh = height(root.left)
            rh = height(root.right)
            # allowed values for (lh - rh) are 1, -1, 0
            if (abs(lh - rh) <= 1) and isBalanced(root.left) and isBalanced(root.right):
                return True
        
            return False


        return isBalanced(root)