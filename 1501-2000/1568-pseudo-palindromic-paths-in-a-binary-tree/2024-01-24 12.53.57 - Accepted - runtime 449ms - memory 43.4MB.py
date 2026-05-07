# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        ##### power by COPILOT #####

        def dfs(node, counter):
            if not node: return 0
            counter[node.val] += 1
            res = dfs(node.left, counter) + dfs(node.right, counter)
            if node.left == node.right:  # leaf node
                if sum(v%2 for v in counter)<=1:  # at most one digit has odd occurrences
                    res += 1
            counter[node.val] -= 1
            return res

        return dfs(root, [0]*10)