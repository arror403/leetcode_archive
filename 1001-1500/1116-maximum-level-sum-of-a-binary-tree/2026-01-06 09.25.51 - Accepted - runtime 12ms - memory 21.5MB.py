class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        S, level = [], [root]

        while level:
            S.append(sum([node.val for node in level]))
            tmp = []

            for node in level:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
                
            level = tmp


        return max(enumerate(S), key = lambda x: x[1])[0] + 1