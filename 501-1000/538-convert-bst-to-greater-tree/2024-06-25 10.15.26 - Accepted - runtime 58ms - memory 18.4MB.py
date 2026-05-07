class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.s=0
        
        def reverse_inorder(node):
            if not node: return
            
            reverse_inorder(node.right)
            self.s += node.val
            node.val = self.s
            reverse_inorder(node.left)
        
        reverse_inorder(root)
        return root