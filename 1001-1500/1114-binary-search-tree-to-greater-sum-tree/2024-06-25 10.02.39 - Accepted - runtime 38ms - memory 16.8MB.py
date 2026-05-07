# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        t=self.inorderTraversal(root)
        d={a:b for a,b in zip(t,(list(accumulate(t[::-1])))[::-1])}


        def get_modify(k):
            return d[k]


        def modify_tree_in_order(node, modify_function):
            if node:
                # Traverse the left subtree
                modify_tree_in_order(node.left, modify_function)
                # Modify the current node's value
                node.val = modify_function(node.val)
                # Traverse the right subtree
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