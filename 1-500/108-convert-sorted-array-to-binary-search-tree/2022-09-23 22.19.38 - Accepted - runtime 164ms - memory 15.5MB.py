# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self._sortedArrayToBST(nums)
    
    def _sortedArrayToBST(self, arr):
        if not arr:
            return None
        # find middle index
        mid = (len(arr)) // 2
        # make the middle element the root
        root = TreeNode(arr[mid])
        # left subtree of root has all
        # values <arr[mid]
        root.left = self._sortedArrayToBST(arr[:mid])
        # right subtree of root has all
        # values >arr[mid]
        root.right = self._sortedArrayToBST(arr[mid+1:])
        return root