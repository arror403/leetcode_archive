class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        t=self.inorderTraversal(root)
        d={a:b for a,b in zip(t,list(accumulate(t[::-1]))[::-1])}


        def get_modify(k):
            return d[k]


        def modify_tree_in_order(node, modify_function):
            if node:
                modify_tree_in_order(node.left, modify_function)
                node.val = modify_function(node.val)
                modify_tree_in_order(node.right, modify_function)


        modify_tree_in_order(root, get_modify)

        return root



    def inorderTraversal(self, root):
        res=[]
        if root:
            res=self.inorderTraversal(root.left)
            res.append(root.val)
            res+=self.inorderTraversal(root.right)
        return res