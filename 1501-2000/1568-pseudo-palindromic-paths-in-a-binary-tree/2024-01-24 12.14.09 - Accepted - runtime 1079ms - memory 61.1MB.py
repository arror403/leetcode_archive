# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        def is_pseudo_palindromic(path_counts):
            odd_count = sum(count % 2 != 0 for count in path_counts.values())
            return odd_count <= 1


        def dfs(node, path_counts):
            if node:
                path_counts[node.val] += 1

                if not node.left and not node.right:
                    if is_pseudo_palindromic(path_counts):
                        return 1
                else:
                    total_paths = dfs(node.left, path_counts.copy()) + dfs(node.right, path_counts.copy())
                    path_counts[node.val] -= 1  # Backtrack to the parent node
                    return total_paths

            return 0

        return dfs(root, Counter())