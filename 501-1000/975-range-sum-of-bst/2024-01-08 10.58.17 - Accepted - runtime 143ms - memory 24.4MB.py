# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        def inorder_traversal(t):
            res=[]
            if t:
                res=inorder_traversal(t.left)
                res.append(t.val)
                res+=inorder_traversal(t.right)
            return res

        l=inorder_traversal(root)
        a=next(i for i,v in enumerate(l) if v>=low)
        b=len(l)-next(i for i,v in enumerate(l[::-1]) if v<=high)

        return sum(l[a:b])