# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: # outside of the tree
            return None # didn't find the value
            
        if root.val == val: # if we found the value
            return root # return this node
        elif root.val > val: # if the value is too big, search to the left
            return self.searchBST(root.left, val)
        else: # if the value is too small, search to the right
            return self.searchBST(root.right, val)
