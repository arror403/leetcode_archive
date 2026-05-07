class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder: return None

        root = TreeNode(preorder[0])
        if len(preorder)==1: return root
        
        i = postorder.index(preorder[1])
        
        root.left = self.constructFromPrePost(preorder[1:i+2], postorder[:i+1])
        root.right = self.constructFromPrePost(preorder[i+2:], postorder[i+1:-1])
        
        return root