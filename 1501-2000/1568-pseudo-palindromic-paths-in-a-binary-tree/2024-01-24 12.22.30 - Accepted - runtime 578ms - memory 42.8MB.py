# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        ##### power by chatGPT #####

        def dfs(node, path_counts):
            if not node: return 0

            path_counts[node.val] += 1

            if not node.left and not node.right:
                odd_count = sum(c%2!=0 for c in path_counts.values())
                path_counts[node.val] -= 1
                return 1 if odd_count <= 1 else 0
            else:
                total_paths = dfs(node.left, path_counts) + dfs(node.right, path_counts)
                path_counts[node.val] -= 1
                return total_paths

        return dfs(root, Counter())