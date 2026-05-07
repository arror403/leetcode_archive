class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.s=0
        
        def reverse_inorder(node):
            if not node: return
            
            reverse_inorder(node.right)
            self.s+=node.val
            node.val=self.s
            reverse_inorder(node.left)
        
        reverse_inorder(root)
        return root