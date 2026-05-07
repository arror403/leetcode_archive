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


        def binary_search_first_larger_equal(array, target):
            left, right = 0, len(array) - 1
            while left <= right:
                mid = (left + right) // 2
                if array[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left


        def binary_search_last_smaller_equal(array, target):
            left, right = 0, len(array) - 1
            while left <= right:
                mid = (left + right) // 2
                if array[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right


        l=inorder_traversal(root)
        a=binary_search_first_larger_equal(l, low)
        b=binary_search_last_smaller_equal(l, high)+1

        return sum(l[a:b])