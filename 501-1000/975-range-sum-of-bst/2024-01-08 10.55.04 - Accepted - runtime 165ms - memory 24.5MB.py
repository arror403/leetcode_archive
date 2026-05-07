# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        def inorder_traversal(root):
            res = []
            if root:
                res = inorder_traversal(root.left)
                res.append(root.val)
                res = res + inorder_traversal(root.right)
            return res

        l=inorder_traversal(root)
        
        # Find the index of the first element greater than or equal to 'begin'
        a = next(i for i,v in enumerate(l) if v>=low)

        # Find the index of the last element less than or equal to 'end'
        b = len(l)-next(i for i,v in enumerate(l[::-1]) if v<=high)


        return sum(l[a:b])