# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        d = deque()
        d.append(root)
        max_sum = float('-inf')
        level = 1

        while d:
            level_sum = 0
            for _ in range(len(d)):
                node = d.popleft()
                level_sum += node.val

                if node.left: d.append(node.left)
                if node.right: d.append(node.right)

            if level_sum > max_sum:
                max_sum, max_level = level_sum, level

            level += 1


        return max_level