# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def helper(res, root, d):
            if ( not root):
                return
            # Expand list size
            if (d == len(res)):
                res.append(root.val)
            else:
                # to ensure largest value
                # on level is being stored
                res[d] = max(res[d], root.val)
            # Recursively traverse left and
            # right subtrees in order to find
            # out the largest value on each level
            helper(res, root.left, d + 1)
            helper(res, root.right, d + 1)


        # function to find largest values
        def largestValues(root):
            res = []
            helper(res, root, 0)
            return res
        
        return largestValues(root)