class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(root):
            arr = []
            if root:
                arr = inorder(root.left)
                arr.append(root.val)
                arr += inorder(root.right)
            return arr
        
        t = deque(inorder(root))
        if len(t)==1: return TreeNode(t.pop())
        
        res = TreeNode(t.popleft(), None, TreeNode())
        r = res.right

        while t:
            r.val = t.popleft()
            r.left = None
            r.right = TreeNode() if t else None
            r = r.right
        

        return res