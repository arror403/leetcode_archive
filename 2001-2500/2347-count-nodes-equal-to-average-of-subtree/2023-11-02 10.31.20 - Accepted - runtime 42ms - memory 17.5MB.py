# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self.average_subtree_values(root)


    def average_subtree(self, node):
        if node is None: return (0,0)  # Return a tuple (sum, count)

        left_sum, left_count = average_subtree(node.left)
        right_sum, right_count = average_subtree(node.right)

        subtree_sum = left_sum + right_sum + node.val
        subtree_count = left_count + right_count + 1

        return (subtree_sum, subtree_count)

    def average_subtree_values(self, root):
        res = 0  # Initialize res to 0

        def dfs(node):
            nonlocal res  # Declare res as nonlocal so it can be modified

            if node is None: return (0,0)

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            subtree_sum = left_sum + right_sum + node.val
            subtree_count = left_count + right_count + 1

            if node.val == subtree_sum // subtree_count: res += 1

            return (subtree_sum, subtree_count)

        dfs(root)
        return res