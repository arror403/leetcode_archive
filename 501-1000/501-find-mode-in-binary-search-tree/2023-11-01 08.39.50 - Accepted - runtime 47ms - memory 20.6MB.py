# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        t=Counter(self.bst_to_list(root))
        m=max(t.values())
        return [v for v,f in t.items() if f==m]


    def inorder_traversal(self, root, result):
        if root:
            self.inorder_traversal(root.left, result)
            result.append(root.val)
            self.inorder_traversal(root.right, result)


    def bst_to_list(self, root):
        result = []
        self.inorder_traversal(root, result)
        return result