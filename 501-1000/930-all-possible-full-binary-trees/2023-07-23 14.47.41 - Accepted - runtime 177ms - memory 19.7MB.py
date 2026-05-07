# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n % 2 == 0:
            return []  # No full binary trees can have an even number of nodes
        
        dp = [[] for _ in range(n + 1)]
        dp[1].append(TreeNode(0))
        
        for i in range(3, n + 1, 2):
            for j in range(1, i, 2):
                k = i - j - 1
                for left_tree in dp[j]:
                    for right_tree in dp[k]:
                        root = TreeNode(0)
                        root.left = left_tree
                        root.right = right_tree
                        dp[i].append(root)
        
        return dp[n]